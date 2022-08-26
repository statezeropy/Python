# https://imgur.com/
# 이미지 업로드
import requests as req


url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7"

# 이미지 불러오기
#f = open("image.png", "rb")
#img = f.read()
#f.close()

# 이미지 불러오기 - 위의 방법보다 편하게
with open("C:\python\crawling_static\Chapter01\image.png", "rb") as f: #r :read, b: binary
    img = f.read()


print(len(img)) # 이미지 읽기


res = req.post(url, files={
    "image": img,
    "type": "file",
    "name": "img"
})
print(res.status_code)
print(res.text)


# 링크 가져오기
# 개발자 도구 - 콘솔 - 데이터 영역
link = res.josn()["data"]["link"]
print(link)


# Client_id
# 개발자도구에서 ctl + f 
# client_id 검색