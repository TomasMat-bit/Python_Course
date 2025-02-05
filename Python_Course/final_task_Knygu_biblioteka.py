# # Galutinė Užduotis: Knygų Bibliotekos Sistema
# # Šioje užduotyje naudosime viską, ką išmokome šiame pokalbyje: klases, metodus, sąrašų
# # valdymą, paveldimumą, datetime modulį, try-except, *args, **kwargs, ir dar daugiau.
# print('- Užduotis: Sukurkite paprastą bibliotekos valdymo sistemą - ')
#
# # • Sukurti dvi klases: Book ir Library.
# # • Naudoti datetime modulį knygų paskolos laikotarpiams valdyti.
# # • Naudoti *args ir **kwargs knygų filtravimui.
# # • Naudoti try-except klaidų valdymui.
#
# # 2. Žingsniai:
print('- - - - - - - - - --  ŽINGSNIS 1: Sukurkite klasę Book- - - - - - - - - - - - - - ')
#
# # ŽINGSNIS 1: Sukurkite klasę Book
# # • Laukai:
# # o title (pavadinimas)
# # o author (autorius)
# # o year (išleidimo metai)
# # o available (ar knyga prieinama) – pagal nutylėjimą True
# # • Metodai:
# # o __str__ – grąžina informaciją apie knygą gražiu formatu.
# # o is_classic() – grąžina True, jei knyga išleista daugiau nei prieš 50 metų.
#
import datetime

class Book:
    def __init__(self, title, author, year, available=True):
        try:
            self.year = int(year)
            if self.year < 0:
                raise ValueError("Metai negali būti neigiami.")
        except ValueError as e:
            print(f"Klaida kuriant knygą: {e}")
            self.year = None
        self.title = title
        self.author = author
        self.available = available
        self.borrowed_date = None

    def __str__(self):
        availability = "Prieinama" if self.available else "Neprieinama"
        return f"Knyga: {self.title}\nAutorius: {self.author}\nIšleidimo metai: {self.year}\nStatusas: {availability}"

    def is_classic(self):
        if self.year is None:
            return False
        current_year = datetime.datetime.now().year
        return current_year - self.year > 50

    def borrow(self):
        self.available = False
        self.borrowed_date = datetime.datetime.now()

    def return_book(self):
        self.available = True
        self.borrowed_date = None

    def due_date(self):
        if self.borrowed_date:
            return self.borrowed_date + datetime.timedelta(days=14)
        else:
            return None

print('- - - - - - - - -ŽINGSNIS 2: Sukurkite klasę Library- - - - - - - - - - - - - - ')
#
# # ŽINGSNIS 2: Sukurkite klasę Library
# # • Laukai:
# # o books (sąrašas, kuriame saugomos knygos)
# # • Metodai:o add_book(book) – prideda naują Book objektą į biblioteką.
# # o display_books() – atvaizduoja visas knygas bibliotekoje.
# # o borrow_book(title) – leidžia pasiskolinti knygą, jei ji prieinama.
# # ▪ Naudoti try-except, kad suvaldytumėte klaidas (pvz., jei knygos
# # nėra).
# # o return_book(title) – leidžia grąžinti knygą.
# # o filter_books(*args, **kwargs) – leidžia filtruoti knygas pagal autorių,
# # metus ar pavadinimą.
# # ▪ Pvz.: filter_books(author="Jonas") arba
# # filter_books(year=2000)
#
class Library:
    def __init__(self):
        self.books = []
        # Pradinės knygos
        self.books.append(Book("1984", "George Orwell", 1949))
        self.books.append(Book("To Kill a Mockingbird", "Harper Lee", 1960))
        self.books.append(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Klaida: Pateikta netinkama knygos reikšmė.")
            return
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("Biblioteka tuščia.")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        try:
            book = next(book for book in self.books if book.title == title)
            if book.available:
                book.borrow()
                print(f"Jūs pasiskolinote knygą: {book.title}")
                print(f"Knygos grąžinimo data: {book.due_date().strftime('%Y-%m-%d')}")
            else:
                print("Knyga jau pasiskolinta.")
        except StopIteration:
            print(f"Knyga su pavadinimu '{title}' nerasta.")

    def return_book(self, title):
        try:
            book = next(book for book in self.books if book.title == title)
            book.return_book()
            print(f"Knyga '{book.title}' buvo grąžinta.")
        except StopIteration:
            print(f"Knyga su pavadinimu '{title}' nerasta.")

    def filter_books(self, *args, **kwargs):
        filtered_books = self.books

        for key, value in kwargs.items():
            if not hasattr(Book, key):
                print(f"Klaida: Nėra tokio filtro parametro '{key}'.")
                return
            filtered_books = [book for book in filtered_books if getattr(book, key, None) == value]

        for arg in args:
            filtered_books = [book for book in filtered_books if arg.lower() in book.title.lower()]

        if not filtered_books:
            print("Nerasta atitinkančių knygų.")
        for book in filtered_books:
            print(book)

print('- - - - - - - - -ŽINGSNIS 3: Naudokite datetime paskolos valdymui- - - - - - - - - - - - - - ')
#
# # ŽINGSNIS 3: Naudokite datetime paskolos valdymui
# # • Kai vartotojas pasiskolina knygą, įrašykite paskolos datą.
# # • Pridėkite metodą due_date(), kuris grąžins datą, kada knyga turi būti grąžinta
# # (pvz., po 14 dienų).

print('- - - - - - - - -ŽINGSNIS 4: Sukurkite sąveiką su vartotoju- - - - - - - - - - - - - - ')
#
# # ŽINGSNIS 4: Sukurkite sąveiką su vartotoju
# # • Naudokite while ciklą, kad vartotojas galėtų:
# # o Pridėti naują knygą į biblioteką.
# # o Peržiūrėti visą bibliotekos knygų sąrašą.
# # o Pasiskolinti knygą.
# # o Grąžinti knygą.
# # o Filtruoti knygas pagal autorių, metus ar pavadinimą.
# # o Išeiti iš programos.
#
def main():
    library = Library()

    while True:
        print("\nPasirinkite veiksmą:")
        print("1. Pridėti knygą")
        print("2. Peržiūrėti knygų sąrašą")
        print("3. Pasiskolinti knygą")
        print("4. Grąžinti knygą")
        print("5. Filtruoti knygas")
        print("6. Išeiti")

        choice = input("Įveskite pasirinkimą (1-6): ")

        if choice == '1':
            title = input("Įveskite knygos pavadinimą: ")
            author = input("Įveskite knygos autorių: ")
            year = input("Įveskite knygos išleidimo metus: ")

            try:
                year = int(year)
            except ValueError:
                print("Klaida: Metai turi būti skaičius!")
                continue

            book = Book(title, author, year)
            library.add_book(book)
            print(f"Knyga '{title}' buvo pridėta į biblioteką.")

        elif choice == '2':
            print("\nVisos bibliotekos knygos:")
            library.display_books()

        elif choice == '3':
            title = input("Įveskite knygos pavadinimą, kurią norite pasiskolinti: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
            library.return_book(title)

        elif choice == '5':
            print("\nFiltravimo galimybės:")
            print("1. Pagal autorių")
            print("2. Pagal metus")
            print("3. Pagal pavadinimą")

            filter_choice = input("Pasirinkite filtrą (1-3): ")

            if filter_choice == '1':
                author = input("Įveskite autoriaus vardą: ")
                library.filter_books(author=author)
            elif filter_choice == '2':
                try:
                    year = int(input("Įveskite metus: "))
                    library.filter_books(year=year)
                except ValueError:
                    print("Klaida: Metai turi būti skaičius!")
            elif filter_choice == '3':
                title = input("Įveskite pavadinimo dalį: ")
                library.filter_books(title=title)

        elif choice == '6':
            print("Ačiū, kad naudojotės biblioteka!")
            break
        else:
            print("Klaida: Pasirinkite galiojantį veiksmą (1-6).")


if __name__ == "__main__":
    main()

# print('- - - - - - - - -3. Papildomos Sąlygos:- - - - - - - - - - - - - - ')
#
# # 3. Papildomos Sąlygos:
# # • Naudokite try-except klaidoms suvaldyti, pvz., neteisingai įvedus metus.
# # • Naudokite *args ir **kwargs knygų filtravimui pagal skirtingus kriterijus.


# ### - - -       -- - -  Detytojo kodas - - - - - - -
#
# import datetime
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.available = True
#         self.borrow_date = None
#
#     def __str__(self):
#         status = "Prieinama" if self.available else f"Pasiskolinta iki {self.due_date()}"
#         return f"{self.title}, autorius: {self.author}, išleista: {self.year}, Statusas: {status}"
#
#     def is_classic(self):
#         current_year = datetime.datetime.today().year
#         return current_year - self.year > 50
#
#     def due_date(self):
#         if self.borrow_date:
#             return (self.borrow_date + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
#         return None
#
#     def is_overdue(self):
#         if self.borrow_date:
#             return datetime.datetime.today() > self.borrow_date + datetime.timedelta(days=14)
#         return False
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#         print("Knyga pridėta sėkmingai!")
#
#     def display_books(self):
#         if not self.books:
#             print("Biblioteka tuščia.")
#         for book in self.books:
#             print(book)
#
#     def borrow_book(self, title):
#         try:
#             for book in self.books:
#                 if book.title.lower() == title.lower() and book.available:
#                     book.available = False
#                     book.borrow_date = datetime.datetime.today()
#                     print(f"Jūs sėkmingai pasiskolinote knygą: {book.title}")
#                     return
#             raise ValueError("Knyga nerasta arba ji jau pasiskolinta.")
#         except ValueError as e:
#             print(e)
#
#     def return_book(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower() and not book.available:
#                 book.available = True
#                 book.borrow_date = None
#                 print(f"Jūs sėkmingai grąžinote knygą: {book.title}")
#                 return
#         print("Knyga nerasta arba ji nebuvo pasiskolinta.")
#
#     def filter_books(self, *args, **kwargs):
#         filtered_books = self.books
#
#         for key, value in kwargs.items():
#             if key == "title":
#                 filtered_books = [book for book in filtered_books if book.title == value]
#             elif key == "author":
#                 filtered_books = [book for book in filtered_books if book.author == value]
#             elif key == "year":
#                 filtered_books = [book for book in filtered_books if book.year == value]
#
#         for book in filtered_books:
#             print(book)
#
# library = Library()
#
# while True:
#     print("""
# 1. Pridėti naują knygą
# 2. Peržiūrėti bibliotekos knygas
# 3. Pasiskolinti knygą
# 4. Grąžinti knygą
# 5. Filtruoti knygas
# 6. Išeiti
#     """)
#
#     choice = input("Pasirinkite veiksmą: ")
#
#     if choice == "1":
#         title = input("Įveskite knygos pavadinimą: ")
#         author = input("Įveskite autorių: ")
#         try:
#             year = int(input("Įveskite išleidimo metus: "))
#             book = Book(title, author, year)
#             library.add_book(book)
#         except ValueError:
#             print("Įveskite tinkamą metų formatą!")
#     elif choice == "2":
#         library.display_books()
#     elif choice == "3":
#         title = input("Įveskite knygos pavadinimą, kurią norite pasiskolinti: ")
#         library.borrow_book(title)
#     elif choice == "4":
#         title = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
#         library.return_book(title)
#     elif choice == "5":
#         key = input("Filtruoti pagal (title/author/year): ")
#         value = input("Įveskite reikšmę: ")
#         if key in ["title", "author"]:
#             library.filter_books(**{key: value})
#         elif key == "year":
#             try:
#                 year = int(value)
#                 library.filter_books(year=year)
#             except ValueError:
#                 print("Metai turi būti skaičius.")
#         else:
#             print("Netinkamas filtravimo pasirinkimas.")
#     elif choice == "6":
#         print("Programa baigiama.")
#         break
#     else:
#         print("Netinkamas pasirinkimas. Bandykite dar kartą.")






