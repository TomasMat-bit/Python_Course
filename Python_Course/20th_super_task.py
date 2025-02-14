from cgi import print_environ_usage

print(' - - - - Mokyklos duomenų valdymo sistema - - - - - - - - ')
# Tikslas
# Sukurti mokyklos duomenų valdymo sistemą naudojant Python objektinį programavimą,
# SQLite duomenų bazę, funkcijas, iteratorius, dekoratorius ir klaidų valdymą.
print(' - - - - 1. Sistemos Funkcionalumas - - - - - - - - ')
# Sukurti Python programą, kuri galėtų atlikti šiuos veiksmus:
# • Pridėti naujus mokinius į duomenų bazę
# • Pridėti naujus mokytojus
# • Priskirti mokinius į klases
# • Atvaizduoti visus mokinius ir jų informaciją
# • Ieškoti mokinių pagal vardą/pavardę
# • Atnaujinti mokinio informaciją (pvz., pakeisti klasę)
# • Pašalinti mokinį iš sistemos
# • Tvarkyti mokinių sąrašus naudojant iteratorius
# • Naudoti dekoratorių funkcijoms registruoti
# • Naudoti try-except bloką klaidų valdymui
print(' - - - - 2. Struktūra - - - - - - - - ')
# Klasės
# Asmuo (tėvinė klasė)
# Atributai:
# • vardas
# • pavardeMokinys (paveldi Asmuo)
# Papildomi atributai:
# • klase
# • vidurkis
# Mokytojas (paveldi Asmuo)
# Papildomi atributai:
# • dalykas
print(' - - - - 3. Realizacija - - - - - - - - ')
# 1. SQLite duomenų bazė
# • Sukurti dvi lenteles: mokiniai ir mokytojai.
# • Naudoti sqlite3, kad būtų galima atlikti INSERT, SELECT, UPDATE, DELETE
# užklausas.
# 2. Iteratorius mokinių sąrašui
# • Sukurti iteratoriaus klasę, kuri leis eiti per mokinių sąrašą po vieną.
# 3. Dekoratorius funkcijoms registruoti
# • Sukurti dekoratorių, kuris prieš iškviesdamas bet kurią duomenų bazės funkciją
# išspausdina "Vykdoma operacija...".
# 4. Try-except klaidų valdymas
# • Užtikrinti, kad programa necrash'intų, jei vartotojas įveda blogus duomenis (pvz., ne
# skaičių, kai tikimasi skaičiaus).
print(' - - - - 4. Užduoties Etapai - - - - - - - - ')
# Turite atlikti šiuos žingsnius:
# 1. Sukurti SQLite duomenų bazę su dviem lentelėmis (mokiniai, mokytojai).
# 2. Sukurti Asmuo, Mokinys, Mokytojas klases su atitinkamais atributais.
# 3. Parašyti funkcijas mokinių/mokytojų įterpimui, atnaujinimui, trynimui ir paieškai
# naudojant SQLite.
# 4. Sukurti iteratoriaus klasę, kuri leis peržiūrėti visus mokinius po vieną.
# 5. Sukurti dekoratorių, kuris prideda log' ą prieš kiekvieną DB operaciją.
# 6. Pridėti try-except bloką, kad būtų išvengta programos kritimų dėl blogos įvesties.
# 7. Testuoti programą su keliais įvesties scenarijais.
print('-' * 30)
import sqlite3

def sukurti_duomenu_baze():
    conn = sqlite3.connect('universitetas.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mokiniai (
            id INTEGER PRIMARY KEY,
            vardas TEXT NOT NULL,
            pavarde TEXT NOT NULL,
            klase TEXT,
            vidurkis REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mokytojai (
            id INTEGER PRIMARY KEY,
            vardas TEXT NOT NULL,
            pavarde TEXT NOT NULL,
            dalykas TEXT
        )
    """)

    conn.commit()
    conn.close()

sukurti_duomenu_baze()
print('-' * 30)

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis

class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas


class MokiniuIteratorius:
    def __init__(self, mokiniai):
        self.mokiniai = mokiniai
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.mokiniai):
            mokinys = self.mokiniai[self.index]
            self.index += 1
            return mokinys
        else:
            raise StopIteration

def log_dekoratorius(funkcija):
    def wrapper(*args, **kwargs):
        print('Vykdoma operacija...')
        return funkcija(*args, **kwargs)
    return wrapper

print('-' * 30)

@log_dekoratorius
def prideti_mokini(mokinys):
    try:
        with sqlite3.connect('universitetas.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM mokiniai WHERE vardas = ? AND pavarde = ?', (mokinys.vardas, mokinys.pavarde))
            if cursor.fetchone()[0] > 0:
                print('Toks mokinys jau egzistuoja.')
            else:
                cursor.execute('''
                    INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) 
                    VALUES (?, ?, ?, ?)
                ''', (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis))
                conn.commit()
    except sqlite3.Error as e:
        print(f'Klaida: {e}')




def prideti_mokytoja(mokytojas):
    try:
        conn = sqlite3.connect('universitetas.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO mokytojai (vardas, pavarde, dalykas)
            VALUES (?, ?, ?)
        """, (mokytojas.vardas, mokytojas.pavarde, mokytojas.dalykas))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f'Klaida: {e}')

def perziureti_visus_mokinius():
    conn = sqlite3.connect('universitetas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, vardas, pavarde, klase, vidurkis FROM mokiniai')
    mokiniai = cursor.fetchall()
    conn.close()

    if mokiniai:
        for row in mokiniai:
            print(f'ID: {row[0]} | Vardas: {row[1]} | Pavardė: {row[2]} | Klasė: {row[3]} | Vidurkis: {row[4]}')
    else:
        print('Mokinių sąrašas tuščias.')

def ieskoti_mokinio(vardas, pavarde):
    conn = sqlite3.connect('universitetas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, vardas, pavarde, klase, vidurkis FROM mokiniai WHERE vardas = ? AND pavarde = ?', (vardas, pavarde))
    mokiniai = cursor.fetchall()
    conn.close()

    if mokiniai:
        for row in mokiniai:
            print(f'ID: {row[0]} | Vardas: {row[1]} | Pavardė: {row[2]} | Klasė: {row[3]} | Vidurkis: {row[4]}')
    else:
        print('Mokinys nerastas.')

def atnaujinti_mokinio_klase(mokinys_id, nauja_klase):
    try:
        conn = sqlite3.connect('universitetas.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE mokiniai SET klase = ? WHERE id = ?
        """, (nauja_klase, mokinys_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f'Klaida: {e}')

def istrinti_mokini(mokinys_id):
    try:
        conn = sqlite3.connect('universitetas.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM mokiniai WHERE id = ?', (mokinys_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f'Klaida: {e}')

def pradinis_mokiniu_sarasas():
    mokiniai = [
        Mokinys(vardas='Jonas', pavarde='Jonaitis', klase='8A', vidurkis=8.5),
        Mokinys(vardas='Petras', pavarde='Petraitis', klase='9B', vidurkis=9.2),
        Mokinys(vardas='Ieva', pavarde='Ievaitė', klase='10C', vidurkis=7.8)
    ]
    for mokinys in mokiniai:
        prideti_mokini(mokinys)


def pasirinkti_veiksma():
    while True:
        print('\nMokyklos duomenų valdymo sistema')
        print('1. Pridėti mokinį')
        print('2. Pridėti mokytoją')
        print('3. Peržiūrėti visus mokinius')
        print('4. Ieškoti mokinio pagal vardą')
        print('5. Atnaujinti mokinio klasę')
        print('6. Ištrinti mokinį')
        print('7. Išeiti')

        pasirinkimas = input('Pasirinkite veiksmą: ')

        if pasirinkimas == '1':
            vardas = input('Mokinio vardas: ')
            pavarde = input('Mokinio pavardė: ')
            klase = input('Mokinio klasė: ')
            vidurkis = float(input('Mokinio vidurkis: '))
            mokinys = Mokinys(vardas, pavarde, klase, vidurkis)
            prideti_mokini(mokinys)

        elif pasirinkimas == '2':
            vardas = input('Mokytojo vardas: ')
            pavarde = input('Mokytojo pavardė: ')
            dalykas = input('Mokytojo dėstomas dalykas: ')
            mokytojas = Mokytojas(vardas, pavarde, dalykas)
            prideti_mokytoja(mokytojas)

        elif pasirinkimas == '3':
            perziureti_visus_mokinius()

        elif pasirinkimas == '4':
            vardas = input('Mokinio vardas: ')
            pavarde = input('Mokinio pavardė: ')
            ieskoti_mokinio(vardas, pavarde)

        elif pasirinkimas == '5':
            mokinys_id = int(input('Mokinio ID: '))
            nauja_klase = input('Nauja klasė: ')
            atnaujinti_mokinio_klase(mokinys_id, nauja_klase)

        elif pasirinkimas == '6':
            mokinys_id = int(input('Mokinio ID: '))
            istrinti_mokini(mokinys_id)

        elif pasirinkimas == '7':
            print('Išeinate...')
            break

        else:
            print('Neteisingas pasirinkimas. Bandykite vėl.')

sukurti_duomenu_baze()
pradinis_mokiniu_sarasas()

pasirinkti_veiksma()

def gauti_visus_mokinius():
    conn = sqlite3.connect('universitetas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, vardas, pavarde, klase, vidurkis FROM mokiniai')
    mokiniai = cursor.fetchall()
    conn.close()

    mokiniai_objektai = [Mokinys(vardas=row[1], pavarde=row[2], klase=row[3], vidurkis=row[4]) for row in mokiniai]
    return MokiniuIteratorius(mokiniai_objektai)

iteratorius = gauti_visus_mokinius()
for mokinys in iteratorius:
    print(f'{mokinys.vardas} {mokinys.pavarde}, Klasė: {mokinys.klase}, Vidurkis: {mokinys.vidurkis}')
print('-' * 30)



