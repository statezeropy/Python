
from fastapi import FastAPI
from typing import Optional
import uvicorn

from pydantic import BaseModel, HttpUrl, EmailStr # EmailStr 이메일 검증

app = FastAPI()

#### 요청 본문

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None

@app.post("/users") # get 아닌 post
def create_user(user: User):
    return user


# app 실행
if __name__ == "__main__":
    uvicorn.run("05:app", reload=True) # 파일명으로 수정 