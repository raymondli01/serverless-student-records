# Serverless Student Records (AWS Lambda + DynamoDB)

This repo contains the code and artifacts for the assignment **"Building a Serverless Web Application with AWS Lambda and DynamoDB"**.

## What’s included
- **lambda/lambda_function.py** — Python handler implementing POST (create) and GET (read) for the `StudentRecords` table.
- **scripts/curl_examples.sh** — Ready-to-run `curl` commands that hit your API Gateway endpoint.
- **policies/dynamodb-crud-studentrecords.json** — Least-privilege IAM policy example.
- **postman_collection.json** — Postman collection with POST and GET requests prefilled.
- **screenshots/** — Put your proof screenshots here (DynamoDB table items, successful API calls).

## API Gateway endpoint
> Replace with your own when grading; currently set to your working endpoint:
```
https://7pjdrb32we.execute-api.us-east-2.amazonaws.com/dev
```

Endpoints used:
- `POST /students` — create student record
- `GET /students?student_id=...` — fetch a record by id

## Test quickly with curl
```bash
bash scripts/curl_examples.sh
```

Or copy/paste:
```bash
curl -X POST "https://7pjdrb32we.execute-api.us-east-2.amazonaws.com/dev/students"   -H "Content-Type: application/json"   -d '{ "student_id": "123", "name": "John Doe", "course": "Enterprise Software" }'

curl -X GET "https://7pjdrb32we.execute-api.us-east-2.amazonaws.com/dev/students?student_id=123"
```

## IAM (least privilege policy)
See **policies/dynamodb-crud-studentrecords.json** and replace `<ACCOUNT_ID>` with your AWS account id before using.

## Notes
- DynamoDB table name: **StudentRecords** (PK: `student_id` as String).
- Region used: **us-east-2 (Ohio)**.
- API Gateway: REST API with resources `POST /students` and `GET /students` (Lambda proxy integration).

## Screenshots to include
Place the following under **screenshots/**:
- Successful **POST** and **GET** (from CloudShell or Postman).
- DynamoDB **Explore table items** showing inserted records.
