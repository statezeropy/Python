import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

res = req.get(url)
body = res.text

# 정규표현식 준비
# DOT
r = re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)
print(captures)


# 나라 , 율 조회
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)
print(captures)


# 
for c in captures:
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전되었습니다.")