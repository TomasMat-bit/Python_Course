
# - - - - - - - U Z D U O T I S  - -- 1 - -- - - - - - - - - - -

# Įvadas į funkcijas
# Užduotis 1:
# Sukurkite funkciją sveikink(), kuri tris kartus iš eilės atspausdintų pasisveikinimą:
# „Labas!“. Iškvieskite šią funkciją programoje.
def pasveikink():
    for i in range(3):
        print('Sveikinu atvykus ! ! !')

pasveikink()
print('---------------------------------------------------------')

# - - - - - - - U Z D U O T I S  - -- 2 - -- - - - - - - - - - -
# Argumentai ir return reikšmės
# Užduotis 2:
# Sukurkite funkciją sudaugink(x, y), kuri priimtų du skaičius ir grąžintų jų sandaugą.
# 1. Iškvieskite funkciją su reikšmėmis 5 ir 10.
# 2. Išspausdinkite grąžintą rezultatą.

def sudaugink(x, y):
    if not x or not y:
        return
    return x * y

suma = sudaugink(5, 10)
if suma:
    print(suma)
else:
    print('Numbers is not provided!')

print('---------------------------------------------------------')

# - - - - - - - U Z D U O T I S  - -- 3 - -- - - - - - - - - - -

# 3. Funkcijos su keliais argumentais
# Užduotis 3:
# Sukurkite funkciją trys_sveikinimai(vardas1, vardas2, vardas3), kuri priimtų tris
# vardus ir kiekvienam iš jų atspausdintų pasisveikinimą.
# Pvz.: „Labas, Jonas!“, „Labas, Asta!“, „Labas, Mantas!“.

def pasisveikinimas_su_naujais_vartotojais(vardas1, vardas2, vardas3):
    sveiki = f'Labas  {vardas1}! Labas {vardas2}! Ir Labas {vardas3}'
    return sveiki
res = pasisveikinimas_su_naujais_vartotojais('Jonas', 'Asta', 'Mantas!')
print(res)
print('---------------------------------------------------------')
# 4. Numatytosios reikšmės ir keyword argumentai
# Užduotis 4:
# Sukurkite funkciją sveikink_su_pavadinimu(vardas, pavadinimas="drauge"), kuri
# atspausdintų žinutę: „Sveikas, [vardas]! Ką veiki, [pavadinimas]?“.
# 1. Iškvieskite funkciją nenurodydami pavadinimo.
# 2. Iškvieskite funkciją, nurodydami pavadinimą „kolega“.

def sveikink_su_pavadinimu(vardas, pavadinimas='drauge'):
    print(f'Sveikas, {vardas}! Ką veiki, {pavadinimas}?')
sveikink_su_pavadinimu('Tomas')
sveikink_su_pavadinimu('Petras', pavadinimas='kainyne')

print('---------------------------------------------------------')


