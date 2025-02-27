# # SQL Saugumas ir SQL Injection Atakos
# # SQL Injection demonstracija
#
# import sqlite3
#
# conn = sqlite3.connect('sql_injection.db')
# c = conn.cursor()
#
# # - STEP1: DB and TABLE creation
#
# # query = """CREATE TABLE IF NOT EXISTS user (
# #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
# #     username TEXT NOT NULL,
# #     password TEXT NOT NULL,
# #     email TEXT NOT NULL
# # );
# # """
# #
# # with conn:
# #     c.execute(query)
# #
# # with conn:
# #     c.execute('INSERT INTO user VALUES (NULL, "Adomas", "123456", "ada@gmail.com")')
# #     c.execute('INSERT INTO user(username, password, email) VALUES ("Adomas", "Adom123456", "adss@gmail.com")')
# #     c.execute('INSERT INTO user(username, password, email) VALUES ("Tomas", "Tom123456", "tos@gmail.com")')
#
#
#
#
# # #STEP2: cHECK IF USERS CREATED
# # with conn:
# #     c.execute('SELECT * FROM user')
# # print(c.fetchall())
#
#
#
#
#
# # # STEP 3: GET ALL USERS WITH SQL INJECTIONS
#
# # inp_username = input('Iveskite username: ') "' OR True;--"
# # inp_password = input('Iveskite password: ') ""
# # query = f'SELECT * FROM user WHERE user.username="{inp_username}" AND user.password="{inp_password}";'
# #
# # with conn:
# #     print('>>>>', query)
# #     c.execute(query)
# #     res = c.fetchall()
# #     if res:
# #         print('Jusu profilio duomenys yra: ')
# #         print(res)
# #     else:
# #         print(f'Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis')
#
#
# # - STEP4: PROTECTION
#
# inp_username = input('Iveskite username: ')
# inp_password = input('Iveskite password: ')
#
# with conn:
#     c.execute('SELECT * FROM user WHERE user.username=? AND user.password=?;', (inp_username, inp_password))
#     res = c.fetchall()
#     if res:
#         print('Jūsų profilio duomenys yra: ')
#         print(res)
#     else:
#         print(f'Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis')
from traitlets.utils.descriptions import describe

# SQL Santykiai: One-to-Many ir Many-to-Many
# One-to-Many ryšys
print('                                   -                   - - - - -     - - - - - ')

from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session

engine = create_engine("sqlite:///one_to_many.db")

Base = declarative_base()
 # - STEP 1 : LENTEKIU KURIMAS
class Coder(Base):
    __tablename__ = 'coder'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    xp_years = Column(Integer)

    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="coders")

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


    coders = relationship("Coder", back_populates="team")

# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

team_row = Team(name='DevOps', description='DevOps team')
coder_row = Coder(first_name='Romas', last_name='Adomaitis', age=35, team=team_row)
coder_row2 = Coder(first_name='Adomas', last_name='Romaitis', age=25, team=team_row)

session.add(team_row)
session.commit()

print(coder_row.first_name, coder_row.last_name, coder_row.team.name) # Romas Adomaitis DevOps
print(' - - - - - - - ')
print(', '.join([x.first_name for x in team_row.coders])) # Romas, Adomas
print(' - - - - - - - ')
print(*[f"{row.first_name} {row.last_name}\n" for row in team_row.coders]) # Romas Adomaitis / Adomas Romaitis


