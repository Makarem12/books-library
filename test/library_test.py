import pytest
from datetime import date
from books_library.library import Library
from books_library.book import Book
from books_library.member import Member
from books_library.person import Person

@pytest.fixture
def setup_library():
    # Create a library instance
    library = Library()

    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "2345678901")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Create members
    expired_member = Member("Jane Doe", 40, date(2023, 12, 31))  # Assume the current date is past this date
    valid_member = Member("John Doe", 30, date(2024, 12, 31))

    return library, book1, book2, expired_member, valid_member

def test_add_and_list_books(setup_library):
    library, book1, book2, expired_member, valid_member = setup_library
    books_list = library.list_books()
    assert "The Great Gatsby" in books_list
    assert "1984" in books_list

def test_add_and_list_members(setup_library):
    library, book1, book2, expired_member, valid_member = setup_library
    library.add_member(expired_member)
    library.add_member(valid_member)
    members_list = library.list_members()
    assert "Jane Doe" in members_list
    assert "John Doe" in members_list

def test_borrow_book_with_expired_membership(setup_library):
    library, book1, book2, expired_member, valid_member = setup_library
    with pytest.raises(Exception, match="Membership has expired"):
        expired_member.borrow_book(book1)

def test_borrow_and_return_book(setup_library):
    library, book1, book2, expired_member, valid_member = setup_library
    valid_member.borrow_book(book1)
    borrowed_books = valid_member.list_borrowed_books()
    assert "The Great Gatsby" in borrowed_books

    with pytest.raises(Exception, match="Book not borrowed by this member"):
        valid_member.return_book(book2)
    
    valid_member.return_book(book1)
    borrowed_books = valid_member.list_borrowed_books()
    assert "No Books Borrowed" in borrowed_books

def test_is_membership_valid(setup_library):
    library, book1, book2, expired_member, valid_member = setup_library
    assert not expired_member.is_membership_valid()
    assert valid_member.is_membership_valid()
