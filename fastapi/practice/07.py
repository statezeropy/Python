from typing import List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field

import uvicorn
app = FastAPI()

# DB 대신 임시로 사용
inventory = (
    {
        "id": 1,
        "user_id": 1,
        "name": "레전드포션",
        "price": 2500.0,
        "amount": 100,
    },
    {
        "id": 2,
        "user_id": 1,
        "name": "포션",
        "price": 300.0,
        "amount": 50,
    },
)
class Item(BaseModel):
    name: str
    price: float
    amount: int = 0

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    price: float = Field(None, ge=0)
    amount: int = Field(
        default=1,
        gt=0,
        le=100,
        title="수량",
        description="아이템 갯수. 1~100 개 까지 소지 가능",
    ) 

@app.get("/users/{user_id}/inventory", response_model=List[Item])
def get_item(
    user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
    name: str = Query(None, min_length=1, max_length=2, title="아이템 이름"),
):
    user_items = []
    for item in inventory:
        if item["user_id"] == user_id:
            user_items.append(item)

    response = []
    for item in user_items:
        if name is None:
            response = user_items
            break
        if item["name"] == name:
            response.append(item)

    return response
# http ':8000/users/1/inventory?name=포션'



@app.post("/users/{user_id}/item")
def create_item(item: Item):
    return item



# app 실행
if __name__ == "__main__":
    uvicorn.run("07:app", reload=True) # 파일명으로 수정 