from fastapi import APIRouter
import asyncio
from package.test import ping

testroute = APIRouter()


@testroute.get('/pingtest')
def pingtest():
    try:
       return asyncio.run(ping.fetch("https://pokeapi.co/api/v2/pokemon/151"))      
    except BaseException as error:
            return error
