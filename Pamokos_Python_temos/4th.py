#  ----- Sąlygos programoje, jų naudojimas su if  ------------------
from http.cookiejar import uppercase_escaped_char
from idlelib.window import add_windows_to_menu

# numb1 = 100
# numb2 = 500
# numb3 = 100
#
# print(numb1 < numb2)
# print(numb1 > numb2)
# print(numb1 == numb2)
# print(numb1 != numb2)
#
# print(numb1 >= numb2)
# print(numb1 <= numb2)
#-----------------------------------
# numb1 = 100
# numb2 = 500
# numb3 = 100
# a = numb1 == numb2
# print(a)
# print(type(a))
# print(type(a) is bool) # YES = TRUE
# print(type(numb1) is bool) # NO = FALSE
# print(type(numb1) is int) #YES = TRUE
#-------------------------------------------
# char = 'A'
# text = 'ABCD'
# text2 = 'QWER'

# print(
#     char in text
# )
# print(
#     char in text2
# )
#-----------------------------------------------
# name = 'Jonas'
# names_list = ['Donald', 'Darius', 'Ona']
#
# print(
#     name in names_list
# )

#-----------UZDUOTIS-----------------------------------------

# # 1. Parašykite programą, kuri leidžia vartotojui įvesti du skaičius ir patikrina, kuris iš jų
# # yra didesnis.
#
# a = 110
# b = 215
# print(a < b)
# print(a > b)
#
# # 2. Sukurkite sąlygą, kuri patikrina, ar įvestas skaičius yra lyginis ar nelyginis,
# # naudodami operatorių %.
# print('--------------')
# print(a % 2 == 0) #lyginis ar ne
# print(b % 2 == 0)
#
# # 3. Sukurkite sąrašą ir naudodami in operatorių patikrinkite, ar vartotojo įvestas žodis
# # yra šiame sąraše
# print('--------------')
# name = 'Jonas'
# names_list = ['Donald', 'Darius', 'Ona']
# names_list2 = ['Donald', 'Darius', 'Jonas']
#
# print(
#     name in names_list
# )
# print(
#     name in names_list2
# )
# #---- O TUREJO BUTI TAIP::: DOWN-----
#
# a = int(input('Skaicius 1: '))
# b = int(input('Skaicius 2: '))
# zodis = input("Įveskite žodį: ")
# zodziai = ['labas', 'kaip', 'sekasi']
# print(a > b)
# print(a % 2 == 0)
# print(zodis in zodziai)

#--------------- IF statement---------------------------------------------

# numb1 = 100
# numb2 = 500
# numb3 = 300
#
# if numb1 < numb2:
#     print(f'{numb1} yra mazesnis uz {numb2}')
# else:
#     print('else')
#
# if numb1 > numb2:
#     print(f'{numb1} yra mazesnis uz {numb2}')
# else:
#     print('else')
#
# if numb2 > numb3 < numb1:
#     print(f'{numb1} yra mazesnis uz {numb2}')
# else:
#     print('else')

#--------3 UZDUOTELE------------

# # 1.Parašykite programą, kuri tikrina vartotojo įvestą amžių:
#
# a = 18
# user_age= int(input('Iveskite Amziu: '))
#
# # a. Jei amžius mažesnis nei 18, spausdina „Nepilnametis“.
# # b. Jei amžius didesnis arba lygus 18, spausdina „Pilnametis“.
# if user_age < a:
#     print("Nepilnametis")
# if user_age >= a:
#     print("Pilnametis")


# # 2. Sukurkite programą, kuri leidžia vartotojui įvesti temperatūrą ir patikrina:
# # a. Jei temperatūra mažesnė už 0, spausdina „Šalta“.
# # b. Jei temperatūra tarp 0 ir 20, spausdina „Vidutiniška“.
# # c. Jei temperatūra viršija 20, spausdina „Šilta“
#
# temperatures = int(input('Iveskite temperatura: '))
# if temperatures < 0:
#     print('Salta')
# if 20 <= temperatures >= 0:
#     print('Vidutiniska')
# if temperatures > 20:
#     print('Silta')
#--------kitoks variantas-----------
# temperatures = int(input('Iveskite temperatura: '))
# if temperatures < 0:
#     print('Salta')
# elif 20 <= temperatures >= 0:
#     print('Vidutiniska')
# else:
#     print('Silta')

# numb1 = 100
# numb2 = 500
#
# if numb1 > numb2:
#     print(f'{numb1} yra didesnis uz {numb2}')
# elif numb1 == numb2:
#     print(f'{numb1} yra toks pat kaip {numb2}')
# else:
#     print(f'{numb1} yra mazesnis ir nelygus {numb2}')

# -------- 4 UZDUOTELE-------------------------------------
# 1. Parašykite programą, kuri patikrina vartotojo įvestą balą:
# a.Jei balas tarp 0–4, spausdina „Nepatenkinamas“.
# b.Jei balas tarp 5–7, spausdina „Vidutinis“.
# c.Jei balas tarp 8–10, spausdina „Puikus“.
# points = int(input('Iveskite balus: '))
# if  0 <= points <= 4:
#     print('Nepatenkinamas')
# elif 5 <= points <= 7:
#     print('Vidutinis')
# elif 8 <= points <= 10:
#     print('Puikus')
# else:
#     print('Nera tokio balo')

# # # 2. Sukurkite programą, kuri leidžia vartotojui įvesti metų laiką
# # # (pvz., „Žiema“, „Pavasaris“).
# # #Priklausomai nuo įvesto laiko, spausdinkite atitinkamus mėnesius.
# #
# yearTime = input('Pasirinkite metu laika pvz. „Ziema“, „Pavasaris“, „Vasara“, „Ruduo“: ')
# if yearTime == 'Ziema':
#     print('Gruodis, Sausis, Vasaris')
# elif yearTime == 'Pavasaris':
#     print('Kovas, Balandis, Geguze')
# elif yearTime == 'Vasara':
#     print('Birzelis, Liepa, Rugpjutis')
# elif yearTime == 'Ruduo':
#     print('Rugsejis, Spalis, Lapkritis')
# else:
#     print('Nera tokio metu laiko')
# Kitas sprendimo variantas-----------------------:






#--------------------------------kita tema-------------------------------

# numb1 = 100
# numb2 = 500
# numb3 = 100
#
# if numb1 < numb2 and numb1 == 100:
#     print('True')
#
# if numb1 < numb2 or numb1 == 500: # jei tinka nors viena salyga  - true - ir sukasi toliau
#     print('True')
#
# if not 100 > 500:
#     print('True')

# employee = ''
# if numb1 > 1000:
#     employee = 'Adomas'
# elif numb1 > 2000:
#     employee = 'John'



# auto = 'Audi'
# autos_ger = ['BMW', 'Audi', 'Mercedes']
# autos_it = ['Ferrari', 'Fiat', 'Alfa']
# autos_sport = ['BMW', 'Ferrari']
#
# if (auto in autos_ger or auto in autos_it) and auto in autos_sport:
#     print(f'{auto} yra vokiskas-sportinis arba italiskas-sportiskas')
#
# # ----------- 5 UZDUOTIS----------------
#
# # 1. Sukurkite programą, kuri leidžia vartotojui įvesti du skaičius ir tikrina:
# # a. Ar abu skaičiai yra teigiami.
# # b. Ar bent vienas iš jų yra neigiamas.
#
# a = int(input('Skaicius 1: '))
# b = int(input('Skaicius 2: '))
#
# if a < 0 and b < 0:
#      print('Abu skaiciai yra neigiami')
# if a > 0 and b > 0:
#      print('Abu skaiciai yra Teigiami')
#
# if a < 0 < b:
#      print('Pirmas skaicius yra neigiamas, antras yra teigimas')
# if a > 0 > b:
#      print('Pirmas skaicius yra teigiamas, antras yra neigimas')
#
# # 2. Sukurkite programą, kuri leidžia vartotojui įvesti automobilio markę ir modelį.
#
# user_car = input('Iveskite marke: ')
# user_model = input('Iveskite modeli: ')
# car = ['BMW', 'Audi', 'Aprilia']
# carModel = ['M3', 'RS6', 'Pegaso']
# # Patikrinkite:
# # a. Ar markė yra iš sąrašo „vokiškų“ automobilių (pvz., „BMW“, „Audi“).
# if user_car in car:
#     print(f'selecteted {user_car} is iin the list')
# else:
#     print(f'choise {user_car} is not in the list')
#
# if user_model in carModel:
#     print(f'selection {user_model} is in the list')
# else:
#     print(f'selection {user_model} is not the list')
#
# # b. Ar modelis yra sportinis pagal sąrašą (pvz., „M3“, „RS6“).
#
# # /////////  IF INTEGRACIJA /////////////////////
#
# numb4 = 9
# result = ''
# if numb4 % 2 == 0:
#     result = 'lygus'
# else:
#     result = 'nelygus'
# print(result)
# print('-------------------------------')
# numb4 = 9
# result = 'lygus' if numb4 % 2 == 0 else 'nelygus'
# print(result)

# ///////////// 'lygus' jei True, kitu atveju 'nelygus'////////////

# # //////    UZDUOTIS   ////////
# #   SUTRUMPINTAS IF SAKINYS
#
# # Parašykite programą, kuri leidžia vartotojui įvesti skaičių ir nustato, ar skaičius yra
# # teigiamas ar neigiamas, naudodami vieną eilutę.
#
#
# print('teigiamas' if float(input('Iveskite skaiciu: ')) > 0 else 'neigiamas')

# ///////// Kita tema: /////////

miestas1 = 'Vilnius'
miestas2 = 'Kaunas'

# print(miestas1.istitle())
# if miestas1.title():
#     print('Vartotojas ivede miesto pavadinima')

# print(miestas2.isupper())

print(miestas1.startswith('V'))
print(miestas2.startswith('V'))


asmens_kodas = '3563663795320408'
user_gender = 'Vyras'

if asmens_kodas.startswith('3'):
    user_gender = 'Vyras'
elif asmens_kodas.startswith('4'):
    user_gender = 'Moteris'
else:
    print('Neteisingas A.K.')

    # Sukurkite programą, kuri tikrina vartotojo įvestą simbolių eilutę. Jei eilutė prasideda
    # didžiąja raide, spausdina „Didžioji raidė“, kitu atveju – „Mažoji raidė“

city = input('Iveskite miesto pavadinima: ')

if city.istitle():
    print('Didzioji raide')
else:
    print('Mažoji raidė')
eilute = input('Įveskite sakinį/simbolį: ')
ar_prasideda_didz = 'Didžioji raidė' if eilute.istitle() else 'Mažoji raidė'
print(ar_prasideda_didz)

print('Didžioji raidė' if input('Įveskite sakinį/simbolį: ').istitle() else 'Mažoji raidė')


# 6. Metodai, grąžinantys True arba False
# 1. Sukurkite programą, kuri leidžia vartotojui įvesti žodį ir tikrina:
# a. Ar žodis prasideda didžiąja raide.
# b. Ar visi žodžio simboliai yra mažosios raidės.

print('Didzioji raide' if input('iveskites sakini/simboli: ').istitle() else )
# Task 1
zodis = input('Įveskite žodį: ') # vilnius
ar_prasideda_didz = zodis.istitle()

ar_mazosios = zodis.islower() # True
ar_mazosios = not zodis.isupper() # True

print(f'Žodis prasideda didžiąja raide: {ar_prasideda_didz}')
print(f'Visi žodžio simboliai yra mažosios raidės: {ar_mazosios}')

# 2. Parašykite programą, kuri leidžia vartotojui įvesti sakinio eilutę ir:
# a. Tikrina, ar eilutė prasideda tam tikru simboliu (pvz., „A“).


# b. Tikrina, ar eilutė yra parašyta tik didžiosiomis raidėmis.


# Task 1-2


# Task 2
eilute = input('Įveskite sakinį: ')
ar_prasideda_A = eilute.startswith('A')
ar_didziosios = eilute.isupper()
print(f'Eilutė prasideda simboliu „A“: {ar_prasideda_A}')
print(f'Eilutė parašyta tik didžiosiomis raidėmis: {ar_didziosios}')
