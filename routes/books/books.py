from fastapi import APIRouter, Path, Query, HTTPException, status

# schemas
from schemas.books import BaseBook, Book

# models
import routes.books.models as book_models

router = APIRouter(prefix='/books', tags=['books'])


@router.get('/all')
def get_books() -> list[Book]:
    """Get all books"""

    # get all books from database
    books = book_models.get_all_books()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    return books


@router.get('/{id}')
def get_book_by_id(id: int = Path()) -> Book:
    """Get book by id"""

    # get books from database
    books = book_models.get_all_books()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    # search book by id
    for book in books:
        if book.id == id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')


@router.get('/')
def get_books_by_query(page: int = Query(default=1, ge=1), per_page: int = Query(default=1, ge=1), title: str = '') -> list[Book]:
    """Get books by title, page and per page"""

    # get books from database
    books = book_models.get_all_books()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    coincidences: list[Book] = []

    for book in books:
        if title.casefold() in str(book.title).casefold():
            coincidences.append(book)

    # filter by page and per page
    limit = page * per_page
    offset = limit - per_page

    return books[offset:limit]


@router.post('/')
def create_book(book: BaseBook) -> Book:
    """Create a new book"""

    # get books from database
    books = book_models.get_all_books()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    created_book = None

    # get the last book id
    if books:
        bookd_id = books[-1].id + 1
        created_book = Book(id=bookd_id, **book.model_dump())
        books.append(created_book)

    result = book_models.save_all_books([book.model_dump() for book in books])

    if not result or not created_book:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
                            'message': 'Error ocurren when creating the book'})

    return created_book


@router.put('/{id}')
def update_book_by_id(book: BaseBook, id: int = Path()):
    """Update book by id"""

    book_by_id = book_models.get_book_by_id(id)

    if not book_by_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'message': 'Book not found'})

    # get books from database
    books = book_models.get_all_books()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    # search book by id
    for i in range(len(books)):
        curr_book = books[i]

        if curr_book.id == id:
            # update book
            curr_book.title = book.title
            curr_book.author = book.author
            curr_book.year = book.year

            # save book in database
            result = book_models.save_book(curr_book.model_dump())

            if not result:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail={'message': 'Error ocurred when updating the book'})

            return {'message': 'Book updated'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail={'message': 'Book not found'})


@router.delete('/{id}')
def delete_book_by_id(id: int = Path()):
    """Delete book by id"""

    book_by_id = book_models.get_book_by_id(id)

    if not book_by_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'message': 'Book not found'})

    # get books from database
    books = book_models.get_all_books()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    result = book_models.delete_book_by_id(id)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'})

    return {'message': 'Book deleted'}
