from fastapi import APIRouter
import requests

routes = APIRouter()

# public api
@routes.get('/public')
def public():
    try:
        result = requests.get('https://catfact.ninja/fact')
        return f"""{result.text}"""
    except BaseException as error:
        return error

# private api
@routes.get('/private')
def private():
    try:
        result = requests.get('http://localhost:8080')
        return f"""{result.text}"""
    except BaseException as error:
        return error