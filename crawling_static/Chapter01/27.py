from bs4 import BeautifulSoup as BS
import requests as req

# 네이버 - 금융 - 국내증시 - 우측 인기 검색 종목 더보기
url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

#for title in soup.select("a.tltle"): # title 오타 주의
#    print(title.get_text(strip=True))

# chrome에 문법에 맞게 꾸며줌.. 그거에 낚일 수 있으니
# 소스보기로 보는게 더 정확함
for tr in soup.select("table.type_5 tr"):
    if len(tr.select("a.tltle")) == 0: # 빈칸 등은 넘어가기
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True) # 오타 있음
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    print(title, price, change)