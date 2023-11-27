from fastapi import FastAPI
from .router import get_route


app = FastAPI()
app.include_router(get_route())
