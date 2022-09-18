
from fastapi import FastAPI, status #응답코드
from typing import Optional
import uvicorn

from pydantic import BaseModel, HttpUrl, EmailStr # EmailStr 이메일 검증

app = FastAPI()

#### 응답 모델

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None

@app.get("/users/me", response_model=User)
def get_user(user: User):
    return user

@app.post("/users/me", response_model=User)
def get_user(user: User):
    return user

class CreateUser(BaseModel):
    name: str
    password: str
    avatar_url: HttpUrl = "https://naver.com"


class GetUser(BaseModel):
    name: str
    avatar_url: HttpUrl = "https://naver.com"


""" @app.post("/users", response_model=GetUser)
def create_user(user: CreateUser):
    return user
 """
#@app.post("/users", response_model=User, status_code=201) # status_code 추가
@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED) # status id로 추가 가능
def create_user(user: CreateUser):
    return user


# app 실행
if __name__ == "__main__":
    uvicorn.run("06:app", reload=True) # 파일명으로 수정 