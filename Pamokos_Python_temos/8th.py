# # - - - - - - -  - List Comprehensions naudojimas - - - - - -
# from pyexpat.errors import messages
#
# kaupiklis = []
# duomenu_listas = [1, 10, 2, 20, 3, 30, 4, 40]
#
# for elem in duomenu_listas:
#     kaupiklis.append(elem)
#
# print(kaupiklis)  # [1, 10, 2, 20, 3, 30, 4, 40]
#
# # tas pats rezultatas, naudojant list comprehension
# kaupiklis2 = [elem for elem in duomenu_listas]
# print(kaupiklis2)  # [1, 10, 2, 20, 3, 30, 4, 40]
# print( ' ------------------------------------ ')
# # - - - - - - -  - Operacijų atlikimas naudojant list comprehension - - - -
#
# # visi seno listo skaičiai sudauginami iš 9
# print(duomenu_listas)
# kaupiklis3 = [elem * 9 for elem in duomenu_listas]
# print(kaupiklis3)  # [9, 90, 18, 180, 27, 270, 36, 360]
#
# # visi seno listo skaičiai pakelti kvadratu
# kaupiklis4 = [elem ** 2 for elem in duomenu_listas]
# print(kaupiklis4)  # [1, 100, 4, 400, 9, 900, 16, 1600]
# print( ' ------------------------------------ ')
# print( ' -----------1 uzduotis--------------- ')
# # - - - - - - - UZDUOTYS ------ - - - - - -
# # 1. List Comprehensions naudojimas
# # Užduotis 1:
# # Turite sąrašą skaičių [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# # 1. Naudodami list comprehension, sukurkite naują sąrašą, kuriame
# # būtų visi elementai padvigubinti.
# # 2. Sukurkite sąrašą, kuriame būtų visi pradinio sąrašo elementai
# # pakelti kvadratu.
# # 2. Operacijų atlikimas naudojant list comprehension
# kauptukas = []
# numb_listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(numb_listas)
# kauptukas1 = [elem * 2 for elem in numb_listas]
# print(kauptukas1)
# kauptukas2 = [elem ** 2 for elem in numb_listas]
# print(kauptukas2)
# print( ' ------------Kitokoks sprendimas ------------------------ ')
# skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# padvigubinti = [x * 2 for x in skaiciai]
# print("Padvigubinti skaičiai:", padvigubinti)
#
# kvadratu = [x ** 2 for x in skaiciai]
# print("Pakelta kvadratu:", kvadratu)
#
# print( ' -----------2 uzduotis--------------- ')
#
# # Užduotis 2:
# # Turite sąrašą kainų eurais: [10, 15, 20, 25, 30].
# # 1. Naudodami list comprehension, konvertuokite visas kainas į
# # dolerius, pritaikant kursą 1 EUR = 1.1 USD.
# # 2. Sukurkite sąrašą su pranešimais, pvz., „Kaina: 10 EUR“, „
# # Kaina: 15 EUR“ ir t.t.
#
# eurai = [10, 15, 20, 25, 30]
# doreliai = [round(eur * 1.1, 1) for eur in eurai]
# print(doreliai)
#
# message = [f'Kaina: {eur} EUR' for eur in eurai]
# print(message)
# print( ' ----------Kitokoks sprendimas-------------------------- ')
# kainos_eurais = [10, 15, 20, 25, 30]
#
# kursas = 1.1
# kainos_doleriais = [round(kaina * kursas, 2) for kaina in kainos_eurais]
# print("Kainos doleriais:", kainos_doleriais)
#
# pranesimai = [f"Kaina: {kaina} EUR" for kaina in kainos_eurais]
# print("Pranešimai:", pranesimai)
# print( ' ------------------------------------ ')

# # Duomenų filtravimas naudojant list comprehension
# kaupiklis = []
# duomenu_listas = [1, 10, 2, 20, 3, 30, 4, 40]
# # struktūra [skaicius, skaicius kvadratu]
# kaupiklis5 = [[elem, elem ** 2] for elem in duomenu_listas]
# print(kaupiklis5)  # [[1, 1], [10, 100], [2, 4],.. , [4, 16], [40, 1600]]
#
# # Vidinės struktūros sudarymas naudojant list comprehension
#
# kaupiklis6 = [[elem, elem ** 2, elem ** 3] for elem in duomenu_listas]
# print(kaupiklis6)   # [[1, 1, 1], [10, 100, 1000], [2, 4, 8],.. , [4, 16, 64], [40, 1600, 64000]]
#
#
# #Duomenų filtravimas naudojant list comprehension
#
# listas = [1, 10, 2, 20, 3, 30, 4, 40, 99]
#
# # išfiltruojam, kad gautume elementus tik mažesnius už 10
# res = [elem for elem in listas if elem < 10]
# print(res)  # [1, 2, 3, 4]
# print( ' ------------------------------------ ')
# # - - - - - - - -  U Z D U O T Y S - - - - - -
# # 3. Vidinės struktūros sudarymas naudojant list comprehension
# # Užduotis 3: Sukurkite sąrašą, kuriame yra šių
# # skaičių [1, 2, 3, 4, 5] informacija:
# # 1. Kiekvienas elementas turi būti sąrašas, kuriame yra:
# # pats skaičius, jo kvadratas ir kubas.
# # 2. Pvz.: [1, 1, 1], [2, 4, 8].
# # 3. Papildykite struktūrą taip, kad kiekvienas vidinis
# # sąrašas turėtų dar vieną elementą – informaciją, ar skaičius yra lyginis (True/False).
# # 4. Duomenų filtravimas naudojant list comprehension
# duomenu_sarasas = [1, 2, 3, 4, 5]
# print(duomenu_sarasas)
# pakelimas_laipsniu = [[elem, elem ** 2, elem ** 3,  elem % 2 == 0] for elem in duomenu_sarasas]
# print(pakelimas_laipsniu) # + True ir False
# print( ' ------------------------------------ ')
# # Užduotis 4:
# # Turite sąrašą skaičių [5, 8, 12, 18, 25, 30, 35, 40].
# # 1. Sukurkite naują sąrašą, kuriame būtų tik skaičiai
# # didesni nei 20.
# # 2. Sukurkite sąrašą, kuriame būtų tik tie skaičiai,
# # kurie dalijasi iš 5.
# # 3. Sukurkite sąrašą su reikšmėmis „Lyginis“ arba
# # „Nelyginis“, atitinkamai kiekvienam pradiniam sąrašo skaičiui.
# stock_on = [5, 8, 12, 18, 25, 30, 35, 40]
# print(stock_on)
# res = [elem for elem in stock_on if elem > 20]
# print(res)  # [25, 30, 35, 40]
# res = [elem for elem in stock_on if not elem % 5]
# print(res) # [5, 25, 30, 35, 40]
# lyginis_nelyginis = [f'{x}: {"Lyginis" if x % 2 == 0 else "Nelyginis"}' for x in stock_on]
# print("Lyginis arba Nelyginis:", lyginis_nelyginis)

# - - - - - - KITA TEMA ---------
# Sudėtingas list comprehension su keliais for ir sąlyginiais sakiniais

raides = ['A', 'B', 'C']
skaiciai = ['1', '2', '3', '4']

res = [raid + sk for raid in raides for sk in skaiciai]
print(res)  # ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4']
res = [raid + sk for raid in raides for sk in skaiciai if int(sk) % 2 == 0]
print(res) # ['A2', 'A4', 'B2', 'B4', 'C2', 'C4']
print( ' ------------------------------------ ')
# - - - - - -- - -  - - - - ----- - --------- -------- ------------ - -----


# - - - - Comprehension naudojimas su kitomis duomenų struktūromis - - -


listas = [0, 0, 5, 2, 3, 3, 3]

# tuple comprehension
tuple_res = tuple(elem for elem in listas)
print(tuple_res)  # (0, 0, 5, 2, 3, 3, 3)

# dict comprehension
dict_res = {elem: elem ** 2 for elem in listas}
print(dict_res)  # {0: 0, 5: 25, 2: 4, 3: 9}

# set comprehension - - - Pasalina duplikatus - -
set_res = {elem for elem in listas}
print(set_res)  # {0, 2, 3, 5}

set_res = {elem for elem in listas}
set_res.add(4) # prideda nauja norima skaiciu
print(set_res)  # {0, 2, 3, 4, 5}


 # - - -       - - - - -  U Z D U O T Y S - - - - - -


# 5. Sudėtingas list comprehension su keliais for ir sąlyginiais sakiniais
# Užduotis 5:
# Turite sąrašus:
# • Raidės: ['A', 'B', 'C']
# • Skaičiai: [1, 2, 3]
# 1. Sukurkite sąrašą, kuriame kiekviena raidė derinama su kiekvienu skaičiumi.
# Pvz.: ['A1', 'A2', 'A3', 'B1', ...].
# 2. Sukurkite sąrašą, kuriame derinamos tik tos raidės ir skaičiai, kurių suma (raidės
# indeksas + skaičius) yra didesnė nei 3.
# 3. Sukurkite sąrašą, kuriame derinami tik lyginiai skaičiai su mažosiomis raidėmis.

raides = ['A', 'B', 'C']
skaiciai = ['1', '2', '3']
res = [raid + sk for raid in raides for sk in skaiciai]
print(res)
res = [raid + sk for raid in raides for sk in skaiciai if raides.index(raid) + int(sk) > 3]
print(res)

lower_leters = [raid.lower() + sk for raid in raides for sk in skaiciai if not int(sk) % 2]
print(lower_leters)


# 6. Comprehension naudojimas su kitomis duomenų struktūromis
# Užduotis 6:
# Turite sąrašą: [1, 2, 3, 2, 1, 4, 5, 5].
# 1. Naudodami set comprehension, sukurkite aibę, kurioje yra tik unikalios reikšmės.
# 2. Naudodami tuple comprehension, sukurkite tuple, kuriame yra visos reikšmės
# padidintos vienetu.
# 3. Naudodami dict comprehension, sukurkite žodyną, kurio raktai yra skaičiai, o
# reikšmės – jų kvadratai.

# Task 6
# Given list
skaiciai = [1, 2, 3, 2, 1, 4, 5, 5]

# 1. Create a set containing only unique values
unikalus = {x for x in skaiciai}
print("Unikalios reikšmės (aibė):", unikalus)

# 2. Create a tuple with all values incremented by 1
tuple_pakeistas = tuple(x + 1 for x in skaiciai)
print("Padidintos reikšmės (tuple):", tuple_pakeistas)

# 3. Create a dictionary where keys are numbers, and values are their squares
kvadratai = {x: x ** 2 for x in skaiciai}
print("Žodynas su kvadratais:", kvadratai)

