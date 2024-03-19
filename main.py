from fastapi import FastAPI
from src.settings import settings


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": settings}


