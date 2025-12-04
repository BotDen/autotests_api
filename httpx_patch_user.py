import httpx

from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "123456",
    "firstName": "John",
    "lastName": "Smith",
    "middleName": "dog",
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_json = create_user_response.json()
print(create_user_response.status_code)
print("Created user: ", create_user_response_json)


login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_json = login_response.json()
print(login_response.status_code)
print("Logged in user: ", login_response_json)


update_user_headers = {
    "Authorization": f"Bearer {login_response_json["token"]["accessToken"]}"
}
update_user_payload = {
    "firstName": "Danny",
    "lastName": "Boy",
}
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_json["user"]["id"]}",
                                    headers=update_user_headers, json=update_user_payload)
update_user_response_json = update_user_response.json()
print(update_user_response.status_code)
print("Updated user: ", update_user_response_json)
