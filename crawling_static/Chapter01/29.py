# https://webhook.site/
import requests as req

url = "https://webhook.site/8e50f687-a208-455b-b2aa-9e6dea07f08d"
res = req.get(url)

print(res.text)