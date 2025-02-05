# Galutinė Užduotis: Knygų Bibliotekos Sistema
# Šioje užduotyje naudosime viską, ką išmokome šiame pokalbyje: klases, metodus, sąrašų
# valdymą, paveldimumą, datetime modulį, try-except, *args, **kwargs, ir dar daugiau.
print('- Užduotis: Sukurkite paprastą bibliotekos valdymo sistemą - ')

# • Sukurti dvi klases: Book ir Library.
# • Naudoti datetime modulį knygų paskolos laikotarpiams valdyti.
# • Naudoti *args ir **kwargs knygų filtravimui.
# • Naudoti try-except klaidų valdymui.

# 2. Žingsniai:
print('- - - - - - - - - --  ŽINGSNIS 1: Sukurkite klasę Book- - - - - - - - - - - - - - ')

# ŽINGSNIS 1: Sukurkite klasę Book
# • Laukai:
# o title (pavadinimas)
# o author (autorius)
# o year (išleidimo metai)
# o available (ar knyga prieinama) – pagal nutylėjimą True
# • Metodai:
# o __str__ – grąžina informaciją apie knygą gražiu formatu.
# o is_classic() – grąžina True, jei knyga išleista daugiau nei prieš 50 metų.

import datetime

class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        availability = 'Prieinama. ' if self.available else 'Neprieinama. '
        return f'Knyga: {self.title}\nAutorius: {self.author}\nIšleidimo metai: {self.year}\nStatusas: {availability}'

    def is_classic(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year > 50

# ŽINGSNIS 2: Sukurkite klasę Library
# • Laukai:
# o books (sąrašas, kuriame saugomos knygos)
# • Metodai:o add_book(book) – prideda naują Book objektą į biblioteką.
# o display_books() – atvaizduoja visas knygas bibliotekoje.
# o borrow_book(title) – leidžia pasiskolinti knygą, jei ji prieinama.
# ▪ Naudoti try-except, kad suvaldytumėte klaidas (pvz., jei knygos
# nėra).
# o return_book(title) – leidžia grąžinti knygą.
# o filter_books(*args, **kwargs) – leidžia filtruoti knygas pagal autorių,
# metus ar pavadinimą.
# ▪ Pvz.: filter_books(author="Jonas") arba
# filter_books(year=2000)







# ŽINGSNIS 3: Naudokite datetime paskolos valdymui
# • Kai vartotojas pasiskolina knygą, įrašykite paskolos datą.
# • Pridėkite metodą due_date(), kuris grąžins datą, kada knyga turi būti grąžinta
# (pvz., po 14 dienų).
# ŽINGSNIS 4: Sukurkite sąveiką su vartotoju
# • Naudokite while ciklą, kad vartotojas galėtų:
# o Pridėti naują knygą į biblioteką.
# o Peržiūrėti visą bibliotekos knygų sąrašą.
# o Pasiskolinti knygą.
# o Grąžinti knygą.
# o Filtruoti knygas pagal autorių, metus ar pavadinimą.
# o Išeiti iš programos.
# 3. Papildomos Sąlygos:
# • Naudokite try-except klaidoms suvaldyti, pvz., neteisingai įvedus metus.
# • Naudokite *args ir **kwargs knygų filtravimui pagal skirtingus kriterijus.