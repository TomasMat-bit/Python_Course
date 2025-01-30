# # precision_digits = 2
# #
# # x = -
#
#
# skaiciai = [5, 1, 0, 100, 200]
# res = sorted(skaiciai)
# print(skaiciai) # [5, 1, 0, 100, 200]
# print(res) # [0, 1, 5, 100, 200]
# print('-----------------------')
# res = sorted(skaiciai, reverse=True) # Atvirksciai
# print(skaiciai) # [5, 1, 0, 100, 200]
# print(res) # [200, 100, 5, 1, 0]
#
# print('-----------------------')
#
# raides = ['a', 'c', 'b', 'e', 'd']
# print(raides) # ['a', 'c', 'b', 'e', 'd']
# res = sorted(raides)
# print(res) # ['a', 'b', 'c', 'd', 'e']
#
# # - -- - - - - -Symbolio numeracija - - - - -
# print(ord('a'))
# print(ord('b'))
# print(ord('c'))
# print(ord('d'))
# print(ord('e'))
# print(ord('7'))
# print(ord('6'))
# print('-----------------------')

# #  - - -- - - - lietuviskos raides sortinimas - - - - - - -
# import locale
# locale.setlocale(locale.LC_ALL, 'lt_LT')
# list_lt = ['Žemė', 'Ąžuolas', 'Vilnius']
# res = sorted(list_lt, key=locale.strxfrm)
# print(res)

# #  - - - - UZDUOTIS - - - - - -
#
# # round ir sorted funkcijos
# # Užduotis: Sukurkite programą, kuri:
# # • Duotų sąrašą skaičių, pvz., [1.234, 3.14159, 2.71828, 0.57721], ir apvalintų
# # kiekvieną iki 3 skaitmenų po kablelio.
#
# numb = [1.234, 3.14159, 2.71828, 0.57721]
# for elem in numb:
#     if  type(elem) == float:
#         print(round(elem, 3)) # 1.234 / 3.142 / 2.718 / 0.577
#
# # • Rikiuotų sąrašą su lietuviškais žodžiais, pvz., ["Žalgiris", "Ąžuolas",
# # "Lietuva", "Vilnius"], tinkama abėcėlės tvarka.
#
# import locale
# locale.setlocale(locale.LC_ALL, 'lt_LT')
# list_lt = ['Žalgiris', 'Ąžuolas', 'Lietuva', 'Vilnius']
# res = sorted(list_lt, key=locale.strxfrm)
# print(res)    # ['Ąžuolas', 'Lietuva', 'Vilnius', 'Žalgiris']
#
# # • Išrikiuotų skaičių sąrašą [10, 3, 7, 1, 15] mažėjimo tvarka ir jį atspausdintų.
#
# numb1 = [10, 3, 7, 1, 15]
# res = sorted(numb1)
# print(sorted(numb1, reverse=True)) #[15, 10, 7, 3, 1]
# print(res) # [1, 3, 7, 10, 15]



# # ------- - - - - - - - - -- ZODYNAI---------- - - - - - - - - - --------
#
# person_info = {
#     'name': 'Albert',
#     'surname': 'Einstein',
#     'languages': ['German', 'Latin', 'Italian', 'English'],
#     'occupation': {
#         'role': 'Professor',
#         'workplace': 'University of Berlin',
#         }
#     }
#
# for element in person_info: #name / surname / languages / occupation
#     print(element)
#
# for key, value in person_info.items():
#     print(f'key: {key} value: {value}')
# # key: name value: Albert
# # key: surname value: Einstein
# # key: languages value: ['German', 'Latin', 'Italian', 'English']
# # key: occupation value: {'role': 'Professor', 'workplace': 'University of Berlin'}
#
# for key, value in person_info.items():
#     if type(value) == dict:
#         for k, val in value.items():
#             print(f'key: {k} value: {val}')
# # key: role value: Professor
# # key: workplace value: University of Berlin
#
#
#
#
# print(person_info)
# print(type(person_info))
#
# print(person_info['name'])
# print(person_info['surname'])
# print(person_info['languages']) #['German', 'Latin', 'Italian', 'English']
# print(person_info['languages'][0]) # German
# print(person_info['languages'][1]) # Latin
#
# print(
#     person_info['occupation'] # {'role': 'Professor', 'workplace': 'University of Berlin'}
# )
# print(
#     person_info['occupation']['workplace'] # 'University of Berlin'
# )

# ------------- -------- ---- Uzduotys --------- ----------- ---------

# # 1. Žodyno sukūrimas ir duomenų pasiekimas
# # Užduotis 1:
# # Sukurkite programą, kuri:
# # 1. Sukurtų žodyną apie mokyklą, kuriame yra:
# # a. pavadinimas: mokyklos pavadinimas.
# # b. mokytojai: sąrašas žodynų apie mokytojus. Kiekvienas mokytojas turi:
# # i. vardas, pavardė, mokomas_dalykas.
# # c. mokinių_skaičius: mokinių skaičius.
# # 2. Atliktų šiuos veiksmus:
# # a. Išspausdintų pirmo mokytojo vardą ir mokomą dalyką.
# # b. Patikrintų, ar mokykloje yra daugiau nei 500 mokinių, ir atspausdintų atitinkamą žinutę.
# school_info = {
#     'name': 'Fast Track', # a. pavadinimas: mokyklos pavadinimas.
#     'teachers': {
#         'teacher1': { # b. mokytojai: sąrašas žodynų apie mokytojus. Kiekvienas mokytojas turi:
#             'name' : 'Antanas',# i. vardas, pavardė, mokomas_dalykas.
#             'surname' : 'Antanaitis',
#             'Mokomas dalykas' : 'Fizika'
#         },
#         'teacher2': {
#             'name' : 'Petras',
#             'surname' : 'Petraitis',
#             'Mokomas dalykas' : 'Matematika'
#         }
#         },
#     'students' : 700 # c. mokinių_skaičius: mokinių skaičius.
#     }
# print('Mokytojas: ' + school_info['teachers']['teacher1']['name'])# a. Išspausdintų pirmo mokytojo vardą ir mokomą dalyką.
# print('Mokomas dalykas: ' + school_info['teachers']['teacher1']['Mokomas dalykas'])# a. Išspausdintų pirmo mokytojo vardą ir mokomą dalyką.
#
# if school_info['students'] > 500:
#     print('mokykloje yra daugiau nei 500 mokinių')
# else: print('mokykloje yra maziau nei 500 mokinių')# b. Patikrintų, ar mokykloje yra daugiau nei 500 mokinių, ir atspausdintų
#
# # 2. Reikšmių pasiekimas pagal raktus
# # Užduotis 2:
# # Turite šį žodyną apie įmonės darbuotojus:
# company = {'name': 'TechCorp', 'employees':
#             [{'name': 'Jonas', 'role': 'Developer', 'salary': 3000 },
#             {'name': 'Asta','role': 'Designer', 'salary': 2500 },
#             {'name': 'Tomas', 'role': 'Manager', 'salary': 4000} ],
#             'location': 'Vilnius', 'industry': 'IT'
#             }
#
# # Atlikite šiuos veiksmus:
# # 1. Gaukite ir išspausdinkite visų darbuotojų vardus bei jų pareigas.
#
# for darbuotojas in company['employees']:
#     print(f'Darbuotojas: {darbuotojas["name"]}, Pareigos: {darbuotojas["role"]}')
#
# suma = 0
#
# # 2. Apskaičiuokite ir išspausdinkite visų darbuotojų atlyginimų vidurkį.
#
# for darbuotojas in company['employees']:
#     suma += darbuotojas['salary']
# average = suma/len(company['employees'])
# print(f'Algu vidurkis: {average}')
#
#
# # 3. Patikrinkite, ar žodyne yra raktas location. Jei yra, atspausdinkite jo reikšmę.
#
# if 'location' in company:
#     print('location')
#
# # 3. Iteracija per žodyną
#
# print(company.get('location'))
#
# # Užduotis 3:
# # Turite žodyną apie knygų biblioteką:
# library = { 'books': [ {'title': '1984', 'author': 'George Orwell', 'copies': 3},
#                        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'copies': 5},
#                        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'copies': 2} ],
#             'location': 'Kaunas', 'open_hours': {'start': '8:00', 'end': '20:00'} }
# # Atlikite šiuos veiksmus:
# # 1. Iteruokite per knygų sąrašą ir išspausdinkite knygos pavadinimą bei autorių.
#
# for info in library['books']:
#     print(f'Knygos pavadinimas: {info["title"]}, Autorius: {info["author"]}')
#
# # 2. Suraskite knygą su mažiausiai kopijų ir išspausdinkite jos pavadinimą.
# min_copies_book = library['books'][0]
# for book in library['books']:
#     if book['copies'] < min_copies_book['copies']:
#         min_copies_book = book
# print(f'Knyga su mažiausiai kopijų: {min_copies_book["title"]}')

# - - - - - -- sekanti diena - - - - - --Duomenų pašalinimas ir reikšmių keitimas

# marke = 'Audi'
# modelis = 'A6'
# auto = {}
# print(auto)
# if marke == 'Audi':
#     auto['marke'] = marke
# auto['modelis'] = modelis
# print(auto)
#
# auto['marke'] = 'BMW'
# auto['modelis'] = '5'
#
# auto['colors'] = ['red', 'white', 'black']
# print(auto)
#
# car_technical_characteristics = {
#     'engine' : 3.0,
#     'interior' : 'leather'
# }
#
# auto.update(car_technical_characteristics)
# auto.update({
#     'year' : 2026,
#     'eco2000' : True
# })
# print(auto)
#
# del auto['eco2000'] #{'marke': 'BMW', 'modelis': '5', 'colors': ['red', 'white', 'black'], 'engine': 3.0, 'interior': 'leather', 'year': 2026}
# print(auto)

# del auto['eco2000']
# interior = auto.pop('interior')
# print(f'interior: {interior}')
# print(auto)
# - - - -- - - - - UZDUOTYS - - - - - - - - -
from pprint import pprint
store = {
    "name": "E-Shop",
    "categories": ["Electronics", "Books", "Clothing"],
    "products": [
        {"name": "Laptop", "price": 1000, "stock": 10},
        {"name": "Book", "price": 20, "stock": 50},
        {"name": "T-shirt", "price": 15, "stock": 100}
    ],
    "rating": 4.5
}

pprint(store)
print('--------------------------------------------')
#1. Pasalinkite kategorija 'Clothing' is saraso kategoriju.
store['categories'].remove('Clothing')
pprint(store)
print('--------------------------------------------')
#2. Sumazinkite kiekvieno produkto kaina 5%, jei jo kaina yra didesne nei 50.
for product in store['products']:
    if product['price'] > 50:
        product['price'] *= 0.95
pprint(store['products'])
print('--------------------------------------------')

#3. Padidinkite produkto 'Laptop' sandelio kieki iki 15.
for product in store['products']:
    if product['name'] == 'Laptop':
        product['stock'] = 15
pprint(store['products'])
print('--------------------------------------------')

#4. Jei parduotuves ivertinimas (rating) yra mazesnis nei 4.6 padidinkite ji 0.1.

if store['rating'] < 4.6:
        store['rating'] += 0.1
pprint(store['rating'])
print('--------------------------------------------')

