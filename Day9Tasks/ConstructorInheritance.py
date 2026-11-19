"""16. Library Management System (Constructor & Inheritance)
A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information"""

class Book:

  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn

  def display_details(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"ISBN: {self.isbn}")


# Derived class inheriting from Book
class EBook(Book):

  def __init__(self, title, author, isbn, file_size):
    # Call the parent class constructor using super()
    super().__init__(title, author, isbn)
    self.file_size = file_size  # Additional attribute for EBook

  def display_details(self):
    # Reuse the parent display method and add file size
    super().display_details()
    print(f"File Size: {self.file_size} MB")


# --- Example Usage ---
if __name__ == "__main__":
  print("--- Physical Book ---")
  book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
  book1.display_details()

  print("\n--- Digital Book (E-Book) ---")
  ebook1 = EBook("1984", "George Orwell", "978-0451524935", 2.5)
  ebook1.display_details()  
