from xml.dom.minidom import ProcessingInstruction

# user_name = input('Please write Your name: ')

# print(f'hello, {user_name}!')

# text = 'ABCcba123'
# sarasas_tuple = ('1', '2', '3')
# res = len(text) # length
# print(res)
# print(len(sarasas_list))

# sarasas_skaiciu = [12, 15, 18, 20, 60, 1]

#print(sum(sarasas_skaiciu))
# print(max(sarasas_skaiciu))
# print(min(sarasas_skaiciu))


# res = 0
# for i in sarasas_skaiciu:
#     res += i
# print(res)

# print(type(res))

# print(
#     bool(0.1)
# )

# # 1. Python integruotos funkcijos: Pagrindai Užduotis:
# #    Sukurkite programą, kuri:
# # • Paprašytų vartotojo įvesti savo vardą ir amžių naudojant input.
#
# user = input('Iveskite savo Varda: ')
# user_age = int(input('Iveskite savo amziu: '))
# # • Išspausdintų sveikinimo žinutę, pvz., „Sveikas, Jonas! Tau 25 metai.“
#
# print(f'Sveikas, {user}! Tau {user_age} metai. ')
# # • Paskaičiuotų, kiek simbolių sudaro vartotojo vardas, ir išspausdintų
# # šią informaciją.
# name_lenght = len(user)
# print(f'Jusu varda sudaro {name_lenght} simboliai')
#
# # • Patikrinkite, ar amžius didesnis nei 18, ir atitinkamai spausdinkite
# # „Pilnametis“ arba „Nepilnametis“.
# if user_age <= 18:
#     print(f' {user} Nepilnametis')
# if user_age >= 18:
#     print(f' {user} Pilnametis')

# ------ FUNKCIJA RANGE --------------

# for skaicius in range(1, 6):
#     print(skaicius)
#
# vardu_sarasas = ['Darius', 'Tomas', 'Audrius', 'Antanas']
# lyginiu_vardu_sarasas = []
# for skaicius in range(len(vardu_sarasas)):
#     if skaicius % 2:
#         lyginiu_vardu_sarasas.append(vardu_sarasas[skaicius])
#     print(lyginiu_vardu_sarasas)


# print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]


# # ----------------  RANGE funkcija -----------------------
# # Užduotis: Sukurkite programą, kuri:
# # • Atspausdintų visus lyginius skaičius nuo 1 iki 20 naudojant range.
#
# print(list(range(0, 21, 2))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# for skaicius in range(2, 21, 2):
#     print(skaicius)
#     print('--------------------')
# # • Atliktų šių skaičių kvadratų sumą ir ją išspausdintų.
# # skaicius in range(1, 21)
#
# suma = sum(skaicius ** 2 for skaicius in range(2, 21, 2))
# print(f'suma: {suma}')
# print('--------------------')
# print(', '.join((str(x) for x in lyginiai_skaiciai)))
# lyginiai_skaiciai_str = []
# for skaiciai in lyginiai_skaiciai:
#     lyginiai_skaiciai_str.append(str(skaicius))
# print(', '.join(lyginiai_skaiciai_str))
# print('--------------------')
#
# # • Panaudotų range, kad sukurtų skaičių seką nuo 10 iki 1 (atvirkštine tvarka) ir juos
# # atspausdintų
#
# print(list(range(11, 0, -1)))
# print('--------------------')

# ------------- F_JA PRINT -----------------------------------------

# print(
#     'A', 'B', 'C', 'D', 'E', sep='|' #A|B|C|D|E
# )
#
# print(
#     'TASK2', end='LABAS' #TASK2LABASA B C D E
# )
#
# print(
#     'A B C D E', sep='|'
# )
#
# print(
#     f'{"A"} {"B"} {"C"} {"D"} {"E"}', sep='|' #A B C D E
# )

# listas = ['abc', 123, True]
#
# for elem in listas:
#     if type(elem) == str:
#         print(elem.upper())
#     elif type(elem) == int:
#         print(elem % 2)
#     elif type(elem) == bool:
#         print('Verification passed!')


# # 3. print funkcija su parametrais
# # Užduotis: Sukurkite programą, kuri:
# # • Išspausdintų sąrašą žodžių (['Obuolys', 'Kriaušė', 'Bananas',
# # 'Vyšnia']), atskirdama juos simboliu „|“.
#
# print(
#     'Obuolys', 'Kriaušė', 'Bananas', 'Vyšnia' '.', sep='|'
# )
# print('--------------------')
# # • Naudojant print, suformuotų tokį rezultatą vienoje eilutėje: „1) Obuolys, 2)
# # Kriaušė, 3) Bananas, 4) Vyšnia“.
#
# print(
#     '1)Kriaušė, 2)Kriaušė, 3)Bananas, 4)Vyšnia.', sep='|'
# )
# print('--------------------')
# # • Panaudotų end parametrą, kad išspausdintų kelias eilutes vienoje konsolės
# # eilutėje.
#
# print(
#     '1)Kriaušė, 2)Kriaušė,', end='Bananas'
# )
# print(
#     '1)Kriaušė, 2)Kriaušė, 3)Bananas, 4)Vyšnia.', sep='|'
# )
# print('--------------------')



# 4. type funkcija ir tipų patikra
# Užduotis: Sukurkite programą, kuri:
# • Priimtų sąrašą įvairių tipų duomenų, pvz., [123, 'Labas', True, 45.6, None].

sarasas = [123, 'Labas', True, 45.6, None] # int, str, bool, flat.

for elem in sarasas:
    if type(elem) == str:
        print(elem.upper())
    elif type(elem) == int:
        print(elem % 2)
    elif type(elem) == float:
        print(elem / 2)
    elif type(elem) == bool:
        print('Verification passed!')


# • Naudodama type, patikrintų kiekvieno elemento tipą ir atliktų šiuos veiksmus:
# o Jei tai sveikasis skaičius (int), padaugintų jį iš 10.

for elem in sarasas:
    if type(elem) == int:
        print(elem % 2 * 10)

# o Jei tai eilutė (str), išspausdintų didžiosiomis raidėmis.

for elem in sarasas:
    if type(elem) == str:
        print(elem.upper())

# o Jei tai bool, atspausdintų „True arba False aptikta“.

for elem in sarasas:
    if  type(elem) == bool:
        print('TRUE')

# o Jei tai float, apvalintų iki dviejų skaičių po kablelio.

for elem in sarasas:
    if  type(elem) == float:
        print(elem % 2,round(2))

# • Išspausdintų visus apdorotus rezultatus.