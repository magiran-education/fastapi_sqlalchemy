from enum import Enum
from pydantic import BaseModel, Field


class TradeInput(BaseModel):
    id: int
    side: Enum("TradeSideEnum", (("BUY", "BUY"), ("SELL", "SELL")))  # значение BUY или SELL
    price: float = Field(ge=0)  # значение >= 0


class UserOutput(BaseModel):
    id: int
    name: str
