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

print('-------  Užduotis 4   ----------------')
