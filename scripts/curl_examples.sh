#!/usr/bin/env bash
set -euo pipefail

URL_BASE="https://7pjdrb32we.execute-api.us-east-2.amazonaws.com/dev"

echo "POST create 123"
curl -s -X POST "$URL_BASE/students"   -H "Content-Type: application/json"   -d '{ "student_id": "123", "name": "John Doe", "course": "Enterprise Software" }' | jq . || true
echo

echo "GET 123"
curl -s -X GET "$URL_BASE/students?student_id=123" | jq . || true
echo

echo "POST create 124"
curl -s -X POST "$URL_BASE/students"   -H "Content-Type: application/json"   -d '{ "student_id": "124", "name": "Jane Smith", "course": "Distributed Systems" }' | jq . || true
echo

echo "GET 124"
curl -s -X GET "$URL_BASE/students?student_id=124" | jq . || true
echo
