# #  - - - - - - - -- Paskaita: Funkcijos – pažangi dalis
# #  - - - - - - - - -*args naudojimas funkcijose - - - - - - -
#
# def print_args(*args):
#     print(args)
#     print(type(args))
#
# print_args('Adomas', 'sausis', 1000)
# print('------------- Funkcija su daugybe vardų --------------------------------------')
# def give_hello_to_names(*args):
#     res = ''
#     for name in args:
#         res += f'Hello, {name}!\n'
#     return res
#
# print(give_hello_to_names('Tomas', 'Adomas', 'Valdas'))
# print('-----------------Argumentų derinimas su *args------------------------------')
#
# def multiply_all_by_numb(numb, *args):
#     for elem in args:
#         print(numb * elem)
#
# multiply_all_by_numb(1, 2, 3, 4, 5)
# print('---------------Pavyzdys realiam gyvenime------------------------------------')
#
# def take_order(customer_name, *args):
#     """
#     Takes a restaurant order with multiple food items.
#
#     :param customer_name: str
#     :param args: food items
#     :return: None
#     """
#
#     print(f'Order for {customer_name}')
#     for i in args:
#         print(f'- {i}')
#     print('Thank You for your order!')
#
# take_order('Tomas', 'Pizza', 'Burger', 'Sausages', 'Milk shake')
#
# print('---------------Kelių argumentų tipų derinimas ------------------------------------')
#
# def multiply_all_by_numb(numb, *args, text="* DAUGYBA"):
#     for elem in args:
#         print(f"{elem * numb} {text}")
#
# multiply_all_by_numb(7, 10, 11, 50)
# multiply_all_by_numb(7, 10, 11, 50, text="***")
#
# # # Printinama:
# #
# # 70 * DAUGYBA
# # 77 * DAUGYBA
# # 350 * DAUGYBA
# # 70 ***
# # 77 ***
# # 350 ***
#
# print('---------------Rezultatų grąžinimas naudojant *args ------------------------------------')
#
# def return_list_of_multiplied_numbs(numb, *args, info=False):
#     multiplied_numbs = [elem * numb for elem in args]
#     if info:
#         print(f"daugiklis: {numb}, args: {args}, rezultatas: {multiplied_numbs}")
#     return multiplied_numbs
#
# res = return_list_of_multiplied_numbs(7, 10, 11, 50)
# print(res)  # [70, 77, 350]
#
# res = return_list_of_multiplied_numbs(3, 10, 11, 50, info=True)  # daugiklis yra: 3 *args yra: (10, 11, 50) rezultatas yra: [30, 33, 150]
# print(res)  # [30, 33, 150]
# print('--------------- ------------------------------------')
#
# def check_type_of_args(*args: (int, float)):
#     for arg in args:
#         print(type(arg))
#
# check_type_of_args(1, '2', '58', 99.99) # tipu patikrinimai
# print('--------------- ------------------------------------')
# def check_file_type(file: (bytes, str)):
#     print(type(file)) # tipu patikrinimai
#
# # print('---------------**kwargs mechanizmas ------------------------------------')
# #
# # def print_kwargs(**kwargs):  # ** - pakavimas į žodyną, kintamajame kwargs
# #     print(kwargs)
# #     print(type(kwargs))
# #
# # print_kwargs(pirmas=1, antras=2)  # {'pirmas': 1, 'antras': 2} <class 'dict'>
# #
# 
# # def print_list(listas, skirtukas=' ', eilutes_pabaiga='\n'):
# #     for elem in listas:
# #         print(elem, 'men.', sep=skirtukas, end=eilutes_pabaiga)
# #
# # listas_duom = ['sausis', 'vasaris', 'kovas']
# # print_list(listas_duom)
# # print_list(listas_duom, skirtukas='|||', eilutes_pabaiga='***\n')
# #  KITAS VARIANTAS
#
# listas_duom = ['sausis', 'vasaris', 'kovas']
# def print_list(listas, **kwargs):
#     for elem in listas:
#         print(elem, 'men.', kwargs)
#
# print_list(listas_duom, sep='>>>', end='---')


print('----------Nereikalingų argumentų sugėrimas naudojant **K W A R G S ------------------------------------')

def kelk_laipsniu(sk, laipsnis=2, **kwargs):
    res = sk ** laipsnis
    return res

print(kelk_laipsniu(2, laipsnis=3, radianas=2))
# radianas yra nenumatytas parametras, jį sugeria kwargs
print('-------------------------------- ------------------------------------')

print('---------------Lambda funkcijos ir rūšiavimas ------------------------------------')

darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

# Rūšiavimas pagal pirmąjį elementą (vardą) – numatytoji rūšiavimo tvarka
res = sorted(darbuotojai)
print(res)

print('--------------- Rūšiavimas naudojant paprastą funkciją------------------------------------')

def grazink_index_1(listas):
    return listas[1]  # grąžina profesiją
res = sorted(darbuotojai, key=grazink_index_1)
print(res)

print('--------------- Rūšiavimas naudojant lambda funkciją------------------------------------')

 # rūšiavimas pagal atlyginimą
res = sorted(darbuotojai, key=lambda listas: listas[-1])

print(res)

# #pavyzdukas   NEVEIKIA
#
# def sudeti(a, b, c, d):
#     return a + b
# print(sudeti(3, 5))
#
# sudeti_lambda = lambda a, b, c, d: a+ b
# print(sudeti_lambda(3, 5, 1, 1))


print('---------------filtravimo pvz--------------------')
skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lyginiai_skaiciai = list(filter(lambda x: x % 2 == 0, skaiciai))
print(lyginiai_skaiciai)




