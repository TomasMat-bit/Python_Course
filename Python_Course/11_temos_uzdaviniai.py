print('--------------- Užduotis 2 ------------------------------------')

# *args naudojimas funkcijose
# Užduotis 2:
# Parašykite funkciją sudeti_skaicius(), kuri priimtų neribotą kiekį skaičių kaip
# argumentus ir grąžintų jų sumą.
# 1. Iškvieskite funkciją su (5, 10, 15).
# 2. Iškvieskite funkciją su (100, 200, 300, 400).

def sudeti_skaicius(*args):
    return sum(args)
print(sudeti_skaicius(5, 10, 15))
print(sudeti_skaicius(100, 200, 300, 400))

print('--------------- Užduotis 3 ------------------------------------')

# Funkcija su daugybe vardų
# Užduotis 3:
# Parašykite funkciją sveikinti_vardus(*args), kuri priimtų kelis vardus ir grąžintų žinutę
# su pasisveikinimu kiekvienam vardui.
# Pvz.: sveikinti_vardus("Jonas", "Asta", "Mantas")

def sveikinti_vardus(*args):
    res = ''
    for i in args:
        res += f'Labas, {i}!\n'
    return res

print(sveikinti_vardus('Jonas', 'Asta', 'Mantas'))

print('--------------- Užduotis 4 ------------------------------------')

# Argumentų derinimas su *args
# Užduotis 4:
# Parašykite funkciją pakelti_laipsniu(n, *args), kuri priimtų
# pagrindinį skaičių n ir keletą kitų skaičių, kuriuos reikia pakelti n
# laipsniu.

def pakelti_laipsniu(n, *args):
    return [i ** n for i in args]
print(pakelti_laipsniu(3, 5, 3, 9))

print('--------------- Užduotis 5 ------------------------------------')

# Kelių argumentų tipų derinimas
# Užduotis 5:
# Sukurkite funkciją spausdinti_zinutes(kartai, *args, pabaiga="!"), kuri
# pakartotų kiekvieną perduotą žinutę kartai kartų, o pabaigoje pridėtų pabaiga reikšmę.
# Rezultatų grąžinimas naudojant *args
#  Detytojo kodas-------------------------DOWN -----------------

def spausdinti_zinutes(kartai: int, *args: str, pabaiga: str="!") -> None:
    for zinute in args:
        print((zinute + " ") * kartai + pabaiga)

spausdinti_zinutes(3, "Labas", "Pasauli", pabaiga="!!!")

print('--------------- Užduotis 6 ------------------------------------')

# Užduotis 6:
# Sukurkite funkciją dauginti_skaicius(n, *args), kuri priimtų skaičių n ir kitus
# skaičius *args, padaugintų kiekvieną iš n, o rezultatą grąžintų kaip sąrašą.
#  Detytojo kodas-------------------------DOWN -----------------
def dauginti_skaicius(n: int, *args: int) -> list:
    return [skaicius * n for skaicius in args]

rezultatas = dauginti_skaicius(2, 1, 3, 5, 7)
print(rezultatas)

print('--------------- Užduotis 7 ------------------------------------')

# Įvadas į **kwargs
# Užduotis 7:
# Parašykite funkciją rodyti_duomenis(**kwargs), kuri išspausdintų visus perduotus
# vardinius argumentus raktu ir reikšme.
# **kwargs su numatytaisiais argumentais

def rodyti_duomenis(**kwargs):
    for raktas in kwargs.items():
        print(f'{raktas}')
rodyti_duomenis(vardas='Tomas', Amzius=34, Trauma='Miniskas')
# ('vardas', 'Tomas')
# ('Amzius', 34)
# ('Trauma', 'Miniskas')

print('--------------- Užduotis 8 ------------------------------------')

# Užduotis 8:
# Sukurkite funkciją registruoti_naudotoja(vardas, el_pastas, **kwargs), kuri
# priimtų vardą, el. paštą ir papildomus pasirinktinus duomenis.
# **kwargs naudojimas kitoje funkcijoje

def registruoti_naudotoja(vardas, el_pastas, **kwargs):
    naudotojas = {"vardas": vardas, "el_pastas": el_pastas, **kwargs}
    print('New user created:')
    for key, value in naudotojas.items():
        print(f' - {key}: {value}')
    return naudotojas

# Pavyzdys:
naudotojas_info = registruoti_naudotoja("Jonas", "jonas@example.com", amzius=25, miestas="Vilnius")
print(naudotojas_info)

def atspausdinti_lista(listas, **kwargs):
    for i in listas:
        print(i, **kwargs)
    # print(*listas, **kwargs)


# New user created:
#  - vardas: Jonas
#  - el_pastas: jonas@example.com
#  - amzius: 25
#  - miestas: Vilnius
# {'vardas': 'Jonas', 'el_pastas': 'jonas@example.com', 'amzius': 25, 'miestas': 'Vilnius'}


print('--------------- Užduotis 9 ------------------------------------')

# Užduotis 9:
# Sukurkite funkciją atspausdinti_lista(listas, **kwargs), kuri perduoda **kwargs
# į print(), leisdama valdyti formatavimą.

# Pavyzdys:
atspausdinti_lista(["Obuolys", "Bananai", "Vyšnios"], sep=" | ", end=".\n")

print('--------------- Užduotis 11 ------------------------------------')

# 11. Įvadas į lambda funkcijas
# Užduotis 11:
# Sukurkite lambda funkciją pakelti_kvadratu, kuri priima vieną skaičių ir grąžina jo
# kvadratą.

pakelti_kvadratu = lambda x: x ** 2
print(pakelti_kvadratu(3)) # atsakymas 9

print('--------------- Užduotis 12 ------------------------------------')

# 12. Lambda funkcijos ir rūšiavimas
# Užduotis 12:
# Turite sąrašą darbuotojų su vardais ir atlyginimais:
# darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
# Naudodami sorted() ir lambda funkciją, surūšiuokite sąrašą pagal atlyginimą nuo
# mažiausio iki didžiausio.

darbuotojai = [
    ['Jonas', 2500],
    ['Asta', 3200],
    ['Mantas', 2100],
]
res = sorted(darbuotojai, key=lambda listas: listas[-1])
print(res) # atsakymas [['Mantas', 2100], ['Jonas', 2500], ['Asta', 3200]]

print('--------------- Užduotis 13 ------------------------------------')

# 13. Lambda funkcija su filter()
# Užduotis 14:
# Turite sąrašą [5, 10, 15, 20, 25, 30]. Naudodami filter() ir lambda funkciją,
# palikite tik skaičius, kurie dalijasi iš 10.

listas = [5, 10, 15, 20, 25, 30]

dalus_is_desimties = list(filter(lambda x: x % 10 == 0, listas))
print(dalus_is_desimties) # atsakymas [10, 20, 30]

print('--------------- PABAIGA ------------------------------------')
