from fastapi import FastAPI

# import the routes
from routes.books.books import router as books_router
from routes.home.home import router as home_router


app = FastAPI()


# include the routes
app.include_router(books_router, prefix="/api")
app.include_router(home_router, prefix='/api')
