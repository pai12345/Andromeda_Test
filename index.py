import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from router.test import routes

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(routes, prefix="/api")

# Welcome Page
@app.get("/")
async def call():
    return "Welcome to Andromeda Test Application"

uvicorn.run(app, host='0.0.0.0', port=9000)
