# FastAPI Tutorial

# Create a FastAPI Project

## Requirements

- Python v3.9+

## Create Virtual Environment

```$
# Windows
python -m venv <venv name>
```

## Activate/Deactivate Virtual Environment

In the project root:

```$
# Windows (Activate)
venv\scripts\activate

# Windows (Deactivate)
venv\scripts\deactivate
```

## Install Dependencies

```$
pip install -r requirements.txt
```

## Run the Project

```$
# Using the development server Uvicorn
uvicorn app:app --reload

# Using the FastAPI development mode
fastapi dev app.py

# Using the FastAPI production mode
fastapi run app.py
```

# HTTP Methods

Among the most commonly used HTTP methods are:

| **Method** |         **Explanation**         |
| :--------- | :-----------------------------: |
| GET        |      Used to retrieve data      |
| POST       | Used to send data to the server |
| PUT        |    Used to update a resource    |
| DELETE     |    Used to delete a resource    |

## Get Method

Used to obtain information from a REST API, we send a request to our application and it responds by delivering the requested resources.

For the **GET** method, there are two additional ways to extract data, which are:

- URL Parameters
- Query Parameters

We will see these below.

### URL Parameters

URL parameters are used to send certain data through the URL to locate resources based on their location.

For example: I want to find a book with **ID 3**, for this I need to use the **GET** method and send the ID via URL as follows:

```$
[GET] http://localhost:8000/api/books/3 # with the last part being the ID of the book I want to obtain
```

### Query Parameters

Query parameters are a way to send multiple dynamic values via URL to perform more specific queries using the GET method.

For example: Imagine we want to capture a book with the initials of The Lord Of The Rings, we would do the following:

## POST Method

Used to create a resource on the server, typically in our database. We send a body to our REST API, which usually looks like this:

```$
# JSON Format
{
    "technology": "FastAPI",
    "year": 2018
}
```

The server takes the data we sent, verifies it, and if it meets the validation standards, it is registered in a **database**.
