class Publication: #this is a where the objects of the class are defined.
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages

    def set_title(self, title): 
        self.title = title

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages

    def display_info(self): #This displays the information of the publication.
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.number_of_pages}")

class Book(Publication): #This is a child class that inherits from the parent class Publication. It overrides the display_info method to provide a specific implementation for books.
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author, number_of_pages)
        self.number_of_pages = 0
        self.number_of_pages = number_of_pages #This is where the number of pages is set for the book. It checks if the number of pages is positive and sets it accordingly.

    def get_number_of_pages(self): 
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages

    def display_info(self):
        super().display_info()
     


class Magazine(Publication): #This is a child class that inherits from the parent class Publication. It overrides the display_info method to provide a specific implementation for the magazines.
    def __init__(self, title, author, issue_number): 
        super().__init__(title, author, issue_number)
        self.issue_number = issue_number

    def set_issue_number(self, issue_number): #This is where the issue number is set for the magazine. It checks if the issue number is positive and sets it accordingly.
        if issue_number < 0:
            print("Issue numbers must be postive. Please enter a positive integer.")
        else:
            self.issue_number = issue_number

    def get_issue_number(self):
        return self.issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


#This is where the objects of the classes are created and their methods are called to display their information.
pub1 = Publication("Publication", "Basta Libro", 414)
book1 = Book("The Hunger Games", "Suzanne Collins", 374)
magazine1 = Magazine("National Geographic", "Various Authors", 123)

print("\nPublication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-5)
print(book1.get_number_of_pages())
book1.display_info()

print("\nMagazine Information:")
magazine1.display_info()
print(magazine1.get_issue_number())


#Made with the help of IntelliSense. (2026, November 5).