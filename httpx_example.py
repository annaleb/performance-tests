import httpx
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.status_code)
# print(response.url)
# print(response.text)
client = httpx.Client(headers={"Authorization": "Bearer my_token"},
                      base_url="https://jsonplaceholder.typicode.com/")
response1 = client.get("todos/1")
response2 = client.get("todos/2")
print(response1.status_code)
print(response2.request.headers)
print(response1.json(), response2.text)


