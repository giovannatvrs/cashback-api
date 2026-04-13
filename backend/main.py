from fastapi import FastAPI
from backend import models
from backend.database import engine
from backend.routers import router


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


app.include_router(router)


@app.get("/")
def root():
    return "Hello, World"