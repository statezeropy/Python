# https://finance.naver.com/marketindex/?tabSel=exchange#tab_section
# 페이지 우클릭 -> 소스 보기 -> 찾기 '미국 USD'
import requests as req

res = req.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

html = res.text
# find는 값 존재 유무 확인 용도만
#pos = html.find('미국 USD')

# split이 그나마 쓰임
pos = html.split('<span class="value">')[1].split('</span>')[0]
print(pos)