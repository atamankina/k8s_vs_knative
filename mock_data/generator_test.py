import requests
from urllib.parse import urljoin

data = {
    "email": "hstollhofer0@auda.au",
    "name": "helloway0"
}

url = urljoin('http://192.168.99.102:31703', 'users/')
print(url)
res = requests.get(url=url)
print(res.status_code)

response = requests.post(url=url, json=data)
print(response.status_code)