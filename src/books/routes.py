from fastapi import APIRouter, Depends, status
from src.books.schemas import BookUpdateModel, BookCreateModel, BookResponse
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.books.services import BookService

book_router = APIRouter()
book_service = BookService()


# view all books
@book_router.get("/", response_model=list[BookResponse])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return [BookResponse.model_validate(book) for book in books]


# view a book by id
@book_router.get("/{book_uid}", response_model=BookResponse)
async def get_book_by_id(book_uid: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book_by_id(book_uid, session)
    
    if book:
        return BookResponse.model_validate(book)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with uid '{book_uid}' not found"
        )


# create new book
@book_router.post("/create_book", status_code=status.HTTP_201_CREATED, response_model=BookResponse)
async def create_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data, session)
    return BookResponse.model_validate(new_book)


# edit a book by id
@book_router.patch("/{book_uid}", response_model=BookResponse)  # Changed to PATCH for partial updates
async def update_book(book_uid: str,book_update_data: BookUpdateModel,session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book:
        return BookResponse.model_validate(updated_book)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with uid '{book_uid}' not found"
        )

# delete a book by id
@book_router.delete("/{book_uid}", status_code=status.HTTP_200_OK)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    deleted = await book_service.delete_book(book_uid, session)
    
    if deleted:
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with uid '{book_uid}' not found"
        )
