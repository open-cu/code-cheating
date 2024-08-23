from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    user_id: UUID
    name: str
    level: int
    average_coefficient: float
    maximum_coefficient: float
    median_coefficient: float


class Coefficient(BaseModel):
    homework_id: int
    coefficient: float


class TableItem(BaseModel):
    name: str
    coefficients: list[Coefficient]


class TableUser(BaseModel):
    name: str
    table: list[TableItem]
