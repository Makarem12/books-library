from .member import Member
from .book import Book
from datetime import date
from .person import Person

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.members = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        self.members = [member for member in self.members if member.member_id != member_id]

    def list_books(self):
        return '\n'.join([book.get_details() for book in self.books])

    def list_members(self):
        return '\n'.join([member.get_details() for member in self.members])

# Additional test cases and actions
if __name__ == "__main__":
    # Create a library instance
    my_library = Library()

    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "2345678901")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)

    # Create a member with an expired membership for testing
    expired_member = Member("Jane Doe", 40, date(2023, 12, 31))  # Assume the current date is past this date

    # Member tries to borrow a book with expired membership
    try:
        expired_member.borrow_book(book1)
    except Exception as e:
        print(e)  # Expecting to see "Membership has expired"

    # Create a valid member
    valid_member = Member("John Doe", 30, date(2024, 12, 31))

    # Member borrows a book
    valid_member.borrow_book(book1)

    # List borrowed books
    print(valid_member.list_borrowed_books())  # Expecting to see details of book1

    # Try to return a book not borrowed by the member
    try:
        valid_member.return_book(book2)
    except Exception as e:
        print(e)  # Expecting to see "Book not borrowed by this member"

    # Return the book
    valid_member.return_book(book1)

    # List borrowed books again
    print(valid_member.list_borrowed_books())  # Expecting to see "No Books Borrowed"

    # Check membership validity
    print(valid_member.is_membership_valid())  # Expecting to see True (assuming the current date is before Dec 31, 2024)

    # List books in the library
    print("List of books in the library:")
    print(my_library.list_books())

    # List members in the library
    my_library.add_member(expired_member)
    my_library.add_member(valid_member)
    print("List of members in the library:")
    print(my_library.list_members())
