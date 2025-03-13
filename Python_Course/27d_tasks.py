print(' TEMA - SQL Injection Atakos Demonstracija')
print(' - - - - - - - - - - - - - - - - - - -Užduotis: 1  - - - - - - - - - - - - - - - - - - - - -- - ')

# 1. Sukurkite lentelę admin_users su šiais laukais:
# a. id (pirminis raktas, INTEGER)
# b. username (TEXT, unikalus)
# c. password (TEXT, negali būti NULL)
# d. role (TEXT, numatytoji reikšmė "user")
# 2. Įterpkite tris vartotojus: vieną administratorių (role="admin") ir du paprastus
# vartotojus.
# 3. Parašykite SQL užklausą, kuri leidžia prisijungti vartotojui pagal username ir
# password, tačiau nenaudokite parametrizuotų užklausų.
# 4. Naudodami SQL Injection techniką prisijunkite prie administratoriaus paskyros,
# nors nežinote slaptažodžio.

print(' TEMA - SQL Injection Atakų Prevencija')

# 1. Pataisykite ankstesnę užklausą, kad ji būtų apsaugota nuo SQL Injection,
# naudodami parametrizuotas užklausas.
# 2. Pabandykite prisijungti naudodami ' OR 1=1;-- kaip username. Ar sistema vis dar
# pažeidžiama?

# import sqlite3
#
# conn = sqlite3.connect('27d_task.db')
# c = conn.cursor()
#
# query = """CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL,
#     role TEXT NOT NULL DEFAULT "user"
# );
# """
#
# with conn:
#     c.execute(query)
#
#
# inp_username = input('Įveskite username: ')
# inp_password = input('Įveskite password: ')
#
# query = f"SELECT * FROM admin_users WHERE admin_users.username= '{inp_username}' AND admin_users.password= '{inp_password}';"
#
# with conn:
#     c.execute(query)
#     # c.execute("SELECT * FROM admin_users WHERE admin_users.username= ? AND admin_users.password= ?;", (inp_username, inp_password))
#     res = c.fetchall()
#     if res:
#         print('Jūsų prisijungimo duomenys: ')
#         print(res)
#     else:
#         print('Neteisingi prisijungimo duomenys arba slaptažodis')
#
#
# with conn:
#     c.execute('INSERT INTO admin_users (username, password) VALUES ("genys", "123456");')
#     c.execute('INSERT INTO admin_users (username, password) VALUES ("medis", "789456");')
#     c.execute('INSERT INTO admin_users (username, password, role) VALUES ("namas", "321456" , "admin");')


# DĖSTYTOJO KODAS:

import sqlite3

conn = sqlite3.connect('27d_task.db')
c = conn.cursor()
# c.execute('''
#     CREATE TABLE admin_users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL UNIQUE,
#     password TEXT NOT NULL,
#     role TEXT DEFAULT 'user'
# );''')
#
# users = [
#     ('admin', 'admin', 'admin'),
#     ('user1', '123', 'user'),
#     ('user2', '321', 'user')
# ]
#
# c.executemany('INSERT INTO admin_users (username, password, role) VALUES (?, ? ,?)', users)
# conn.commit()
#
# c.execute('SELECT * FROM admin_users;')
# res = c.fetchall()
# print(res)
#
# print('--- SQL Injection Atakaos Demonstracija ---')
# inp_username = "' OR True;--"
# inp_password = ''
# #
# query = f"SELECT * FROM admin_users WHERE username='{inp_username}' AND password='{inp_password}';"
# print(query)
# #
# c.execute(query)
# res = c.fetchall()
# #
# print('Result: ', res)
#
# print('--- SQL Injection Atakų Prevencija ---')
# inp_username = "' OR True;--"
# inp_password = ''
# #
# query = "SELECT * FROM admin_users WHERE username=? AND password=?"
# print(query)
# #
# c.execute(query, (inp_username, inp_password))
# res = c.fetchall()
# #
# print(res)
#
#
# print(' TEMA - One-to-Many ryšys: Projektai ir užduotys')

print(' - - - - - - - - - - - - - - - - - - -Užduotis: 2  - - - - - - - - - - - - - - - - - - - - -- - ')

# Sukurkite lenteles:
# • Project(id, name, deadline)
# • Task(id, project_id, description, status)
# 1. Pridėkite bent 5 projektus su skirtingais pavadinimais.
# 2. Kiekvienam projektui priskirkite bent 3 užduotis, turinčias skirtingus statusus
# ("Pending", "In Progress", "Completed").
# 3. Parašykite SQL užklausą, kuri grąžina visas užduotis, priklausančias tam tikram
# projektui.
# 4. Parašykite SQL užklausą, kuri pateikia projektus, kuriuose yra bent viena nebaigta
# užduotis.

from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Sukuriame SQLite duomenų bazę
engine = create_engine('sqlite:///projects_tasks_2.db')
Base = declarative_base()

# 1. Lentelė "Project"
class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    deadline = Column(String, nullable=False)

    tasks = relationship('Task', back_populates='project')

# 2. Lentelė "Task"
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)

    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project', back_populates='tasks')

# Sukuriame lenteles duomenų bazėje
Base.metadata.create_all(engine)

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()

# 3. Pridedame 5 projektus
projects_data = [
    Project(name="Website Development", deadline="2025-03-01"),
    Project(name="Mobile App", deadline="2025-04-15"),
    Project(name="Data Analysis", deadline="2025-05-20"),
    Project(name="Marketing Campaign", deadline="2025-06-10"),
    Project(name="AI Research", deadline="2025-07-05"),
]

session.add_all(projects_data)
session.commit()

# 4. Priskiriame kiekvienam projektui 3 užduotis su skirtingais statusais
tasks_data = [
    Task(project_id=1, description="Frontend Development", status="Pending"),
    Task(project_id=1, description="Backend API", status="In Progress"),
    Task(project_id=1, description="Testing", status="Completed"),

    Task(project_id=2, description="UI Design", status="Pending"),
    Task(project_id=2, description="App Development", status="In Progress"),
    Task(project_id=2, description="User Testing", status="Completed"),

    Task(project_id=3, description="Data Collection", status="Pending"),
    Task(project_id=3, description="Model Training", status="In Progress"),
    Task(project_id=3, description="Report Writing", status="Completed"),

    Task(project_id=4, description="Market Research", status="Pending"),
    Task(project_id=4, description="Ad Campaign", status="In Progress"),
    Task(project_id=4, description="Survey Analysis", status="Completed"),

    Task(project_id=5, description="Algorithm Research", status="Pending"),
    Task(project_id=5, description="Model Implementation", status="In Progress"),
    Task(project_id=5, description="Paper Submission", status="Completed"),
]

session.add_all(tasks_data)
session.commit()

# 5. Užklausos

# a) Gauti visas užduotis, priklausančias tam tikram projektui (pvz., projektui su id=1)

# SELECT * FROM task WHERE project_id = 1;

project_id = 1
tasks_for_project = session.query(Task).filter(Task.project_id == project_id).all()
print(f"Užduotys projektui ID {project_id}:")
for task in tasks_for_project:
    print(f"- {task.description} ({task.status})")

# b) Gauti projektus, kuriuose yra bent viena nebaigta užduotis

# SELECT name, deadline
# FROM project
# JOIN task ON project.id = task.project_id
# WHERE task.status != 'Completed'

unfinished_tasks = session.query(Project).join(Task).filter(Task.status != "Completed").distinct().all()
print("\nProjektai su nebaigtomis užduotimis:")
for project in unfinished_tasks:
    print(f"- {project.name}")

# Uždarymas
session.close()








