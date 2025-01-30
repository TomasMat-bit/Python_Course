#----------- - Paskaita: try-except – Exceptionų (klaidų) suvaldymas - - - - - - - - -
print(' - - - - - - -Pagrindinis try-except pavyzdys - - - -- - - - - - - - ')

ivestis = '4'
try:
    skaicius = int(ivestis)
    res = skaicius / 0  # šis veiksmas sukels klaidą
except Exception as e:
    print('Mes crashinom, tačiau suvaldėm crashą')
    print(e.__class__)  # išspausdina klaidos klasę
    print(e)  # išspausdina klaidos pranešimą

print("Programa tęsia darbą")


print(' - - - - - - -kitas pvz- - - -- - - - - - - - ')

produktai = '4'
produktu_skaicius ='0'
# 1 option
try:
    produktas = int(produktai)
    res = produktas / produktu_skaicius
except Exception as e:
    print('Mes crashinom, tačiau suvaldėm crashą')
    print(e.__class__)

print('Hello i am still working')

# print(' - - - - - - -Konkrečių klaidų (Exceptionų) gaudymas - - - -- - - - - - - - ')
#
# ivestis1 = input('Įveskite sveiką skaičių: ')
# ivestis2 = input('Įveskite daliklį: ')
#
# try:
#     skaicius = int(ivestis1)
#     daliklis = int(ivestis2)
#     res = skaicius / daliklis
#     print(f'Rezultatas: {res}')
# except ValueError:
#     print("Mes crashinom su ValueError")
#     print("Paleiskite programą išnaujo ir ivestis padarykit kad tai būtų sveikas skaičius")
# except ZeroDivisionError:
#     print("Mes crashinom su ZeroDivisionError")
#     print("Pakeiskite daliklį iš 0 į kitą")
#
# print("Programa tęsia darbą")

print(' - - - - - - Try-except-else-finally struktūra - - - -- - - - - - - - ')

try:
    res = 100 / 0
except ZeroDivisionError:
    print("Dalyba iš 0 negalima")
else: # vykdomas tik tada kai klaidos nera
    print(res)

# print(' - - - - - - Pavyzdys: Naudojant finally - - - -- - - - - - - - ')
#
# while True:
#     ivestis = input('Įveskite float skaičių: ')
#     try:
#         float_skaicius = float(ivestis)
#         print('Įvestis tinkama', float_skaicius)
#         break
#     except ValueError:
#         print("Įvestis NETINKAMA, pakartokite!!!")
#     finally:
#         print("Manęs niekaip neatsikratysit - FINALLY komanda")
#
# print("Programa tęsia darbą")
#
# def create_user(value: dict):
#     print('User created!')

users_to_create ={
    'user1': {'name', 'Darius' '123456789'},
    'user2': {'name', 'Darius' '123456789'},
    'user3': {'name', 'Darius' '123456789'},
    'user4': {'name', 'Darius' '123456789'}
}

# created_users = {}
# for key, value in user_to_create.items():
#     create_user(value)
#
#     try:
#         create_user(value)
#     except Exception as e:
#         print(e)
#     finally:
#         print('already created values was saved')

print(' - - - - - - raise – Klaidos sukūrimas - - - -- - - - - - - - ')

def sumuok_int_skaicius(sk1: int, sk2: int) -> int:
    if not (type(sk1) is int and type(sk2) is int):
        raise ValueError  # iššaukiame klaidą, jei argumentai nėra sveiki skaičiai
    return sk1 + sk2

res = sumuok_int_skaicius(4, 5)
print(res)

print(' - - - - - - programa show salary- - - -- - - - - - - - ')

current_user = 'Admin'
employee_salaries = {
    'Jim': 1000,
    'Tom': 2000,
}

def show_employee_salary(employee: str) -> int:
    if current_user not in ['Admin', 'Manager']:
        raise ValueError('You are not allowed')
    return employee_salaries[employee]

print(show_employee_salary('Jim'))

