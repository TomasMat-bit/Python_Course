print('-------  Užduotis 1   ----------------')

# 1. Klasės kūrimas ir statiniai laukai
# Užduotis 1:
# 1. Sukurkite klasę Car, kurioje būtų statinis laukas manufacturer su reikšme
# "Toyota".
# 2. Išveskite manufacturer reikšmę.
# 3. Sukurkite kitą klasę Bike, kurioje būtų statinis laukas manufacturer su reikšme
# "Yamaha" ir taip pat išveskite šią reikšmę.

class Car:
    manufacturer = 'Toyota'
print(Car.manufacturer)  # Toyota

class Bike:
    manufacturer = 'Yamaha'
print(Bike.manufacturer)  # Yamaha

#  DESTYTOJO KODAS
# # 1
# # Klasė Car su statiniu lauku
# class Car:
#     manufacturer = "Toyota"
#
# # Išvedame statinio lauko reikšmę
# print("Car manufacturer:", Car.manufacturer)
#
# # Klasė Bike su statiniu lauku
# class Bike:
#     manufacturer = "Yamaha"
#
# # Išvedame statinio lauko reikšmę
# print("Bike manufacturer:", Bike.manufacturer)
#

print('-------  Užduotis 2   ----------------')

# 2. Konstruktorius __init__ ir instancijos laukų inicializavimas
# Užduotis 2:
# 1. Sukurkite klasę Book, kuri turės laukus: title, author, year.
# 2. Naudodami __init__ konstruktorių, inicializuokite šiuos laukus.
# 3. Sukurkite kelias Book instancijas su skirtingais duomenimis
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
book3 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(f'Knyga: {book1.title}, autorius: {book1.author}, metai: {book1.year}')
print(f'Knyga: {book2.title}, autorius: {book2.author}, metai: {book2.year}')
print(f'Knyga: {book3.title}, autorius: {book3.author}, metai: {book3.year}')
print(f'Knyga: {book4.title}, autorius: {book4.author}, metai: {book4.year}')

#  DESTYTOJO KODAS
# # 2
# # Klasė Book su konstruktoriu __init__
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
# # Sukuriame kelias Book instancijas
# book1 = Book("1984", "George Orwell", 1949)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
#
# # Išvedame informaciją apie knygas
# print(f"Book 1: {book1.title}, Author: {book1.author}, Year: {book1.year}")
# print(f"Book 2: {book2.title}, Author: {book2.author}, Year: {book2.year}")
# print(f"Book 3: {book3.title}, Author: {book3.author}, Year: {book3.year}")
#

print('-------  Užduotis 3   ----------------')

# 3. Statinio lauko ir instancijų naudojimas
# Užduotis 3:
# 1. Naudodami klasę Book iš ankstesnės užduoties, išveskite:
# a. Statinį lauką publisher (pridėkite jį kaip "Penguin").
# b. Kiekvienos knygos pavadinimą ir autorių.

class Book:
    publisher = 'Penguin'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
book3 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(f'Knyga: {book1.title}, autorius: {book1.author}')
print(f'Knyga: {book2.title}, autorius: {book2.author}')
print(f'Knyga: {book3.title}, autorius: {book3.author}')
print(f'Knyga: {book4.title}, autorius: {book4.author}')

print('-------  DESTYTOJO KODAS   ----------------')

#  DESTYTOJO KODAS
# # 3
# # Pridedame statinį lauką publisher į Book klasę
class Book:
    publisher = "Penguin"  # Statinis laukas

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Sukuriame kelias Book instancijas
books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]

# Išvedame statinį lauką publisher
print("Publisher:", Book.publisher)

# Išvedame kiekvienos knygos pavadinimą ir autorių
for book in books:
    print(f"Title: {book.title}, Author: {book.author}")
#

print('-------  Užduotis 4   ----------------')

# 4. Klasės instancijų atvaizdavimas
# Užduotis 4:
# 1. Išveskite bet kurią Book instanciją naudojant print().
# 2. Pastebėkite rezultatą (turėtų būti atminties adresas).
books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]
book_instance = books
print(book_instance)

print('-------  Užduotis 5   ----------------')
# 5. Savų metodų kūrimas klasėje
# Užduotis 5:
# 1. Pridėkite metodą get_book_age(), kuris grąžins, kiek metų praėjo nuo knygos
# išleidimo.
# 2. Sukurkite kelias knygas ir iškvieskite šį metodą.

from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        current_year = datetime.now().year
        return current_year - self.year

books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960)
]

for book in books:
    print(f"Book: {book.title}, Age: {book.get_book_age()} years")


print('-------  Užduotis 5   ----------------')
# 6. Metodų iškvietimas ir rezultatų naudojimas
# Užduotis 6:
# 1. Sukurkite Book instanciją ir naudokite get_book_age() metodą.
# 2. Išveskite rezultatą kartu su pranešimu:
# "Knyga <pavadinimas> yra <amžius> metų senumo."

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

age = book.get_book_age()
print(f"Knyga '{book.title}' yra {age} metų senumo.")