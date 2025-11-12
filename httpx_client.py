import httpx
import time
# Шаг 1 Создаем пользователя напрямую в коде
# create_user_payload = {
#   "email": f"negodanna.{time.time()}@example.com",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"
# }
# create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
# create_user_response_data = create_user_response.json()

# Шаг 1 Создаем пользователя c httpx Client
client = httpx.Client(base_url="http://localhost:8003",
                      timeout=5)  # headers={"Authorization": "Bearer ..."}
payload = {
    "email": f"negodanna.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = client.post("/api/v1/users", json=payload)


