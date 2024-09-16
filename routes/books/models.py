import json

# schemas
from schemas.books import Book

# utils
from utils.logger import logger


def get_all_books() -> list[Book] | None:
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)

        # convert dict to Book class
        return [Book(**book) for book in data['books']]
    except Exception as e:
        logger.debug(msg=str(e))
        return None


def get_book_by_id(id: int):
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)

        books = data['books']
        books_len = len(books)

        for i in range(books_len):
            book = books[i]

            if book['id'] == id:
                return book

        return False
    except Exception as e:
        logger.debug(msg=str(e))
        return None


def save_all_books(books: list[dict]) -> bool | None:
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)

        data['books'] = books

        with open('database/db.json', 'w') as file:
            json.dump(data, file, indent=4)

        return True
    except Exception as e:
        logger.debug(msg=str(e))
        return None


def save_book(book: dict) -> bool | None:
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)

        books = data['books']
        books_len = len(books)

        for i in range(books_len):
            curr_book = books[i]

            if curr_book['id'] == book['id']:
                books[i] = book

        data['books'] = books

        with open('database/db.json', 'w') as file:
            json.dump(data, file, indent=4)

        return True
    except Exception as e:
        logger.debug(msg=str(e))
        return None


def delete_book_by_id(id: int):
    try:
        with open('database/db.json', 'r') as file:
            data = json.load(file)

        books = data['books']
        books_len = len(books)

        for i in range(books_len):
            book = books[i]

            if book['id'] == id:
                del books[i]

        data['books'] = books

        with open('database/db.json', 'w') as file:
            json.dump(data, file, indent=4)

        return True
    except Exception as e:
        logger.debug(msg=str(e))
        return None
