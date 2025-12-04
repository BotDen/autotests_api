import httpx

login_payload = {
    "email": "test1764845519.8827214@example.com",
    "password": "123456",
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_json = login_response.json()
print(login_response.status_code)
print("Logged in user: ", login_response_json)

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=3,
    headers={"Authorization": f"Bearer {login_response_json["token"]["accessToken"]}"}
)
get_me_response = client.get("/api/v1/users/me")
get_me_response_json = get_me_response.json()
print(get_me_response.status_code)
print("me data:", get_me_response_json)
