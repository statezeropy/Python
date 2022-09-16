
from fastapi import FastAPI
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


@app.post("/users", response_model=GetUser)
def create_user(user: CreateUser):
    return user


# app 실행
if __name__ == "__main__":
    uvicorn.run("06:app", reload=True) # 파일명으로 수정 