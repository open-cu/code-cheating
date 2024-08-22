from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    level: int
    average_coefficient: int
    maximum_coefficient: int
    median_coefficient: int


class Coefficient(BaseModel):
    homework_id: int
    coefficient: int


class TableItem(BaseModel):
    user_id: int
    coefficients: list[Coefficient]


class TableUser(BaseModel):
    user_id: int
    name: str
    table: list[TableItem]
