from fastapi import APIRouter
import asyncio
from package.test import ping
from config.config import get_env

testroute = APIRouter()

# self ping test
@testroute.get('/selfpingtest')
def selfpingtest():
    try:
        env = get_env()
        pingtest = ping.fetch(env["svc"])
        return asyncio.run(pingtest)
    except BaseException as error:
        return error

# ping test
@testroute.get('/pingtest1')
def pingtest1():
    try:
        return "server 1"
    except BaseException as error:
        return error

# ping test
@testroute.get('/pingtest2')
def pingtest2():
    try:
        return "server 2"
    except BaseException as error:
        return error