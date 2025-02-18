print(' - - - - 1. Užduotis  - - - - - - - ')
# # 1. Duomenų bazės ir modelio sukūrimas
# # Užduotis:
# # • Sukurkite SQLite duomenų bazę mokykla.db.
# # • Sukurkite SQLAlchemy modelį Mokinys, kuris turės šiuos laukus:
# # o id (pirminis raktas, Integer)
# # o vardas (String)
# # o pavarde (String)
# # o klase (Integer)
# # Papildomas iššūkis: Sukurkite antrą modelį Mokytojas, kuris turės laukus:
# # • id (pirminis raktas, Integer)
# # • vardas (String)
# # • pavarde (String)
# # • dalykas (String)
#
# from sqlalchemy import Column, create_engine, Integer, String
# from sqlalchemy.orm import declarative_base
#
# engine = create_engine('sqlite:///mokykla.db')
# Base = declarative_base()
#
# class Mokinys(Base):
#     __tablename__ = 'mokiniai'
#     id = Column(Integer, primary_key=True)
#     vardas = Column(String)
#     pavarde = Column(String)
#     klase = Column(Integer)
#
# class Mokytojas(Base):
#     __tablename__ = 'mokytojai'
#     id = Column(Integer, primary_key=True)
#     vardas = Column(String)
#     pavarde = Column(String)
#     dalykas = Column(String)
#
# Base.metadata.create_all(engine)

print(' - - - - 2. Užduotis  - - - - - - - ')
# 2. Duomenų įterpimas
# Užduotis:
# • Įterpkite bent 3 mokinius ir 2 mokytojus į duomenų bazę naudojant SQLAlchemy
# ORM.
# • Užtikrinkite, kad duomenys būtų išsaugoti naudojant session.commit().
# Papildomas iššūkis: Įterpkite naują mokinį tik tuo atveju, jei jo dar nėra duomenų
# bazėje.

from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Sukuriame duomenų bazę
engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

# Modeliai
class Mokinys(Base):
    __tablename__ = 'mokinys'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

# Sukuriame lenteles
Base.metadata.create_all(engine)

# Sukuriame sesiją
from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Sukuriame duomenų bazę
engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

# Modeliai
class Mokinys(Base):
    __tablename__ = 'mokinys'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

# Sukuriame lenteles
Base.metadata.create_all(engine)

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()

# Funkcija, kuri patikrina, ar mokinys jau yra duomenų bazėje
def ar_mokinys_yra(vardas, pavarde):
    return session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first() is not None

# def ar_mokinys_yra(vardas, pavarde):
#     mokiniai = session.query(Mokinys).all()
#     for row in mokiniai:
#         if row.vardas == vardas and row.pavarde == pavarde:
#             return True

# Pridedame mokinius, jei jų dar nėra
mokiniai = [
    ("Jonas", "Jonaitis", 5),
    ("Petras", "Petraitis", 6),
    ("Asta", "Astaitė", 7)
]

for vardas, pavarde, klase in mokiniai:
    if not ar_mokinys_yra(vardas, pavarde):
        session.add(Mokinys(vardas=vardas, pavarde=pavarde, klase=klase))

# Pridedame mokytojus
mokytojai = [
    Mokytojas(vardas="Rasa", pavarde="Rasaitė", dalykas="Matematika"),
    Mokytojas(vardas="Tomas", pavarde="Tomaitis", dalykas="Fizika")
]

session.add_all(mokytojai)

# Išsaugome pakeitimus
session.commit()

print(' - - - - 3. Užduotis  - - - - - - - ')
# 3. Duomenų skaitymas
# Užduotis:
# • Parašykite funkciją, kuri išveda visų mokinių sąrašą.
# • Parašykite funkciją, kuri išveda visus mokytojus.

# Funkcija mokinių sąrašo išvedimui
def spausdinti_mokinius():
    mokiniai = session.query(Mokinys).all()
    for mokinys in mokiniai:
        print(f"{mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")

# Funkcija mokytojų sąrašo išvedimui
def spausdinti_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    for mokytojas in mokytojai:
        print(f"{mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}")

# Testuojame funkcijas
print("Mokiniai:")
spausdinti_mokinius()

print("\nMokytojai:")
spausdinti_mokytojus()