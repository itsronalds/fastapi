from pydantic import BaseModel, Field


class BaseBook(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=45)
    year: int

    model_config = {
        'json_schema_extra': {
            'example': [
                {
                    'title': 'The Lord Of Ring',
                    'author': 'JR',
                    'year': 2000
                }
            ]
        }
    }


class Book(BaseBook):
    id: int


Books = list[Book]
