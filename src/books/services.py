from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from .models import Books
from datetime import datetime


class BookService:
    # session is the object which is going to help perform crud or any transaction on the database
    # allows us to execute any sql query

    # view all books
    async def get_all_books(self, session: AsyncSession):
        statement = select(Books).order_by(desc(Books.created_at))
        result = await session.execute(statement)
        books = result.scalars().all()
        return books

    # view book by id
    async def get_book_by_id(self, book_uid: str, session: AsyncSession):
        statement = select(Books).where(Books.uid == book_uid)
        result = await session.execute(statement)
        book = result.scalars().first()
        return book if book is not None else None

    # create a book
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Books(**book_data_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)  # Refresh to get auto-generated fields
        return new_book

    # update existing book
    async def update_book(self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession):
        # FIXED: Added await and session parameter
        book_to_update = await self.get_book_by_id(book_uid, session)
        
        if book_to_update is not None:
            update_data_dict = update_data.model_dump(exclude_unset=True)  # Only update provided fields
            
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
            
            # Manually set updated_at
            book_to_update.updated_at = datetime.now()
            
            session.add(book_to_update)
            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update
        else:
            return None

    # delete book by id
    async def delete_book(self, book_uid: str, session: AsyncSession):
        # FIXED: Added await and session parameter
        book_to_delete = await self.get_book_by_id(book_uid, session)
        
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return True
        else:
            return None

    # create a book
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Books(**book_data_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)  # Refresh to get auto-generated fields
        return new_book

    # update existing book
    async def update_book(self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession):
        # FIXED: Added await and session parameter
        book_to_update = await self.get_book_by_id(book_uid, session)
        
        if book_to_update is not None:
            update_data_dict = update_data.model_dump(exclude_unset=True)  # Only update provided fields
            
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
            
            # Manually set updated_at
            book_to_update.updated_at = datetime.now()
            
            session.add(book_to_update)
            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update
        else:
            return None

    # delete book by id
    async def delete_book(self, book_uid: str, session: AsyncSession):
        # FIXED: Added await and session parameter
        book_to_delete = await self.get_book_by_id(book_uid, session)
        
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return True
        else:
            return None
