from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid


# This model is for creating table in database
class Books(SQLModel, table=True):
    __tablename__ = "books"
    
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=False
    )
    title: str
    publisher: str
    page_count: int
    language: str
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False
    )

    class Config:
        from_attributes = True

    def __repr__(self):
        return f"<Book {self.title}>"
