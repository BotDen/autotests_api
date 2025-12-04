import httpx

from tools.fakers import get_random_email

user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "smit",
    "firstName": "bob",
    "middleName": "string",
}
created_user_response = httpx.post("http://localhost:8000/api/v1/users", json=user_payload)
print(created_user_response.status_code)
print(created_user_response.json())
