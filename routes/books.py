from fastapi import APIRouter, Path, HTTPException, status

import json

from schemas.books import Book

router = APIRouter(prefix='/books', tags=['books'])


@router.get('/')
def get_books() -> list[Book]:
    """Get all books"""
    # connect to fake database
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return data['books']


@router.get('/{id}')
def get_book_by_id(id: int = Path()) -> Book:
    """Get book by id"""
    # connect to fake database
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # search book by id
    for book in data['books']:
        if book['id'] == id:
            return Book(**book)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
