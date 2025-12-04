import httpx
from httpx import Response

login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_json = login_response.json()

def get_refresh_access_token() -> Response:
    refresh_payload = {"refreshToken": login_response_json["token"]["refreshToken"]}
    refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
    return refresh_response

client = httpx.Client(headers={"Authorization": "Bearer " + login_response_json["token"]["accessToken"]})
with client:
    me_response = client.get("http://localhost:8000/api/v1/users/me")
    print(me_response.json())
