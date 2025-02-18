# # Darbas su SQLAlchemy ir Python
# print(' - - -- - - - Duomenų bazės sukūrimas ir modelio aprašymas - - -  - - - - - ')
#
# from sqlalchemy import Column, create_engine, Integer, String, Float
# from sqlalchemy.orm import declarative_base, Session
#
# # Sukuriama arba prisijungiama prie SQLite duomenų bazės
# engine = create_engine("sqlite:///projektai.db")
# Base = declarative_base()
#
# # Lentelės aprašymas
# class Projektas(Base):
#     __tablename__ = "projektai"
#     id = Column(Integer, primary_key=True)
#     pavadinimas = Column(String)
#     kaina = Column(Float)
#
# # Sukuriamos lentelės
# Base.metadata.create_all(engine)

print(' - - -- - - - Duomenų įterpimas - - -  - - - - - ')

from models import Projektas, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

pavadinimas = input('Iveskite projekto pavadinima: ')
kaina = float(input('Iveskite kaina: '))

row_object = Projektas(pavadinimas=pavadinimas, kaina=kaina) # Naujos eilutes kurimas
session.add(row_object)
session.commit()

all_rows = session.query(Projektas).all() # Visu eiluciu pasiemimas

for row in all_rows:
    print(row) ## Visu eiluciu printas
for row in all_rows:
    print(f'ID: {row.id}, Pavadinimas: {row.pavadinimas}, Kaina: {row.kaina}')


from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
print('------------------------------------------------------------------------------------------------------')












