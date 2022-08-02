# request 라이브러리 소개
import requests as req

#res = req.get("https://www.naver.com/")
#print(res.text)

###
# GET : 요청, 값 가져오는 역할
# POST : 생성, 액션
# PUT : 수정, 덮어쓰기
# DELETE : 삭제

res = req.get("https://api.ipify.org/")
print(res.status_code) # 상태 값 200
print(res.text) # 값
print(res.request.method) # 메소드
print(res.request.headers) # 헤더
print(res.elapsed) # 시간
print(res.raw) # text의 bit 값




