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

print(' - - - - - Uzduotis 7 - - - - - - - -')

# 7. Importai iš mūsų sukurto modulio
# Užduotis 7:
# 1. Sukurkite naują Python failą matematika.py.
# 2. Šiame faile parašykite funkcijas:
# a. sudetis(a, b), kuri grąžina dviejų skaičių sumą.
# b. daugyba(a, b), kuri grąžina dviejų skaičių sandaugą.
# 3. Sukurkite kitą Python failą main.py, kuris importuoja šias funkcijas ir jas iškviečia.

from mylib import matematika as mtk, matematika, matematika as m

res = mtk.sumuok(2, 9)
print(res) #atsakymas - 11

res = mtk.daugink(11, 7)
print(res) #atsakymas - 77


print(' - - - - - Uzduotis 8 - - - - - - - -')

# 8. Visas modulio importavimas
# Užduotis 8:
# 1. Sukurkite Python programą, kuri importuoja matematika modulį (sukurtą
# ankstesnėje užduotyje).
# 2. Naudoja matematika.sudetis(10, 20) ir matematika.daugyba(5, 4).
# 3. Išspausdina rezultatus.

res = matematika.sumuok(13, 17)
print(res) #atsakymas - 30

res = matematika.daugink(5, 15)
print(res) #atsakymas - 75

print(' - - - - - Uzduotis 9 - - - - - - - -')

# 9. Specifinių funkcijų importavimas
# Užduotis 9:
# 1. Naudodami from matematika import sudetis, daugyba, importuokite tik tas
# funkcijas, kurios reikalingos.
# 2. Paskaičiuokite sumą ir sandaugą skaičių 8 ir 3.
# 3. Išspausdinkite rezultatus.

res = matematika.sumuok(8, 3), matematika.daugink(8, 3)
print(res) #atsakymas - 11, 24

print(' - - - - - Uzduotis 10 - - - - - - - -')

# 10. Modulio trumpinimas naudojant alias
# Užduotis 10:
# 1. Importuokite matematika modulį kaip m.
# 2. Naudokite m.sudetis(12, 18) ir m.daugyba(7, 6).
# 3. Išspausdinkite rezultatus.

res = m.sumuok(12, 18)
print(res) #atsakymas - 30
res = m.daugink(7, 6)
print(res)#atsakymas - 42
#kitas variantas
print(m.sumuok(12, 18))
print(m.daugink(8, 3))

