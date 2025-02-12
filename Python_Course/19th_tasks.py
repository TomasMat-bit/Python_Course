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
# DESTYTOJO KODAS:




print(' - - - - - - - - - Užduotis: 4 - - - - - - - - - - - ')
