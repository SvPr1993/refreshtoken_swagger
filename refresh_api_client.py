import requests
import pickle

url = 'http://127.0.0.1:8000/api/token/'


body = {
    "username": "admin",
    "password": "admin"
}


r = requests.post(url, data=body)

print(r)

access_token = r.json()["access"]
refresh_token = r.json()["refresh"]


with open("token.pickle", "wb") as f:
    pickle.dump(access_token, f)


with open("token.pickle", "rb") as file:
    token_load = pickle.load(file)
    print(token_load)
