# books-library

### The main idea of the Books-Library system is to provide a simple, object-oriented way to manage books and members within a library. It allows for adding and removing books and members, tracking which books are borrowed by which members, and ensuring that members can only borrow books if their membership is valid

### In the implementation of the Library class, we've applied several Object-Oriented Programming (OOP) principles:

1. Singleton Pattern: By implementing the __new__ method, you ensure that there is only one instance of the Library class throughout the application. This promotes resource efficiency and ensures that the state of the library (such as its collection of books and members) is consistent across all parts of the application.

2. Encapsulation: The Library class encapsulates the functionality related to managing books and members. It provides methods (add_book, remove_book, add_member, remove_member, list_books, list_members) for interacting with its internal state (books and members), abstracting away the implementation details from the user of the class.

3. Abstraction: The Library class abstracts the concept of a library, providing a high-level interface for interacting with its resources (books and members). Users of the class do not need to know the internal details of how books and members are stored or managed; they can simply use the provided methods to perform operations on them.

4. inheritance: inheritance is utilized through the Member class, which inherits from the Person class

## Testing
* The project includes unit tests to ensure that all functionality works as expected.

## Running the project
To run the project, follow these steps:

1. Clone the Repository: 
Clone the repository to your local machine using the following command:
python 
git clone <repository_url>

Replace <repository_url> with the URL of your GitHub repository.

2. Navigate to the Project Directory: 
Navigate to the root directory of the cloned repository in your terminal or command prompt.

3. Activate the Virtual Environment: 
If you're using a virtual environment, activate it by running the appropriate activation command. For example, if you're using venv, activate it with:
python 
source .venv/bin/activate


4. Run the Tests: 
Before running the project, it's a good practice to run the tests to ensure everything is working correctly. Use pytest to run the tests:
pytest

This command will automatically discover and run all the test cases in your project