import requests

url = "https://catfact.ninja/fact"  # working endpoint
r = requests.get(url)
data = r.json()
print(data["fact"])
