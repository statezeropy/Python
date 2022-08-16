# 네이버 쇼핑 -> 아이폰 케이스 검색
# 제목 크롤링하기
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%20%EC%BC%80%EC%9D%B4%EC%8A%A4&cat_id=&frm=NVSHATC"
res = req.get(url)
soup = BS(res.text, "html.parser")

arr = soup.select("ul.list_basis div>a:first-child[title]")
print(arr)
for a in arr:
    print(a.get_text(strip=True))