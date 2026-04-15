from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import models
from backend.database import engine
from backend.routers import router


app = FastAPI()

origins = ["http://localhost:5500", 
           "http://127.0.0.1:5500",
           "http://0.0.0.0:5500",
           "cashback-api-production-43b9.up.railway.app",
           "https://giovannatvrs.github.io"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

models.Base.metadata.create_all(bind=engine)


app.include_router(router)


@app.get("/")
def root():
    return "Hello, World"