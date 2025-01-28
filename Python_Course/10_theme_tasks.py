print(' - - - - - Uzduotis 2 - - - - - - - -')

# Paprastas importavimas
# Užduotis 2:
# Sukurkite Python programą, kuri importuoja random modulį ir:
# 1. Sugeneruoja atsitiktinį skaičių nuo 1 iki 100.
# 2. Sugeneruoja atsitiktinį skaičių su uniform(), kuris yra tarp 1 ir 50.
# 3. Išspausdina abu rezultatus.

import random

print(random.randint(1, 100))
print(round(random.uniform(1, 50), 2))

print(' - - - - - Uzduotis 3 - - - - - - - -')

# 3. Specifinių funkcijų importavimas
# Užduotis 3:
# Sukurkite Python programą, kuri naudoja:
# 1. from random import randint, choice
# 2. Sugeneruoja atsitiktinį skaičių nuo 1 iki 10 naudojant randint().
# 3. Pasirenka atsitiktinį elementą iš sąrašo ['obuolys', 'bananas', 'kriaušė',
# 'vyšnia'] naudodama choice().
# 4. Išspausdina abu rezultatus.

from random import randint, choice
generate_random_number = randint(1, 10)
print(generate_random_number)

select_random_fruit = choice(['obuolys', 'bananas', 'kriaušė', 'vyšnia'])
print(select_random_fruit)

print(' - - - - - Uzduotis 4 - - - - - - - -')

# 4. Modulio trumpinimas naudojant alias
# Užduotis 4:
# Sukurkite Python programą, kuri:
# 1. Importuoja datetime modulį su alias dt.
# 2. Naudoja dt.datetime.now() funkciją, kad gautų dabartinę datą ir laiką.
# 3. Išspausdina rezultatą su formatu: Dabartinė data ir laikas: YYYY-MM-DD
# HH:MM:SS

import datetime as dt
print(f'Dabartinė data ir laikas: {dt.datetime.now()}')
print(f"Dabartinė data ir laikas: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


print(' - - - - - Uzduotis 5 - - - - - - - -')

# 5. Specifinių funkcijų importavimas su alias
# Užduotis 5:
# Sukurkite Python programą, kuri:
# 1. Importuoja sqrt funkciją iš math modulio su alias sq.
# 2. Apskaičiuoja kvadratinę šaknį iš 625 naudojant sq().
# 3. Išspausdina rezultatą.

from math import sqrt as sq
print(sq(625)) #atsakymas - 25.0

print(' - - - - - Uzduotis 6 - - - - - - - -')

# 6. Visko importavimas iš modulio (nerekomenduojamas būdas)
# Užduotis 6:
# 1. Sukurkite Python programą, kuri naudoja from math import *.
# 2. Apskaičiuoja sinusą iš 90 laipsnių (naudojant sin()).
# 3. Išspausdina rezultatą.
# 4. Parašykite komentaruose, kodėl šis metodas gali būti pavojingas dideliuose
# projektuose.

from math import *
print(sin(90)) #atsakymas - 0.8939966636005579


