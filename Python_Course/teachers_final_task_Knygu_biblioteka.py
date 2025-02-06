### - - -       -- - -  Detytojo kodas - - - - - - -

import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True
        self.borrow_date = None

    def __str__(self):
        status = "Prieinama" if self.available else f"Pasiskolinta iki {self.due_date()}"
        return f"{self.title}, autorius: {self.author}, išleista: {self.year}, Statusas: {status}"

    def is_classic(self):
        current_year = datetime.datetime.today().year
        return current_year - self.year > 50

    def due_date(self):
        if self.borrow_date:
            return (self.borrow_date + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
        return None

    def is_overdue(self):
        if self.borrow_date:
            return datetime.datetime.today() > self.borrow_date + datetime.timedelta(days=14)
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Knyga pridėta sėkmingai!")

    def display_books(self):
        if not self.books:
            print("Biblioteka tuščia.")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower() and book.available:
                    book.available = False
                    book.borrow_date = datetime.datetime.today()
                    print(f"Jūs sėkmingai pasiskolinote knygą: {book.title}")
                    return
            raise ValueError("Knyga nerasta arba ji jau pasiskolinta.")
        except ValueError as e:
            print(e)

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                book.borrow_date = None
                print(f"Jūs sėkmingai grąžinote knygą: {book.title}")
                return
        print("Knyga nerasta arba ji nebuvo pasiskolinta.")

    def filter_books(self, *args, **kwargs):
        filtered_books = self.books

        for key, value in kwargs.items():
            if key == "title":
                filtered_books = [book for book in filtered_books if book.title == value]
            elif key == "author":
                filtered_books = [book for book in filtered_books if book.author == value]
            elif key == "year":
                filtered_books = [book for book in filtered_books if book.year == value]

        for book in filtered_books:
            print(book)

library = Library()

while True:
    print("""
1. Pridėti naują knygą
2. Peržiūrėti bibliotekos knygas
3. Pasiskolinti knygą
4. Grąžinti knygą
5. Filtruoti knygas
6. Išeiti
    """)

    choice = input("Pasirinkite veiksmą: ")

    if choice == "1":
        title = input("Įveskite knygos pavadinimą: ")
        author = input("Įveskite autorių: ")
        try:
            year = int(input("Įveskite išleidimo metus: "))
            book = Book(title, author, year)
            library.add_book(book)
        except ValueError:
            print("Įveskite tinkamą metų formatą!")
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        title = input("Įveskite knygos pavadinimą, kurią norite pasiskolinti: ")
        library.borrow_book(title)
    elif choice == "4":
        title = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
        library.return_book(title)
    elif choice == "5":
        key = input("Filtruoti pagal (title/author/year): ")
        value = input("Įveskite reikšmę: ")
        if key in ["title", "author"]:
            library.filter_books(**{key: value})
        elif key == "year":
            try:
                year = int(value)
                library.filter_books(year=year)
            except ValueError:
                print("Metai turi būti skaičius.")
        else:
            print("Netinkamas filtravimo pasirinkimas.")
    elif choice == "6":
        print("Programa baigiama.")
        break
    else:
        print("Netinkamas pasirinkimas. Bandykite dar kartą.")