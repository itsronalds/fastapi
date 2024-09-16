# FastAPI

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

Entre los métodos HTTP más utilizados se encuentran:

| **Método** |             **Explicación**             |
| :--------- | :-------------------------------------: |
| GET        |  Utilizado para la extración de datos   |
| POST       | Utilizado para enviar datos al servidor |
| PUT        |  Utilizado para actualizar un recurso   |
| DELETE     |    Utilizado para borrar un recurso     |

# Parámetros de URL

Los parametros de URL se utilizan para enviar ciertos datos a través de la URL para encontrar recursos basandonos en la localización.

Por ejemplo: Quiero encontrar un libro con el **ID 3**, para esto necesito utilizar el método **GET** y enviarle el ID por URL quedando de la siguiente manera:

```$
http://localhost:8000/api/books/3 # siendo este último el ID del libro que quiero obtener
```
