from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from apps.first_app.obj_models import TradeInput, UserOutput


first_app_router = APIRouter()


TRADES = [
    {"id": 1, "side": "buy", "price": 123},
    {"id": 2, "side": "sell", "price": 456},
    {"id": 3, "side": "buy", "price": 789},
]
USERS = [
    {"id": 1, "name": "Andrey"},
    {"id": 2, "name": "Nina"},
]


# первый эндпоинт
@first_app_router.get("/first_endpoint")
def hello():
    return "Hello, World"


# переменная в URL. Например, http://127.0.0.1:8000/users/3
@first_app_router.get("/users/{user_id}")
def get_user(user_id: int):
    return user_id


# параметры в URL со значениями по умолчанию. Например, http://127.0.0.1:8000/trades?limit=2&offset=1
@first_app_router.get("/trades")
def get_trades(limit: int = 10, offset: int = 0):
    return TRADES[offset:][:limit]


# в теле POST передаём JSON с валидацией по модели Pydantic (переменная trades)
# при возврате fake_trades, объект Pydantic автоматически преобразуется в JSON
@first_app_router.post("/add_trades")
def add_trades(trades: list[TradeInput]):
    fake_trades = [{"id": 1, "side": "BUY", "price": 123}]
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


# валидация возвращаемого объекта (response_model=User)
@first_app_router.get("/users/check_output_model/{user_id}", response_model=UserOutput)
def get_user(user_id: int):
    user = tuple(filter(lambda user: user.get("id") == user_id, USERS))
    if len(user) > 0:
        return user[0]
    else:
        raise HTTPException(status_code=404, detail="User not found")


# добавление набора параметров в эндпоинт
async def common_params(offset: int = 0, limit: int = 10):
    return {"offset": offset, "limit": limit}


@first_app_router.get("/trades2")
async def get_trades_2(commons: dict = Depends(common_params)):
    return commons