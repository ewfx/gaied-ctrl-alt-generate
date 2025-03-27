from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.base import router as base_router
from routes.text import router as text_router
from routes.file import router as file_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(base_router)
app.include_router(text_router)
app.include_router(file_router)

