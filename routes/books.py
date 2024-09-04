import json

from fastapi import APIRouter, Path, Query, HTTPException, status
from schemas.books import BaseBook, Book
# from utils.logger import logger

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


@router.get('/search')
def get_books_by_title(title: str = '', page: int = Query(default=1, ge=1), per_page: int = Query(default=1, ge=1)) -> list[Book]:
    """Get books by title, page and per page"""

    # connect to fake database
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # search book by title
    books = []

    for book in data['books']:
        if title.lower() in book['title'].lower():
            books.append(Book(**book))

    # filter by page & per page
    limit = page * per_page
    offset = limit - per_page

    return books[offset:limit]


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


@router.post('/')
def create_book(book: BaseBook) -> Book:
    """Create a new book"""

    # connect to fake database
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    created_book = None

    # get the last book id
    if data['books']:
        bookd_id = data['books'][-1]['id'] + 1

        created_book = Book(id=bookd_id, **book.model_dump())

        data['books'].append(created_book.model_dump())

    try:
        with open('database/db.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    if created_book:
        return created_book
    else:
        raise HTTPException(status_code=500, detail={
                            'message': 'Server internal error'})


@router.put('/{id}')
def update_book_by_id(book: BaseBook, id: int = Path()):
    """Update book by id"""

    # connect to fake database
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # search book by id
    for i in range(len(data['books'])):
        curr_book = data['books'][i]

        if curr_book['id'] == id:
            # update book
            curr_book['title'] = book.title
            curr_book['author'] = book.author
            curr_book['year'] = book.year

            # set updated book
            data['books'][i] = curr_book

            with open('database/db.json', 'w') as file:
                json.dump(data, file, indent=4)

            return {'message': 'Book updated'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail={'message': 'Book not found'})


@router.delete('/{id}')
def delete_book_by_id(id: int = Path()):
    """Delete book by id"""

    # connect to fake database
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    for i in range(len(data['books'])):
        book = data['books'][i]

        if book['id'] == id:
            del data['books'][i]

            with open('database/db.json', 'w') as file:
                json.dump(data, file, indent=4)

            return {'message': 'Book deleted'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail={'message': 'Book not found'})
