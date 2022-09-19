from typing import List

from fastapi import FastAPI, Query, Path, Cookie, Header
from pydantic import BaseModel, Field

import uvicorn
app = FastAPI()


@app.get("/cookie")
def get_cookies(ga: str = Cookie(None)):
    return {"ga": ga}
# http :8000/cookie Cookie:ga=GA12.3.4

@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}
# http :8000/header X-Token:some.secret.token

# app 실행
if __name__ == "__main__":
    uvicorn.run("08:app", reload=True) # 파일명으로 수정 