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
print(data_laikas_1)

data_2 = datetime.date(2023, 1, 1)
print('Antras datetime objektas (be laiko):', data_2)

# # #      ---------     DESTYTOJO KODAS:        --------
#
# # 1
# liepos_15 = datetime.datetime(1995, 7, 14, 15, 30)
# print(liepos_15)
# dt_without_time = datetime.datetime(2023, 1, 1)
# print(dt_without_time)

print('     ----     --     Užduotis 3   -----     ----       ')

# 3. Laiko skirtumo tarp datų skaičiavimas
# Užduotis 3:
# 1. Apskaičiuokite, kiek dienų praėjo nuo 2000-01-01 iki šiandienos.
# 2. Išveskite rezultatą tokia forma:
# "Praėjo <dienų skaičius> dienų nuo 2000-01-01."

data_start = datetime.date(2000, 1, 1)
data_today = datetime.date.today()
skirtumas = data_today - data_start
print(f'Praėjo {skirtumas.days} dienų nuo 2000-01-01.')

# #      ---------     DESTYTOJO KODAS:        --------
# # 2
# dt_today = datetime.datetime.today()
# metai_2000 = datetime.datetime(2000, 1, 1)
# print(f'Praėjo {(dt_today - metai_2000).days} dienų nuo 2000-01-01.')

print('     ----     --     Užduotis 5   -----     ----       ')

# # 5. Datos ir laiko įvedimas naudojant str formatą
# # Užduotis 5:
# # Paprašykite vartotojo įvesti datą formatu "YYYY-MM-DD".
# # Konvertuokite įvestą tekstą į datetime objektą naudojant strptime().
# # Išveskite datą datetime formatu.
#
# data_input = input('Įveskite datą formatu "YYYY-MM-DD": ')
# data_object = datetime.datetime.strptime(data_input, '%Y-%m-%d')
# print(f'datetime formatu: {data_object}')
# #------------- MOKYTOJO KODAS;
#
# while True:
#     try:
#         data_obj = datetime.strptime(ivesta_data, "%Y-%m-%d")
#         print("Įvesta data datetime formatu:", data_obj)
#         break
#     except ValueError:
#         print("Neteisingas datos formatas. Prašome įvesti datą teisingu formatu.")
#
# data_laikas = datetime(2022, 12, 31, 23, 59, 59)
#


print('     ----     --     Užduotis 6   -----     ----       ')

# # 6. Datos ir laiko išvedimas naudojant strftime formatą
# # Užduotis 6:
# # Sukurkite datetime objektą: 2022-12-31, 23:59:59.
# # Naudodami strftime(), suformatuokite ir išveskite:
# # "31/12/2022 23:59:59"
# # "2022 metų gruodžio 31 diena"

# from datetime import datetime
#
# data_laikas = datetime(2022, 12, 31, 23, 59, 59)
#
# ivesta_data = input("Įveskite datą formatu 'YYYY-MM-DD': ")
#
# formatted_1 = data_laikas.strftime("%d/%m/%Y %H:%M:%S")
# print(formatted_1)
#
# menesiai = {
#     1: "sausio", 2: "vasario", 3: "kovo", 4: "balandžio",
#     5: "gegužės", 6: "birželio", 7: "liepos", 8: "rugpjūčio",
#     9: "rugsėjo", 10: "spalio", 11: "lapkričio", 12: "gruodžio"
# }
#
# formatted_2 = f"{data_laikas.year} metų {menesiai[data_laikas.month]} {data_laikas.day} diena"
# print(formatted_2)

print('     ----     --     Užduotis 7   -----     ----       ')

# 7. Laiko skirtumo (timedelta) objekto gavimas atliekant datų atimtį
# Užduotis 7:
# 1. Sukurkite dvi datas:
# a. 2023-01-01
# b. 2024-01-01
# 2. Apskaičiuokite laiko skirtumą tarp jų naudojant - operatorių.
# 3. Išveskite rezultatą dienomis.

dt_first = datetime.datetime(2024, 1, 1)
dt_second = datetime.datetime(2023, 1, 1)
print(f'Praėjo {(dt_first - dt_second).days} dienų nuo 2023-01-01.')

print('     ----     --     Užduotis 8   -----     ----       ')

# 8. Skaičiavimai su timedelta objektais
# Užduotis 8:
# 1. Sukurkite programą, kuri:
# a. Naudoja dabartinę datą.
# b. Prideda 90 dienų naudojant timedelta.
# 2. Išveskite rezultatą:
# "Data po 90 dienų bus: <data>"

dabar = datetime.datetime.today()
print(dabar)
skirtumas = datetime.timedelta(days=90)
print(skirtumas)
res = dabar + skirtumas
print(res)

print('     ----     --     Užduotis 9   -----     ----       ')

# 9. timedelta objekto laukų prieiga
# Užduotis 9:
# 1. Apskaičiuokite skirtumą tarp 2000-01-01 ir šiandienos.
# 2. Išveskite:
# a. Dienų skaičių
# b. Valandų skaičių (naudojant .seconds)
# c. Bendrą sekundžių skaičių (.total_seconds())

#1.a
dt_from = datetime.datetime(2000, 1, 1)
dt_dabar = datetime.datetime.today()
print(f'Skirtumas {(dt_dabar - dt_from).days} dienų nuo 2000-01-01.')

skirtumas = datetime.timedelta(days=1000, hours=100, minutes=100)

print(f'Skirtumas {(dt_dabar - dt_from).seconds} sekundes nuo 2000-01-01.')
print(f'Skirtumas {(dt_dabar - dt_from).total_seconds()} bondros sekundes nuo 2000-01-01.')

