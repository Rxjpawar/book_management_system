from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from config import Config
from typing import AsyncGenerator


# created engine for database connection
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)

# going to help us to create a connection to the db and
# going to have connection established as long as application is running
async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)


# this is our session dependency on which other code is going to rely
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with Session() as session:
        yield session
