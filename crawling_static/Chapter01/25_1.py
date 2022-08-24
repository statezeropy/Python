# 25.py 이어서 작업
# 광고 제거?
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = req.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
})
soup = BS(res.text, "html.parser")

for desc in soup.select("div.descriptions-inner"):
    ads = desc.select("span.ad-badge")
    if len(ads) > 0:
        print("광고!")
    print(desc.select("div.name")[0].get_text(strip=True))