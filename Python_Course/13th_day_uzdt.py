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

print('     ----     --     Užduotis 2   -----     ----       ')



