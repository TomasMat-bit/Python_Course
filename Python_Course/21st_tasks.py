print(' - - - - 1. Užduotis  - - - - - - - ')
# 1. Duomenų bazės ir modelio sukūrimas
# Užduotis:
# • Sukurkite SQLite duomenų bazę mokykla.db.
# • Sukurkite SQLAlchemy modelį Mokinys, kuris turės šiuos laukus:
# o id (pirminis raktas, Integer)
# o vardas (String)
# o pavarde (String)
# o klase (Integer)
# Papildomas iššūkis: Sukurkite antrą modelį Mokytojas, kuris turės laukus:
# • id (pirminis raktas, Integer)
# • vardas (String)
# • pavarde (String)
# • dalykas (String)

from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

Base.metadata.create_all(engine)

print(' - - - - 1. Užduotis  - - - - - - - ')





