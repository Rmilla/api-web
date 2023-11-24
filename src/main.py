from fastapi import FastAPI
from router.ouvrage_router import router

app = FastAPI()
app.include_router(router)


