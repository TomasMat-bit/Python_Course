print('- - - - - - - - - Užduotis 2: - - - - - - - - - - - - ')

# 1. Sukurkite funkciją dalinti(a, b), kuri dalina a iš b.
# 2. Jei b == 0, funkcija turėtų sugauti ZeroDivisionError ir grąžinti "Dalyba iš
# nulio negalima.".
# 3. Išbandykite funkciją su reikšmėmis (10, 2), (5, 0), (8, 4)
# one option

def dalinti(a, b):
    try: return a / b
    except ZeroDivisionError: return "Dalyba iš nulio negalima."
print(dalinti(10, 2), dalinti(5, 0), dalinti(8, 4))

# 2nd option

def dalinti(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Dalyba iš nulio negalima.'
print(dalinti(10,2))
print(dalinti(5,0))
print(dalinti(8,4))

print('- - - - - - - - - Užduotis 3: - - - - - - - - - - - - ')

# Užduotis 3:
# 1. Paprašykite vartotojo įvesti du skaičius.
# 2. Naudokite try-except, kad suvaldytumėte:
# a. ValueError, jei vartotojas įveda ne skaičių.
# b. ZeroDivisionError, jei dalinama iš nulio.
# 3. Jei klaidos nėra, išveskite rezultatą

input1 = input('irasykite skaiciu: ')
input2 = input('irasykite skaiciu: ')

try:
    a = int(input1)
    b = int(input2)
    res = a / b
    print(f'Your result is: {res}')
except ZeroDivisionError:
    print('Change 0 to another integer')
except ValueError:
    print('Use numbers')
print('----------------------------------------------')

print('- - - - - - - - - Užduotis 4: - - - - - - - - - - - - ')


