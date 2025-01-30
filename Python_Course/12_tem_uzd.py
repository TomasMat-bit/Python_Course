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







