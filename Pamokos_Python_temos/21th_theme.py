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
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

Session = sessionmaker(bind=engine)
session = Session()

def print_all_records():
    for row in session.query(Projektas).all():
        print(row)

print_all_records()

# session.query(<lenteles klasė>).filter_by(<lauko_pavadinimas>=<paieškos frazė>).all()

filtered_rows = session.query(Projektas).filter_by(kaina=321).all()
print(f'filtered_rows: {filtered_rows[0]}')

paisekos_pavadinimas = 'Web project'
filtered_rows = session.query(Projektas).filter_by(pavadinimas=paisekos_pavadinimas, kaina=10000).all()
print(f'filtered_rows: {filtered_rows[0]}')


try:
    filtered_rows = session.query(Projektas).filter_by(pavadinimas='Project2').one()
except NoResultFound:
    print('Nėra rezultatų')
except MultipleResultsFound:
    print('Ne vienas rezultatas')



# filtered_rows = session.query(Projektas).filter_by(pavadinimas='Web project').first()

# print(filtered_rows)

# print('-' * 30)
# for row in filtered_rows:
#     print(row)

# print_all_records()
#
# row_id = 2
# row_object = session.get(Projektas, row_id)
# print('PAGAUTAS OBJEKTAS: ', row_object)
#
# session.delete(row_object)
# session.commit()
#
# print_all_records()
#
# pavadinimas = input("Įveskite projekto pavadinimą: ")
# kaina = float(input('Įveskite kainą: '))
#
# row_object = Projektas(pavadinimas=pavadinimas, kaina=kaina)
# session.add(row_object)
# session.commit()
#
# all_rows = session.query(Projektas).all()
#
# for row in all_rows:
#     print(row)
#
# for row in all_rows:
#     print(f'ID: {row.id}, Pavadinimas: {row.pavadinimas}, Kaina: {row.kaina}')



print('------------------------------------------------------------------------------------------------------')












