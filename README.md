# books-library

### The main idea of the Books-Library system is to provide a simple, object-oriented way to manage books and members within a library. It allows for adding and removing books and members, tracking which books are borrowed by which members, and ensuring that members can only borrow books if their membership is valid

### In the implementation of the Library class, we've applied several Object-Oriented Programming (OOP) principles:

1. Singleton Pattern: By implementing the __new__ method, you ensure that there is only one instance of the Library class throughout the application. This promotes resource efficiency and ensures that the state of the library (such as its collection of books and members) is consistent across all parts of the application.

2. Encapsulation: The Library class encapsulates the functionality related to managing books and members. It provides methods (add_book, remove_book, add_member, remove_member, list_books, list_members) for interacting with its internal state (books and members), abstracting away the implementation details from the user of the class.

3. Abstraction: The Library class abstracts the concept of a library, providing a high-level interface for interacting with its resources (books and members). Users of the class do not need to know the internal details of how books and members are stored or managed; they can simply use the provided methods to perform operations on them..