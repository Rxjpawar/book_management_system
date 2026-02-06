from sqlmodel import SQLModel
import uuid
from datetime import datetime
from typing import Optional


# Response schema - what gets returned to users (Read model)
class BookResponse(SQLModel):
    uid: uuid.UUID
    title: str
    publisher: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


# Create schema - what users send when creating a book
class BookCreateModel(SQLModel):
    title: str
    publisher: str
    page_count: int
    language: str


# Update schema - all fields optional for partial updates
class BookUpdateModel(SQLModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
