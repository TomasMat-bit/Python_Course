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
    ("Petras", "Petraitis", 10),
    ("Asta", "Astaitė", 7),
    ("Marius", "Mariūnas", 6),
    ("Laura", "Pauraitė", 12),
    ("Simonas", "Simaitis", 8),
    ("Gabija", "Gabytė", 12),
    ("Tomas", "Pomaitis", 12),
    ("Ieva", "Ievaitė", 9),
    ("Dainius", "Dainaitis", 10)
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
    mokytojai = session.query(Mokytojas).limit(5).all()
    for mokytojas in mokytojai:
        print(f"{mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}")

# Testuojame funkcijas
print("Mokiniai:")
spausdinti_mokinius()

print("\nMokytojai:")
spausdinti_mokytojus()

print(' - - - - 4. Užduotis  - - - - - - - ')

# 5. Duomenų trynimas
# Užduotis:
# • Parašykite funkciją, kuri pašalina mokinį iš duomenų bazės pagal id.
# • Parašykite funkciją, kuri pašalina mokytoją pagal id.
# Papildomas iššūkis:
# • Ištrinkite visus mokinius, kurie jau baigė mokyklą (12 klasė).


def trinti_mokini_pagal_id(mokinys_id):
    mokinys = session.query(Mokinys).filter_by(id=mokinys_id).first()
    if mokinys:
        session.delete(mokinys)
        session.commit()
        print(f'Mokinys {mokinys.vardas} {mokinys.pavarde} buvo ištrintas.')
    else:
        print('Mokinys su tokiu ID nerastas.')

trinti_mokini_pagal_id(1)  # Pavyzdys, kur 1 yra mokinio ID
spausdinti_mokinius()
print('-'* 30)

def trinti_mokytoja_pagal_id(mokytojas_id):
    mokytojas = session.query(Mokytojas).filter_by(id=mokytojas_id).first()
    if mokytojas:
        session.delete(mokytojas)
        session.commit()
        print(f'Mokytojas {mokytojas.vardas} {mokytojas.pavarde} buvo ištrintas.')
    else:
        print('Mokytojas su tokiu ID nerastas.')

trinti_mokytoja_pagal_id(1)  # Pavyzdys, kur 1 yra mokytojo ID
spausdinti_mokytojus()
print('-'* 30)

def trinti_mokinius_kurie_baige_mokykla():
    mokiniai_12_klase = session.query(Mokinys).filter_by(klase=12).all()
    for mokinys in mokiniai_12_klase:
        session.delete(mokinys)
    session.commit()
    print('Visi 12 klasės mokiniai buvo ištrinti.')

trinti_mokinius_kurie_baige_mokykla()
print('Mokiniai:')
spausdinti_mokinius()
print('-'* 30)

print('-'* 30, 'DESTYTOJO KODAS: ','-'* 30)



print(' - - - - 5. Užduotis  - - - - - - - ')

# 6. Paieška ir filtravimas
# Užduotis:
# • Parašykite funkciją, kuri randa mokinį pagal vardą.
# • Parašykite funkciją, kuri randa visus mokinius, kurių pavardė prasideda raide "P".
# Papildomas iššūkis:
# • Raskite visus mokytojus, kurių vardas baigiasi raide „s“.

def rasti_mokini_pagal_varda(vardas):
    mokinys = session.query(Mokinys).filter_by(vardas=vardas).first()
    if mokinys:
        print(f'Rastas mokinys: {mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}')
    else:
        print(f'Mokinys su vardu {vardas} nerastas.')

rasti_mokini_pagal_varda("Jonas")
print('-'* 30)

def rasti_mokinius_pagal_pavarde_pirma_raide():
    mokiniai = session.query(Mokinys).filter(Mokinys.pavarde.like('P%')).all()
    if mokiniai:
        for mokinys in mokiniai:
            print(f'{mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}')
    else:
        print('Mokiniai su pavarde, prasidedančia raide "P", nerasti.')

rasti_mokinius_pagal_pavarde_pirma_raide()
print('-'* 30)

def rasti_mokytojus_pagal_varda_paskutine_raide():
    mokytojai = session.query(Mokytojas).filter(Mokytojas.vardas.like('%s')).limit(5).all()
    if mokytojai:
        for mokytojas in mokytojai:
            print(f'{mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}')
    else:
        print('Mokytojai, kurių vardas baigiasi raide "s", nerasti.')

rasti_mokytojus_pagal_varda_paskutine_raide()
print('-' * 30)

# print('-'* 30, 'DESTYTOJO KODAS: ','-'* 30)
#
# # from models import Mokinys, Mokytojas, engine
# # from sqlalchemy.orm import sessionmaker
# # from sqlalchemy.exc import MultipleResultsFound, NoResultFound
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# def delete_student_by_id(student_id):
#     student = session.get(Mokinys, student_id)
#     if student:
#         session.delete(student)
#         session.commit()
#         print(f'Mokinys su ID {student_id} pašalintas.')
#     else:
#         print(f'Mokinys su ID {student_id} nerastas.')
#
# def delete_teacher_by_id(teacher_id):
#     teacher = session.get(Mokytojas, teacher_id)
#     if teacher:
#         session.delete(teacher)
#         session.commit()
#         print(f'Mokytojas su ID {teacher_id} pašalintas.')
#     else:
#         print(f'Mokytojas su ID {teacher_id} nerastas.')
#
# def delete_graduated_students():
#     graduated_students = session.query(Mokinys).filter_by(klase=12).all()
#     for student in graduated_students:
#         session.delete(student)
#     session.commit()
#     print(f'Visi 12 klasės mokiniai pašalinti.')
#
# def find_student_by_name(name):
#     try:
#         student = session.query(Mokinys).filter_by(vardas=name).one()
#         print(student)
#     except NoResultFound:
#         print(f'Mokinys su vardu {name} nerastas.')
#     except MultipleResultsFound:
#         print(f'Rasta daugiau nei viena įrašų su vardu {name}.')
#
# def find_students_by_lastname_initial(letter):
#     students = session.query(Mokinys).filter(Mokinys.pavarde.ilike(f'{letter}%')).all()
#     for student in students:
#         print(student)
#
# def find_teachers_by_name_endswith(letter):
#     teachers = session.query(Mokytojas).filter(Mokytojas.vardas.ilike(f'%{letter}')).all()
#     for teacher in teachers:
#         print(teacher)

print(' - - - - 6. Užduotis  - - - - - - - ')

# 7. Rikiavimas ir skaičiavimai
# Užduotis:
# • Parašykite funkciją, kuri išveda visus mokinius pagal klasę (didėjančia tvarka).
# • Parašykite funkciją, kuri suskaičiuoja, kiek yra mokinukų kiekvienoje klasėje.
# Papildomas iššūkis:
# • Suskaičiuokite vidutinį mokinių skaičių klasėje.

from sqlalchemy import func

def spausdinti_mokinius_pagal_klase():
    mokiniai = session.query(Mokinys).order_by(Mokinys.klase).all()
    for mokinys in mokiniai:
        print(f'{mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}')

spausdinti_mokinius_pagal_klase()
print('-' * 30)



def suskaiciuoti_mokinius_kiekvienoje_klaseje():
    klasiu_skaicius = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    for klase, skaicius in klasiu_skaicius:
        print(f'Klasė: {klase}, mokinių skaičius: {skaicius}')

suskaiciuoti_mokinius_kiekvienoje_klaseje()
print('-' * 30)


def vidutinis_mokiniu_skaicius_klaseje():
    klasiu_skaicius = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    bendras_mokiniu_skaicius = sum([skaicius for _, skaicius in klasiu_skaicius])
    unikalios_klases = len(klasiu_skaicius)

    if unikalios_klases > 0:
        vidurkis = bendras_mokiniu_skaicius / unikalios_klases
        print(f'Vidutinis mokinių skaičius klasėje: {vidurkis:.2f}')
    else:
        print('Nėra duomenų apie klases.')

vidutinis_mokiniu_skaicius_klaseje()
print('-' * 30)
