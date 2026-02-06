from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
version = "v1"

@asynccontextmanager
async def lifespan (app:FastAPI):
    print("server is starting...")
    await init_db()
    yield
    print("server has been stopped...")

app = FastAPI(
    version=version,
    title="Books",
    description="api for books",
    lifespan=lifespan
    )

app.include_router(book_router,prefix=f"/api/{version}/books")
