import json
import boto3

# DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')  # Make sure this matches your table name

def lambda_handler(event, context):
    method = event.get("httpMethod", "")

    if method == "POST":
        # Create a new student record
        if not event.get("body"):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing request body"})
            }
        
        student = json.loads(event["body"])
        table.put_item(Item=student)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Student record added successfully"})
        }

    elif method == "GET":
        # Fetch student record by student_id
        params = event.get("queryStringParameters") or {}
        student_id = params.get("student_id")
        if not student_id:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "student_id query parameter is required"})
            }

        response = table.get_item(Key={"student_id": student_id})
        item = response.get("Item")

        if not item:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": f"Student with id {student_id} not found"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }

    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": f"Method {method} not allowed"})
        }
