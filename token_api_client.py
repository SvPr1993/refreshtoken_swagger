import pickle
from django.conf import settings
import requests
from django.http import HttpResponse

#url = 'http://127.0.0.1:8000/api/token/'
#
#settings.configure()
#
#body = {
#    "username": "admin",
#    "password": "admin"
# }
#
#r = requests.post(url, data=body)
#
#print(r)
#
#access_token = r.json()["access"]
#refresh_token = r.json()["refresh"]
#with open("access_token.pickle", "wb") as f:
#   pickle.dump(access_token, f)
#
#
#with open("refresh_token.pickle", "wb") as f:
#   pickle.dump(refresh_token, f)


with open("access_token.pickle", "rb") as file:
    access_token_load = pickle.load(file)
    print(access_token_load)

with open("refresh_token.pickle", "rb") as file:
    refresh_token_load = pickle.load(file)
    print(refresh_token_load)

header = {"Authorization": f"Bearer {access_token_load}"}

refresh_body = {"refresh": refresh_token_load}

response = requests.get("http://127.0.0.1:8000/api/products/home/", headers=header)
response_refresh = requests.post("http://127.0.0.1:8000/api/token/refresh/", data=refresh_body)
print(response)
print(response.json())
print(response_refresh)
print(response_refresh.json())

# if access_token and refresh_token == HttpResponse(status=403):
#    def new_token():
#        a = requests.post(url, data=body)
#        print(a)
# else:
#    pass
