from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum


TRADES = [
    {"id": 1, "side": "buy", "price": 123},
    {"id": 2, "side": "sell", "price": 456},
    {"id": 3, "side": "buy", "price": 789},
]
USERS = [
    {"id": 1, "name": "Andrey"},
    {"id": 2, "name": "Nina"},
]


app = FastAPI(
    title="Trading App"
)


# первый эндпоинт
@app.get("/first_endpoint")
def hello():
    return "Hello, World"


# переменная в URL. Например, http://127.0.0.1:8000/users/3
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_id


# параметры в URL. Например, http://127.0.0.1:8000/trades?limit=2&offset=1
@app.get("/trades")
def get_trades(limit: int, offset: int):
    return TRADES[offset:][:limit]


# в теле POST передаём JSON с валидацией по модели Pydantic (переменная trades)
# при возврате fake_trades, объект Pydantic автоматически преобразуется в JSON
class Trade(BaseModel):
    id: int
    side: Enum("TradeSideEnum", [("BUY", "BUY"), ("SELL", "SELL")])  # значение BUY или SELL
    price: float = Field(ge=0)  # значение >= 0


@app.post("/add_trades")
def add_trades(trades: list[Trade]):
    fake_trades = [{"id": 1, "side": "BUY", "price": 123}]
    fake_trades.extend(trades)
    print(fake_trades)
    return {"status": 200, "data": fake_trades}


# валидация возвращаемого объекта (response_model=User)
class User(BaseModel):
    id: int
    name: str


@app.get("/users2/{user_id}", response_model=User)
def get_user(user_id: int):
    user = tuple(filter(lambda user: user.get("id") == user_id, USERS))
    if len(user) > 0:
        return user[0]
    else:
        raise HTTPException(status_code=404, detail="User not found")
