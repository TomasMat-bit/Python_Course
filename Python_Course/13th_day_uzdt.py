import datetime
dt_res = datetime.datetime.today()
print(dt_res)

print('     ----     --     Užduotis 1   -----     ----       ')

# 1. Atskiri datos-laiko laukai iš datetime objekto
# Užduotis 1:
# 1. Sukurkite programą, kuri:
# a. Naudoja datetime.datetime.today() dabartinės datos ir laiko gavimui.
# b. Išveda šiuos laukus: metai, mėnuo, diena, valanda, minutė, sekundė.
# 2. Išveskite pranešimą:
# "Dabar yra <valanda>:<minutė>, <diena>-<mėnuo>-<metai>"

import datetime
dt_res = datetime.datetime.today()

metai = dt_res.year
print(metai)
menesiai = dt_res.month
print(menesiai)
diena = dt_res.day
print(diena)
valanda = dt_res.hour
print(valanda)
minute = dt_res.minute
print(minute)
sekunde = dt_res.second
print(sekunde)

print(f'Dabar yra {valanda}:{minute}, {diena}-{menesiai}-{metai}')

# Mokytojo kodas
# # 1. A
# import datetime
#
# dt_res = datetime.datetime.today()
#
# # 1. B
# print(dt_res.year)
# print(dt_res.month)
# print(dt_res.day)
# print(dt_res.hour)
# print(dt_res.minute)
# print(dt_res.second)
#
# # 2
# print(f'Dabar yra <{dt_res.hour}>:<{dt_res.minute}>, <{dt_res.day}>-<{dt_res.month}>-<{dt_res.year}>')

print('     ----     --     Užduotis 2   -----     ----       ')

# 2. Norimos datos ir laiko objekto sukūrimas
# Užduotis 2:
# 1. Sukurkite datetime objektą, kuris atitinka datą: 1995 m. liepos 14 d., 15:30:00.
# 2. Išveskite šią datą ir laiką.
# 3. Sukurkite antrą datetime objektą tik su data: 2023-01-01 (be laiko).

import datetime

data_laikas_1 = datetime.datetime(1995, 7, 14, 15, 30, 0)
print('Pirmas datetime objektas:', data_laikas_1)

data_2 = datetime.date(2023, 1, 1)
print('Antras datetime objektas (be laiko):', data_2)

print('     ----     --     Užduotis 3   -----     ----       ')

# 3. Laiko skirtumo tarp datų skaičiavimas
# Užduotis 3:
# 1. Apskaičiuokite, kiek dienų praėjo nuo 2000-01-01 iki šiandienos.
# 2. Išveskite rezultatą tokia forma:
# "Praėjo <dienų skaičius> dienų nuo 2000-01-01."

data_start = datetime.date(2000, 1, 1)
data_today = datetime.date.today()
skirtumas = data_today - data_start
print(f"Praėjo {skirtumas.days} dienų nuo 2000-01-01.")

print('     ----     --     Užduotis 4   -----     ----       ')




