from pydantic import BaseModel, Field


class BaseBook(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=45)
    year: int


class Book(BaseBook):
    id: int


Books = list[Book]
