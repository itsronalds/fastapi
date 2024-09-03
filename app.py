from fastapi import FastAPI

# import the routes
from routes.books import router as books_router


app = FastAPI()


# include the routes
app.include_router(books_router, prefix="/api")
