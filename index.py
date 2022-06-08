import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from router.test import testroute

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(testroute, prefix="/testroute")


@app.get("/")
async def ping():
    return "Welcome to Andromeda Test Application"

uvicorn.run(app, host='0.0.0.0', port=5001)
