from .person import Person
from datetime import date

class Member(Person):
    def __init__(self, name, age, expiry_date):
        super().__init__(name, age)
        self.expiry_date = expiry_date
        self.borrowed_books = []

    def get_details(self):
        return f"{super().get_details()}, Expiry_date: {self.expiry_date}"

    def borrow_book(self, book):
        if self.is_membership_valid():
            self.borrowed_books.append(book)
        else:
            raise Exception("Membership has expired")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            raise Exception("Book not borrowed by this member")

    def list_borrowed_books(self):
        if self.borrowed_books:
            return '\n'.join([book.get_details() for book in self.borrowed_books])
        else:
            return "No Books Borrowed"

    def is_membership_valid(self):
        return date.today() <= self.expiry_date
