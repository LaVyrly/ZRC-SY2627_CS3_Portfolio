class Publication:

  def __init__(self, title, author):
    self._title = title
    self._author = author

  
  def get_title(self):
    return self._title

  def set_title(self, title):
    self._title = title

  def get_author(self):
    return self._author

  def set_author(self, author):
    self._author = author

  def display_info(self):
    print(f"Title: {self._title}")
    print(f"Author: {self._author}")



class Book(Publication):

  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author)
    self.set_number_of_pages(number_of_pages)

  def get_number_of_pages(self):
    return self._number_of_pages

  def set_number_of_pages(self, number_of_pages):
    if number_of_pages <= 0:
      print("Number of pages must be positive.")
    else:
      self._number_of_pages = number_of_pages

  def display_info(self):
    super().display_info()
    print(f"Number of pages: {self._number_of_pages}")



class Magazine(Publication):

  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    self.set_issue_number(issue_number)

  def get_issue_number(self):
    return self._issue_number

  def set_issue_number(self, issue_number):
    if issue_number <= 0:
      print("Issue number must be positive.")
    else:
      self._issue_number = issue_number

  def display_info(self):
    super().display_info()
    print(f"Issue number: {self._issue_number}")



pub1 = Publication(
    "Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H."
)
pub2 = Publication("Artificial Intelligence Basics", "John McCarthy")


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Clean Code", "Robert C. Martin", 464)


mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Time Inc.", 50)



print("Publication Information:")
pub1.display_info()
print("-" * 30)
pub2.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  
book1.display_info()
print(f"Retrieved Pages: {book1.get_number_of_pages()}")

print("-" * 30)
book2.display_info()
print(f"Retrieved Pages: {book2.get_number_of_pages()}")

print("\nMagazine Information:")
mag1.display_info()
print(f"Retrieved Issue Number: {mag1.get_issue_number()}")

print("-" * 30)
mag2.display_info()
print(f"Retrieved Issue Number: {mag2.get_issue_number()}")