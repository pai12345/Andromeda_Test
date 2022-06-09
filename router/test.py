from fastapi import APIRouter
import asyncio
from package.test import ping
# from config.config import get_env

testroute = APIRouter()

# self ping test
@testroute.get('/selfpingtest')
def selfpingtest():
    try:
        # env = get_env()
        pingtest = ping.fetch("https://pokeapi.co/api/v2/pokemon/151")
        result = asyncio.run(pingtest)
        print(result)
        return f"""selfping-{result}"""
    except BaseException as error:
        return error

# ping test
@testroute.get('/pingtest')
def pingtest1():
    try:
        return "server 1"
    except BaseException as error:
        return error