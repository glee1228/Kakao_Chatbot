import requests

url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
res = requests.get(url).json()
print(res[0]['url'])