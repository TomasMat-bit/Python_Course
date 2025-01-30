# # ---------------1st task --------------------------------------
#
# # sukuriam tuščią sąrašą
# sarasas = []
# print(type(sarasas))  # <class 'list'>
# print(sarasas)  # []
#
# # duomenys kuriais pildysim tuščią sąrašą
# men1 = "sausis"
# men2 = "vasaris"
# number = 2024
#
# # .append() prijungia naują elementą į sąrašo pabaigą
# sarasas.append(men1)
# print(sarasas)  # ['sausis']
#
# sarasas.append(men2)
# print(sarasas)  # ['sausis', 'vasaris']
#
# sarasas.append(2024)
# print(sarasas)  # ['sausis', 'vasaris', 'kovas', 2024]
# from http.cookiejar import month
# from unittest.util import safe_repr

# #a = []
# print(type(a))
# a.append('sausis')
# print(a)
# a.append('vasaris')
# print(a)
# a.append(2024)
# print(a)


#
# # -------------------2nd Task-----------------------------------------------
# # 2. Sąrašų metodai
# # 1. Sukurkite sąrašą su elementais: "šuo", "katė", "zuikis".
# # a. Pridėkite elementą "dramblys" į pabaigą.
# # b. Įdėkite elementą "žirafa" į antrąją poziciją.
# # 2. Pašalinkite pirmą pasitaikiusį "katė" reikšmę iš sąrašo.
# # 3. Naudokite pop() metodą, kad pašalintumėte ir išsaugotumėte paskutinį elementą.
# # 4. Naudokite indeksus, kad pakeistumėte pirmąjį sąrašo elementą į "tigrai".
#
# sarasas = []
# print(type(sarasas))
# print(sarasas)
#
# animal1 = "suo"
# animal2 = "kate"
# animal3 = "zuikis"
# # .apend()
# sarasas.append(animal1)
# print(sarasas)
#
# sarasas.append(animal2)
# print(sarasas)
#
# sarasas.append(animal3)
# print(sarasas)
#
# sarasas.append("dramblys")
# print(sarasas)
#
# #insert


# Task 2
# b = ['suo', 'kate', 'zuikis']
# b.append('dramblys')
# b.insert(2, 'zirafa')
# b.remove('kate')
# print(b)
# last_element = b.pop(-1)
# print(last_element)
#
# b[0] = 'tigrai'
# print(b)
#
#
# b.append(['a', 'b', 'c'])
# print(b)
# b.extend(['a', 'b', 'c'])
# print(b)


# print('KITA TEMA')

#------------SARASU ITERAVIMAS----------------
# menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']
#
# for element in menesiai:
#     print(element)
#     print(element.upper())
#
# skaiciai = [10, 7, 50, 111]
#
# for elem in skaiciai:
#     print(elem * 100)
#
# print('---------------------')
#
# sum = 0
# for elem in skaiciai:
#     sum += elem
#
# print(sum)


#UZDUOTYS:---------------------
# # ----------------------------3rd TASK ---------------
# #Sukurkite sąrašą su mėnesiais: ["sausis", "vasaris", "kovas",
# # "balandis"].
# # Naudokite for ciklą, kad atspausdintumėte kiekvieną mėnesį su prierašu "
# # mėnuo"
#
# menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']
#
#
# for element in menesiai:
#     print('Menuo ' + element)
#     print(f'Menuo {element}')
#
# # ----------------------------4th TASK ---------------
# # Sukurkite sąrašą su skaičiais: [5, 10, 15, 20].
# skaiciai = [5, 10, 15, 20]
#
# # Suskaičiuokite visų skaičių sumą ir atspausdinkite ją.
# sum = 0
# for elem in skaiciai:
#     sum += elem
#
# print(sum)
#
# # Padauginkite kiekvieną skaičių iš 2 ir išveskite rezultatą.
#
# for elem in skaiciai:
#     print(elem * 2)
#
# print('---------------------')
#
# #------------------------------------------------------------------
#
# skaiciai = [10, 5, 50, 111]
# tuscias = []
#
# #len - listo ilgis, elementu skaicius
# print(len(skaiciai))
# print(len(tuscias))
#
# stringas = 'ABC'
# print(len(stringas))
#
# #sum - elementu suma
#
# print(sum(skaiciai))
# print(sum(tuscias))
# # print(sum(stringas)) neveikai ne flow ir ne 'integer'
#
# # max - didziausias skaicius masyve
# print(max(skaiciai))
#
# # min - maziausias skaicius masyve
# print(min(skaiciai))
#
# # -------- UZDUOTIS------------
#
# # Sukurkite sąrašą su skaičiais: [3, 8, 12, 5, 10].
#
# skaiciai = [3, 8, 12, 5, 10]
#
# # a. Naudokite len(), kad sužinotumėte elementų skaičių.
#
# print(len(skaiciai))
#
# # b. Naudokite sum(), kad suskaičiuotumėte visų elementų sumą.
#
# print(sum(skaiciai))
#
# # c. Naudokite max() ir min(), kad nustatytumėte didžiausią ir mažiausią
# # skaičių
#
# print(max(skaiciai))
# print(min(skaiciai))

# ------------------------------------------------------------------------------------

# month = ['sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis']
#
# #indeksavimas
# print(month[0])
# print(month[2])
# print(month[-1])
#
# print('-----------------------------------')
#
# #slice
# print(month[1:4])
# print(month[1:3 + 1])
# print(month[1:])
# print(month[:5])
#
# print('-----------------------------------')
#
# #zingsniai
# print(month[::3])
# print(month[::-1])
# print(month[::-2])


# month = ['sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis']
#
# print(month[4][1:5:2])
# print(month[4].upper())
# print(month[4].upper()[1:5:2])
#
# # # -------------------- UZDUOTIS---------------------------
#
# # Sukurkite sąrašą: ["Lietuva", "Latvija", "Estija", "Lenkija"].
# # • Atspausdinkite pirmą ir paskutinį sąrašo elementus.
# # • Naudokite pjaustymą, kad gautumėte sąrašą su viduriniais elementais.
# # • Atspausdinkite sąrašą atvirkštine tvarka
#
# countries = ['Lietuva', 'Latvija', 'Estija', 'Lenkija']
# print(countries[0])
# print(countries[-1])
# print(countries[-1:0])
# print(countries[1:-1])
# print(countries[::-1])

#-------------TUPLE SAVYBES------------------------------------------------------------------------------
#
# months = ('sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis')
# print(id(months))
#
# # print(months[1])
# # print(months[2])
# # print(months[-1])
# #
# # print(months[1:3])
# # print(months[3:5])
#
# print(months.index('kovas'))
# print(id(months))
#
# # print(type(months))
#
# # for elem in months: 1rs
# #     print(elem)
# #---------TASK --------------
#
# # Sukurkite tuple: ("pirmadienis", "antradienis", "trečiadienis", "ketvirtadienis").
#
# weekdays = ('pirmadienis', 'antradienis', 'treciadienis', 'ketvirtadienis', 'penktadienis')
# print(weekdays)
# # • Atspausdinkite antrą elementą.
#
# print(weekdays[1])
#
# # • Naudokite .count() ir .index() metodus, kad sužinotumėte, kiek kartų yra
# # "pirmadienis" ir jo indeksą.
#
# print(weekdays.index('pirmadienis'))
# print(weekdays.count('pirmadienis'))

# -----------------------Sąrašai sąrašuose-------------------------//////////////
#
# darbuotojai = [
#     ['Valdas', 'programuotojas', 2000],
#     ['Adomas', 'direktorius', 3000],
#     ['Aldona', 'vadybininkas', 1800],
#     ['Jogaila', 'programuotojas', 2500]
# ]
#
# print(darbuotojai[0])  # ['Valdas', 'programuotojas', 2000]
# print(darbuotojai[0][1])  # programuotojas
# print(darbuotojai[0][1].upper())  # PROGRAMUOTOJAS
#
# # printinam po 1 vidinį pilną listą
# for listas in darbuotojai:
#     print(listas)  # ['Valdas', 'programuotojas', 2000],
#
# # printinam atskirus elementus iš kiekvieno vidinio listo
# # imdami per indeksą
# for listas in darbuotojai:
#     print(listas[0], listas[2])  # Valdas programuotojas, ..
#
# # python priimta yra išardyti listus for eilutėje
# for vardas, pareigos, atlyginimas in darbuotojai:
#     print(atlyginimas, vardas, pareigos)  # Valdas 2000 programuotojas, ..
#
# # susumuojam atlyginimus
# # variantas 1
# suma = 0
# for vardas, pareigos, atlyginimas in darbuotojai:
#     suma += atlyginimas
#
# print(suma)  # 9300
#
# # variantas 2
# atlyginimai = []  # tuščias listas, sukaupti visiems atlyginimams
# for vardas, pareigos, atlyginimas in darbuotojai:
#     atlyginimai.append(atlyginimas)
#
# print(atlyginimai)  # [2000, 3000, 1800, 2500]
# print(sum(atlyginimai))  # 9300
#
# # suskaičiuojam programuotojus
# pozicijos = []
# for vardas, pareigos, atlyginimas in darbuotojai:
#     pozicijos.append(pareigos)
#
# print(pozicijos)  # ['programuotojas', 'direktorius', 'vadybininkas', 'programuotojas']
# print("Programuotojų skaičius yra", pozicijos.count("programuotojas"))  # Programuotojų skaičius yra 2

# TODO perdaryti, kad atlyginimų fondas ir programuotojai būtų suskaičiuoti naudojant 1 for ciklą


# #--------------------STRING METODAI----------------------------------
# months_str = "sausis vasaris kovas"  # str
# print(months_str)  # sausis vasaris kovas  # sausis vasaris kovas
#
# # str metodas .split() - padalina str į listą
# # per nurodytą simbolį
# months_list = months_str.split(" ")
# print(months_list)  # ['sausis', 'vasaris', 'kovas']
#
# # months_list = months_str.split("a")
# # print(months_list)  # ['s', 'usis v', 's', 'ris kov', 's']
#
# # str metodas .join() - sujungia stringų dalis į vieną stringą
# # naudodamas skirtuką
# joined_str = " ".join(months_list)
# print(joined_str)  # sausis vasaris kovas
#
# joined_str = "---".join(months_list)
# print(joined_str)  # sausis---vasaris---kovas
#
# #------------------------UZDUOTIS---------------------UP------------
# # 1. Naudokite eilutę "obuolys bananai kriaušės".
#
# fruits_str = "obuolys bananai kriaušės"  # str
# print(fruits_str)
#
# # a. Paverskite ją sąrašu, naudodami .split() metodą.
#
# fruits_list = fruits_str.split(" ")
# print(fruits_list)
#
# # b. Naudodami .join(), sujunkite sąrašo elementus į vieną eilutę su
# # skiriamąja linija ---.
#
# fruits_str = " ".join(fruits_list)
# print(joined_str)
