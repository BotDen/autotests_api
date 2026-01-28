import httpx

from tools import fakers

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "smit",
    "firstName": "bob",
    "middleName": "string",
}
created_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
created_user_response_json = created_user_response.json()
print(created_user_response.status_code)
print(f"Created user: {created_user_response_json}")

user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_payload)
login_response_json = login_response.json()
print(login_response.status_code)
print(f"Logged in user: {login_response_json}")

delete_user_headers = {
    "Authorization": f"Bearer {login_response_json["token"]["accessToken"]}"
}
delete_user_response = httpx.delete(f"http://localhost:8000/api/v1/users/{created_user_response_json["user"]["id"]}",
                                    headers=delete_user_headers)
print(delete_user_response.status_code)
