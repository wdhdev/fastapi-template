from fastapi import FastAPI

from router import router as router

app = FastAPI()

app.include_router(router)