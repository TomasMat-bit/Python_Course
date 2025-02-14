print(' - - - - - - - - - Užduotis: 1 - - - - - - - - - - - ')

# 1. Prisijungimas prie Duomenų Bazės
# Užduotis:
# 1. Sukurkite Python programą, kuri:
# a. Prisijungia prie SQLite duomenų bazės pavadinimu mokykla.db.
# b. Sukuria lentelę mokykla su stulpeliais: pavadinimas (TEXT), adresas
# (TEXT), mokiniu_skaicius (INTEGER).

import sqlite3
def sukurti_lentele():
    conn = sqlite3.connect('mokykla.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS mokykla (
                    pavadinimas TEXT,
                    adresas TEXT,
                    mokiniu_sk INTEGER)
                    ''')

    conn.commit()
    conn.close()

print(' - - - - - - - - - Užduotis: 2 - - - - - - - - - - - ')

# 2. Duomenų Įterpimas (INSERT)
# Užduotis:
# 1. Įterpkite šiuos duomenis į lentelę mokykla:
# a. "Vilniaus progimnazija", "Vilniaus g. 10", 500
# b. "Kauno gimnazija", "Kauno g. 5", 800
# 2. Parašykite Python funkciją prideti_mokykla, kuri priima tris parametrus
# (pavadinimas, adresas, mokinių skaičius) ir įterpia juos į duomenų bazę.

def prideti_mokykla(pavadinimas, adresas, mokiniu_sk):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_sk) VALUES (?, ?, ?)",(pavadinimas, adresas, mokiniu_sk))
        conn.commit()

def patikrinti_duomenis():
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM mokykla")
        duomenys = c.fetchall()
        for eilute in duomenys:
            print(eilute)


sukurti_lentele()

prideti_mokykla('Vilniaus progimnazija', 'Vilniaus g. 10', 500)
prideti_mokykla('Kauno gimnazija', 'Kauno g. 5', 800)

patikrinti_duomenis()
# DESTYTOJO KODAS:




print(' - - - - - - - - - Užduotis: 3 - - - - - - - - - - - ')

# 3. Duomenų Skaitymas (SELECT)
# Užduotis:
# 1. Sukurkite Python programą, kuri:
# a. Nuskaito visus duomenis iš lentelės mokykla.
# b. Išveda juos tvarkingai formatuotu tekstu (pvz., „Mokykla: Vilniaus
# progimnazija, Adresas: Vilniaus g. 10, Mokinių skaičius: 500“).
# 2. Pridėkite galimybę filtruoti duomenis pagal minimalų mokinių skaičių (pvz., rodyti
# tik tas mokyklas, kuriose yra daugiau nei 600 mokinių).

def nuskaititi_ir_isvesti_duomenis(min_mokiniu_sk=None):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()

        if min_mokiniu_sk is not None:
            c.execute('SELECT * FROM mokykla WHERE mokiniu_sk > ?', (min_mokiniu_sk,))
        else:
            c.execute('SELECT * FROM mokykla')

        duomenys = c.fetchall()

        for eilute in duomenys:
            print(f'Mokykla: {eilute[0]}, Adresas: {eilute[1]}, Mokinių skaičius: {eilute[2]}')

print('Visi mokyklų duomenys:')
nuskaititi_ir_isvesti_duomenis()

print('\n---------------\n')

print('Mokyklos, kuriose daugiau nei 600 mokinių:')
nuskaititi_ir_isvesti_duomenis(min_mokiniu_sk=600)
# # DESTYTOJO KODAS:
# import sqlite3
#
# # Sukuriame (arba prisijungiame prie esamos) duomenų bazės
# conn = sqlite3.connect('mokykla.db')
# cursor = conn.cursor()
#
# # Sukuriame lentelę, jei ji dar neegzistuoja
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS mokykla (
#     pavadinimas TEXT,
#     adresas TEXT,
#     mokiniu_skaicius INTEGER
# )
# ''')
#
#
# # Funkcija duomenų įterpimui
# def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
#     cursor.execute('''
#     INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius)
#     VALUES (?, ?, ?)
#     ''', (pavadinimas, adresas, mokiniu_skaicius))
#     conn.commit()
#
#
# # Įterpiame pateiktus duomenis
# prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
# prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)
#
#
# # Funkcija duomenų nuskaitymui su filtru
# def rodyti_mokyklas(min_mokiniu_skaicius=0):
#     cursor.execute('''
#     SELECT *
#     FROM mokykla
#     WHERE mokiniu_skaicius > ?
#     ''', (min_mokiniu_skaicius,))
#
#     mokyklos = cursor.fetchall()
#
#     for mokykla in mokyklos:
#         print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokinių skaičius: {mokykla[2]}")
#
#
# # Rodome visas mokyklas
# print("Visos mokyklos:")
# rodyti_mokyklas()
#
# # Rodome mokyklas su daugiau nei 600 mokinių
# print("\nMokyklos su daugiau nei 600 mokinių:")
# rodyti_mokyklas(600)
#
# # Uždaryti duomenų bazės ryšį
# conn.close()

print(' - - - - - - - - - Užduotis: 4 - - - - - - - - - - - ')

# 4. Duomenų Atnaujinimas (UPDATE)
# Užduotis:
# 1. Parašykite Python funkciją atnaujinti_mokiniu_skaiciu, kuri:
# a. Priima mokyklos pavadinimą ir naują mokinių skaičių kaip parametrus.
# b. Atnaujina nurodytos mokyklos mokinių skaičių duomenų bazėje.
# 2. Patikrinkite, ar atnaujinimas įvyko sėkmingai, išvesdami visų mokyklų sąrašą po
# pakeitimo.

def atnaujinti_mokiniu_skaiciu(pavadinimas, naujas_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute('UPDATE mokykla SET mokiniu_sk = ? WHERE pavadinimas = ?', (naujas_skaicius, pavadinimas))
        conn.commit()

def nuskaityti_ir_isvesti_duomenis(min_mokiniu_sk=None):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()

        if min_mokiniu_sk is not None:
            c.execute('SELECT * FROM mokykla WHERE mokiniu_sk > ?', (min_mokiniu_sk,))
        else:
            c.execute('SELECT * FROM mokykla')

        duomenys = c.fetchall()

        for eilute in duomenys:
            print(f'Mokykla: {eilute[0]}, Adresas: {eilute[1]}, Mokinių skaičius: {eilute[2]}')

print('Prieš atnaujinimą:')
nuskaityti_ir_isvesti_duomenis()

atnaujinti_mokiniu_skaiciu('Vilniaus progimnazija', 600)
atnaujinti_mokiniu_skaiciu('Kauno gimnazija', 700)

print('\nPo atnaujinimo:')
nuskaityti_ir_isvesti_duomenis()
# # # DESTYTOJO KODAS:
# import sqlite3
#
# def istrink_mokykla(mokyklos_pavadinimas):
#     conn = sqlite3.connect("mokyklos.db")
#     cursor = conn.cursor()
#
#     cursor.execute("DELETE FROM mokyklos WHERE pavadinimas = ?", (mokyklos_pavadinimas,))
#
#     if cursor.rowcount == 0:
#         print(f"Klada: mokykla {mokyklos_pavadinimas} nerasta.")
#     else:
#         conn.commit()
#         print(f"Mokykla {mokyklos_pavadinimas} ištrinta")
#
# def atnaujinti_mokiniu_skaiciu(mokyklos_pavadinimas, naujas_skaicius):
#     conn = sqlite3.connect("mokyklos.db")
#     cursor = conn.cursor()
#
#     cursor.execute("UPDATE mokyklos SET mokiniu_skaicius = ? WHERE pavadinimas = ?",
#                    (naujas_skaicius, mokyklos_pavadinimas))
#
#     if cursor.rowcount == 0:
#         print(f"Klaida: Mokykla '{mokyklos_pavadinimas}' nerasta.")
#     else:
#         conn.commit()
#         print(f"Mokyklos '{mokyklos_pavadinimas}' mokinių skaičius atnaujintas į {naujas_skaicius}.")
#
#     conn.close()
#
# def rodyti_visas_mokyklas():
#     conn = sqlite3.connect("mokyklos.db")
#     cursor = conn.cursor()
#
#     for row in cursor.execute("SELECT pavadinimas, mokiniu_skaicius FROM mokyklos"):
#         print(f"Pavadinimas: {row[0]}, Mokinių skaičius: {row[1]}")
#
#     conn.close()
#
# def sukurti_duomenu_baze():
#     conn = sqlite3.connect("mokyklos.db")
#     cursor = conn.cursor()
#
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS mokyklos (
#             pavadinimas TEXT PRIMARY KEY,
#             mokiniu_skaicius INTEGER
#         )
#     """)
#
#     cursor.executemany("INSERT OR IGNORE INTO mokyklos VALUES (?, ?)", [
#         ("Vilniaus gimnazija", 500),
#         ("Kauno mokykla", 300),
#         ("Klaipėdos progimnazija", 450)
#     ])
#
#     conn.commit()
#     conn.close()
#
# # sukurti_duomenu_baze()
# # atnaujinti_mokiniu_skaiciu("Kauno mokykla", 350)
# istrink_mokykla('Vilniaus gimnazija')
# rodyti_visas_mokyklas()