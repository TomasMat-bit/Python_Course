
print(' - - - - - - - - - Pamoka 19 Darbas su SQLite - - - - - - - - - - - - - ')
print(' - - - - - - - - - Darbas su SQLite ir Python - - - - - - - - - - - - - ')
print(' - - - - - - - - - Prisijungimas prie Duomenų Bazės - - - - - - - - - - ')

import sqlite3

def init_database():
    conn = sqlite3.connect('pavyzdys.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS studentai (
        vardas TEXT,
        pavarde TEXT,
        klase INTEGER
    )
    ''')
    conn.commit()
    conn.close()

print(' - - - - - - - - - Duomenų Įterpimas (INSERT) - - - - - - - - - - ')

def append_to_studentai(vardas, pavarde, klase):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)", (vardas, pavarde, klase))

print(' - - - - - - - - - Duomenų Skaitymas (SELECT) - - - - - - - - - - ')

def print_all_studentai_names():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT vardas FROM studentai"):
            print(row)

def print_all_studentai_by_klase(klase):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM studentai WHERE klase = ?", (klase,)):
            print(row)
def print_all_studentai_row():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM studentai"):
            print(row)

append_to_studentai('John', 'Johnaitis', 10)
append_to_studentai('Gitanas', 'Nauseda', 10)
append_to_studentai('Dalia', 'Grybauskaite', 10)
print_all_studentai_by_klase(10)
print_all_studentai_row()

print(' - - - - - - - - - Duomenų Atnaujinimas (UPDATE) - - - - - - - - - - ')

def change_klase_by_name(klase, vardas):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE studentai SET klase = ? WHERE vardas = ?", (klase, vardas))

def remove_row_by_name(vardas):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute("DELETE FROM studentai WHERE vardas = ?", (vardas,))

print(' - - - - - - - - - Duomenų Ištrynimas (DELETE) - - - - - - - - - - ')

def delete_all_rows():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute("DELETE FROM studentai")

delete_all_rows()
# print_all_studentai_rows()

print(' - - - - - - - - - Uždarymo Praktika - - - - - - - - - - ')
# Ryšio uždarymas
conn = sqlite3.connect("pavyzdys.db")
conn.close()