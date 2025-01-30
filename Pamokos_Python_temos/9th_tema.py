# # Funkcijų paskirtis
#
# # def <mūsų sugalvotas funkcijos pavadinimas> (): - skliausteliuose, funkcijos priimamasis
# def say_hello():
#     print("Hello world!!!")
#     print("Funkcija atsisveikina")
#
# # def aukščiau yra tik paruoštas vykdymui kodas,
# # realiai jis įvykdomas, parašius funkcijos iškvietimą
# say_hello()
#
# # bandymas įsidėti funkcijos darbo rezultatą į kintamąjį
# res = say_hello()  # į res įrašoma None, nes mūsų funkcijoje neaprašytas duomenų atidavimas iš funkcijos
# print(res)  # None
#----------------------------------------------------
# #-------------- Argumentai ir return reikšmės --------------------------------------
#
# def create_greetings(user):
#     if not user:
#         return
#     res = f'Greetings, {user}!'
#     return res
# name = 'Tomas'
# greetings = create_greetings(name)
# if greetings:
#     print(greetings)
# else:
#     print('User not found!')
#----------------------------------------------------
#-------------- Funkcijos su keliais argumentais --------------------------------------

def greet(name='user'):
    print(f'Hello, {name}!')
greet('Tomas')
greet()


print('---------------------------------------------------------')

def say_hello_to2(name1, name2):
    hello_string = f"Hello to {name1} and hello to {name2}"
    return hello_string

res = say_hello_to2("Ramūnas", "Adomas")
print(res)
print('---------------------------------------------------------')

def priimk_pacienta(pacientas, gydytojas='gud. Pagalnutylenis'):
    irasas_gyd_zurnale = f'Pacientas {pacientas}, prieme {gydytojas}'
    return irasas_gyd_zurnale

res = priimk_pacienta('Adomas')
print(res)

res = priimk_pacienta('Rolandas')
print(res)

res = priimk_pacienta('Adomas', gydytojas='gyd. Pakeitenis')
print(res)

print('---------------------------------------------------------')

#-------------- Numatytosios reikšmės ir keyword argumentai --------------------------------------

def greet(name="Drauge"):
    print(f"Hello, {name}!")

greet()  # Hello, Drauge!
greet("Ramūnas")  # Hello, Ramūnas!

print('-------------------------Loginiai jungikliai funkcijose--------------------------------')

#-------------- Loginiai jungikliai funkcijose --------------------------------------

def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
    if not iki_sveiko_sk:
        return sk1 / sk2
    return sk1 // sk2

print(dalink_spec(777, 5, True))

print('---------------------------------------------------------')

# def modify_product(product, inform_client=False):
#     if inform_client:
#         return res
#     print('Product was succesfuly modifyed by system!')
#     return product * 50
#
# button_modify_product('tapkes')
print('---------------------------------------------------------')

#-------------- Docstringai funkcijose --------------------------------------

def say_hello(name):
    """
    Priima vardą ir atspausdina pasisveikinimą.
    :param name: str - vardas žmogaus
    :return: None
    """
    print(f"Hello, {name}")

#-------------- Type hints ir anotacijos --------------------------------------

# def add(x: int, y: int) -> int:
#     return x + y
#
# res = add("10", 10)  # bus rodomas įspėjimas del ''. Turi buti integeris


def add(x: int, y:int) -> int:
     return x + y

a = 1 + add(1, 3)

add(1, 9)

# Apibendrinimas: Type hints naudojimas nurodo funkcijos argumentų ir
# grąžinamų duomenų tipus, padedant programuotojams aiškiau suprasti,
# kokie duomenys turėtų būti perduodami funkcijoms ir kokio tipo
# rezultatai bus grąžinami.

