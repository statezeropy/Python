# 쿠팡 -> 노트북 검색
# 제목 크롤링하기
# 쿠팡은 막힌듯..
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = req.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
})
soup = BS(res.text, "html.parser")

# list comprehension : for문이 내장된 리스트?
#[a for a in range(5)]
# 0 1 2 3 4

arr = soup.select("div.name")
print(arr)
for a in arr:
    print(a.get_text(strip=True))

# 헤더 값 설정 안하면... 막힘
# 헤더값 추출
# 개발자도구 - Network - 새로고침 - Request Header 에서 User-Agent 값 찾기
#res = req.get(url, headers={
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#})


