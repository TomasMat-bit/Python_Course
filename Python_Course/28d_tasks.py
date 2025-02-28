from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import date, timedelta

engine = create_engine('sqlite:///library_final.db')
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)
    borrowed_books = relationship('BorrowedBook', back_populates='book')


class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    borrowed_books = relationship('BorrowedBook', back_populates='reader')


class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id = Column(Integer, ForeignKey('readers.id'), nullable=False)
    borrowed_at = Column(Date, nullable=False)
    return_due_date = Column(Date, nullable=False)
    book = relationship('Book', back_populates='borrowed_books')
    reader = relationship('Reader', back_populates='borrowed_books')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def seed_books():
    books = [
        Book(title="Python programavimas. Pirmieji žingsniai", author="Marius Gaidys", year_published=2020),
        Book(title="JavaScript programavimas", author="Andrius Dainys", year_published=2019),
        Book(title="Kurkite interneto aplikacijas su PHP", author="Povilas Dainys", year_published=2018),
        Book(title="Java programavimas. Pagrindai ir praktika", author="Saulius Tamošiūnas", year_published=2017),
        Book(title="C++ programavimo pradžiamokslis", author="Vaidotas Kasperaitis", year_published=2021),
        Book(title="Web dizainas ir HTML", author="Simonas Jankauskas", year_published=2016),
        Book(title="Mobiliosios aplikacijos su Kotlin", author="Irma Balčiūnaitė", year_published=2020),
        Book(title="Programavimas su C#", author="Tomas Marčiukaitis", year_published=2022),
        Book(title="Algoritmai ir duomenų struktūros", author="Vaidotas Žukauskas", year_published=2021),
        Book(title="Python duomenų analizė", author="Rūta Stankevičiūtė", year_published=2020)
    ]
    for book in books:
        session.add(book)
    session.commit()


def login():
    print("Prisijungimas į biblioteką")
    name = input("Įveskite savo vardą: ")
    surname = input("Įveskite savo pavardę: ")
    email = input("Įveskite savo el. pašto adresą: ")

    reader = session.query(Reader).filter_by(email=email).first()

    if not reader:
        print("Vartotojas nerastas. Prašome užsiregistruoti.")
        return None
    elif reader.name != name or reader.surname != surname:
        print("Netinkami prisijungimo duomenys.")
        return None
    else:
        print(f"Sveiki atvykę, {reader.name} {reader.surname}!")
        return reader


# Funkcija pridėti skaitytoją
def add_reader():
    name = input('Įveskite skaitytojo vardą: ')
    surname = input('Įveskite skaitytojo pavardę: ')
    email = input('Įveskite skaitytojo el. paštą: ')

    # Patikriname, ar el. paštas jau egzistuoja
    existing_reader = session.query(Reader).filter_by(email=email).first()
    if existing_reader:
        print('Klaida: El. paštas jau užregistruotas')
        return

    reader = Reader(name=name, surname=surname, email=email)
    session.add(reader)
    session.commit()
    print('Skaitytojas pridėtas')


# Funkcija prisijungus rodyti knygas ir pasirinkimus
def library_menu(reader):
    while True:
        print(f"\nSveiki, {reader.name} {reader.surname}!")
        print('1. Paskolinti knygą')
        print('2. Atnaujinti knygą')
        print('3. Ištrinti knygą')
        print('4. Išvardyti esamas knygas')
        print('5. Išvardyti paskolintas knygas')
        print('6. Grąžinti knygą')
        print('7. Išeiti')

        choice = input('Pasirinkite veiksmą: ')

        if choice == '1':
            lend_book(reader)
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            list_books()
        elif choice == '5':
            list_borrowed_books(reader)
        elif choice == '6':
            return_book(reader)
        elif choice == '7':
            print('Viso gero!')
            break
        else:
            print("Netinkamas pasirinkimas. Bandykite dar kartą.")


# Funkcija paskolinti knyga
def lend_book(reader):
    try:
        book_id = int(input('Įveskite knygos ID: '))
    except ValueError:
        print('Klaida: Įveskite galiojantį skaičių!')
        return
    book = session.query(Book).filter(Book.id == book_id, Book.available == True).first()
    if not book:
        print('Knyga nėra prieinama')
        return

    borrowed_at = date.today()
    return_due_date = borrowed_at + timedelta(days=14)

    borrowed_book = BorrowedBook(book_id=book_id, reader_id=reader.id, borrowed_at=borrowed_at,
                                 return_due_date=return_due_date)
    book.available = False
    session.add(borrowed_book)
    session.commit()
    print('Knyga paskolinta')


# Funkcija atnaujinti knyga
def update_book():
    try:
        book_id = int(input('Įveskite knygos ID: '))
    except ValueError:
        print('Klaida: Įveskite galiojantį skaičių!')
        return
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print("Knyga nerasta!")
        return
    book.title = input(f'Įveskite naują pavadinimą ({book.title}): ') or book.title
    book.author = input(f'Įveskite naują autorių ({book.author}): ') or book.author
    session.commit()
    print('Knyga atnaujinta')


# Funkcija istrinti knyga
def delete_book():
    try:
        book_id = int(input('Įveskite knygos ID, kurią norite ištrinti: '))
    except ValueError:
        print('Klaida: Įveskite galiojantį skaičių!')
        return
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print('Knyga nerasta!')
        return
    session.delete(book)
    session.commit()
    print('Knyga ištrinta')


# Funkcija isvardnyti visas knygas
def list_books():
    books = session.query(Book).all()
    for book in books:
        status = 'Prieinama' if book.available else 'Paskolinta'
        print(f'{book.id}: {book.title} - {book.author} ({book.year_published}) - {status}')


# Funkcija isvardyti paskolintas knygas
def list_borrowed_books(reader):
    borrowed_books = session.query(BorrowedBook).filter_by(reader_id=reader.id).all()
    if not borrowed_books:
        print("Nėra paskolintų knygų.")
        return
    for bb in borrowed_books:
        book = session.query(Book).filter_by(id=bb.book_id).first()
        print(f'{book.title} - Grąžinimo data: {bb.return_due_date}')


# Funkcija gra=inti knyga
def return_book(reader):

    borrowed_books = session.query(BorrowedBook).filter_by(reader_id=reader.id).all()

    if not borrowed_books:
        print("Jūs neturite paskolintų knygų.")
        return

    print("Jūs paskolinote šias knygas:")
    for index, bb in enumerate(borrowed_books, start=1):
        book = session.query(Book).filter_by(id=bb.book_id).first()
        print(f"{index}. {book.title} - Grąžinimo data: {bb.return_due_date}")

    try:
        book_choice = int(input("Pasirinkite knygą, kurią norite grąžinti (įveskite numerį): "))
        if book_choice < 1 or book_choice > len(borrowed_books):
            print("Klaida: Neteisingas pasirinkimas.")
            return
    except ValueError:
        print("Klaida: Prašome įvesti galiojantį numerį.")
        return

    selected_borrowed_book = borrowed_books[book_choice - 1]
    book_to_return = session.query(Book).filter_by(id=selected_borrowed_book.book_id).first()

# Atnaujiname knygos busena i prieinama
    book_to_return.available = True
    session.delete(selected_borrowed_book)
    session.commit()
    print(f"Knyga '{book_to_return.title}' grąžinta sėkmingai.")


# Programos meniu
def main():
    while True:
        print('Biblioteka')
        print('1. Prisijungti')
        print('2. Registruoti skaitytoją')
        print('3. Išeiti')

        choice = input('Pasirinkite veiksmą: ')

        if choice == '1':
            reader = login()
            if reader:
                library_menu(reader)
        elif choice == '2':
            add_reader()
        elif choice == '3':
            print('Viso gero!')
            break
        else:
            print("Netinkamas pasirinkimas. Bandykite dar kartą.")


if __name__ == '__main__':
    seed_books()
    main()

