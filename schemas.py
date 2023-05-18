from pydantic import BaseModel, Field, validator, root_validator, EmailStr, BaseConfig
from pydantic.types import Decimal
import ujson

categories = ['Coffee', 'Tea']


class Base(BaseModel):
    class Config(BaseConfig):
        json_dumps = ujson.dumps
        json_loads = ujson.loads


class User(Base):
    username: str = Field(min_length=4, max_length=64)
    age: int = Field(ge=18)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)

    @root_validator()
    def validator(cls, values: dict) -> dict:
        if values.get('username').lower() in values.get('password').lower():
            raise ValueError('password has not constraint username')

        return values


class Product(Base):
    title: str
    price: Decimal = Field(max_digits=8, decimal_places=2)


class Category(Base):
    name: str

    # products: list[Product] = Field(default=None)
    # parent_category: "Category" = Field(default=None)

    @validator('name')
    def validate_name(cls, value: str) -> str:
        global categories
        if value.title() in categories:
            raise ValueError('category name is not unique')

        categories.append(value.title())
        return value.title()
