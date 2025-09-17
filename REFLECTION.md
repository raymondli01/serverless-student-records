# Reflection

Briefly describe the challenges you faced and what you learned from using AWS Lambda and DynamoDB.

## Setup & Wiring
- Creating the DynamoDB table and connecting API Gateway → Lambda.

## Issues & Debugging
- Example: initial 500 errors due to missing IAM permissions; fixed by attaching DynamoDB permissions to the Lambda role.

## Testing
- Verified with curl/Postman; confirmed records existed in DynamoDB (`StudentRecords`).

## Learnings
- How Lambda proxy events map to HTTP methods, body, and query params.
- Basics of IAM (least privilege).
- DynamoDB partition key usage and item structure.
