import httpx


response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())


json_data = {
    "title": "my title",
    "completed": False,
    "userId": "1",
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=json_data)
print(response.status_code)
print(response.headers)
print(response.json())


data = {"username": "admin", "password": "12345"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.headers)
print(response.json())


params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.status_code)
print(response.url)
