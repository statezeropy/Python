from bs4 import BeautifulSoup as BS
import requests as req

# html의 iframe은 다른 곳의 html을 가져옴

url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

names = []
for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    #print(td.string) # 기본 출력. 공백이 너무 많음
    print(td.get_text(strip=True))  # 공백 없애고 출력
    names.append(td.get_text(strip=True)) # 배열에 추가

prices = []
for td in tds:
    if "class" in td.attrs:#td 어트리뷰트가 있으면. # 방어코드
        if "sale" in td.attrs["class"]:#class에 sale가 있으면
            prices.append(td.get_text(strip=True))

print(names)
print(prices)
