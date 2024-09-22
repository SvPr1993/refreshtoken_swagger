import pickle
import requests


# Сделать так, чтобы код заработал, по возможности оптимизировать его
def main():
    if response.status_code == 200:
        print("Все в порядке")
    elif response.status_code == 401:
        print("Статус 401")
        update_token()
    else:
        print("Неизвестная ошибка")
    header = {"Authorization": f"Bearer {access_token_load}"}
    refresh_body = {"refresh": refresh_token_load}
    response = requests.get("http://127.0.0.1:8000/api/products/home/", headers=header)
    print(response)
    print(response.json())
    header = {"Authorization": f"Bearer {token_access}"}
    print(response)
    print(response.json())


def load_tokens_from_file() -> tuple[str, str]:
    with open("access_token.pickle", "rb") as file:
        access_token_load = pickle.load(file)
        print(access_token_load)
    with open("refresh_token.pickle", "rb") as file:
        refresh_token_load = pickle.load(file)
        print(refresh_token_load)
    return access_token_load, refresh_token_load


def update_token():
    print("start update token")
    refresh_token = refresh_token_load
    print(refresh_token)
    refresh_body_new = {"refresh": refresh_token}
    response_refresh = requests.post("http://127.0.0.1:8000/api/token/refresh/", data=refresh_body_new)
    print("Cтатус код", response_refresh.status_code)
    json = response_refresh.json()
    token_access = json["access"]
    print(token_access)


def save_access_token(access_token: str):
    with open("access_token.pickle", "wb") as f:
        pickle.dump(access_token, f)
        print("File save, OK")
