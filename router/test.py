from fastapi import APIRouter
import asyncio
from package.test import ping
from config.config import get_env

testroute = APIRouter()

# ping test
@testroute.get('/pingtest')
def pingtest():
    try:
        env = get_env()
        pingtest = ping.fetch(env["svc"])
        return asyncio.run(pingtest)
    except BaseException as error:
        return error
