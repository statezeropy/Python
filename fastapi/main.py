# python 3.6 이상 필요
# 
# C:\python\fastapi\fastapi\Scripts\activate
# pip install fastapi

# curl 과 비슷한 툴
# pip install httpie
# 콘솔에서  접근
# http localhost:8000


from fastapi import FastAPI
from typing import Optional # 쿼리 매개변수 때 사용 함
from enum import Enum
import uvicorn

app = FastAPI()

""" @app.get("/")
def hello():
    return "Hello, World!"
 """


#### 경로 매개변수 ####
# top -> bottom 이라서 me를 먼저 
@app.get("/users/me") # 여기서 int 힌트 추가할 수 있지만 함수에서 정하는게 더 유용함
#def get_user(user_id): --> 기본값이 문자열
def get_current_user(): # --> int 힌트 
    return {"user_id": 5678}


@app.get("/users/{user_id}") # 여기서 int 힌트 추가할 수 있지만 함수에서 정하는게 더 유용함
#def get_user(user_id): --> 기본값이 문자열
def get_user(user_id: int): # --> int 힌트 
    return {"user_id": user_id}
# http localhost:8000/users/123
# "user_id": "123" --> 문자열

# def get_user(user_id: int): --> int 힌트
# "user_id": 123 --> int


#### 쿼리 매개변수 ####
""" @app.get("/users")
#def get_users(limit: int):
def get_users(limit: Optional[int] = None): # limit를 옵션으로 None를 추가 Optional은 힌트
    return {"limit": limit}
# http localhost:8000/users?limit=1

 """


""" @app.get("/users")
def get_users(is_admin: bool, limit: int = 100): # 추가: q
    return {"is_admin": is_admin, "limit": limit} # 추가: q
# http localhost:8000/users?is_admin=true --> json 문법 : 소문자 true
# http localhost:8000/users?is_admin=True --> python 문법 : 대분자 True
 """


class UserLevel(str, Enum):
    a = "a"
    b = "b"
    c = "c"

@app.get("/users")
#def get_users(grade: UserLevel):
#def get_users(grade: UserLevel = "a"): # --> 하드코딩보다는 아래처럼 편하게
def get_users(grade: UserLevel = UserLevel.a):
    return {"grade": grade}
# http localhost:8000/users?grade=b
# http localhost:8000/users?grade=d --> 오류 발생


# app 실행
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) # 코드 수정하면 실시간으로 리로드 됨

# 실행 후 접속 
# http://127.0.0.1:8000/docs

