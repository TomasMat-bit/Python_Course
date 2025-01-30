#  - - - - - - - Paskaita: Importai ir moduliai - - - -
#  - - - - - - - Įvadas į importus ir modulius - - - -
#  - - - - - - - Paprastas importavimas - - - -

import random

atsitiktinis_skaicius = random.randint(1, 10)
print(f"Atsitiktinis int skaičius nuo 1 iki 10: {atsitiktinis_skaicius}")
print(' - - - - - -------------------- - - - - - - - -')
#  - - - - - - - Specifinių funkcijų importavimas - - - -

from random import randint, choice
random_number = randint(1, 10)
print(random_number)
random_month = choice(["sausis", "vasaris", "kovas"])
print(random_month) # vasaris
print(' - - - - ---------------------------- - - - - - - - -')
#  - - - - - - - - - - -Modulio trumpinimas naudojant alias -- - - - - - - - - - - -- - - - -

import random as rn

atsitiktinis_skaicius = rn.randint(20, 25)
print(atsitiktinis_skaicius)

atsitiktinis_elementas = rn.choice(["sausis", "vasaris", "kovas"])
print(atsitiktinis_elementas)

print(' - - - - ---------------------------- - - - - - - - -')

#  - - - - - - - - - - -Specifinių funkcijų importavimas su alias -- - - - - - - - - - - -- - - - -

from random import randint as rnt

atsitiktinis_skaicius = rnt(1, 10)

print(' - - - - ---------------------------- - - - - - - - -')


#  - - - - - - - - -SVisko importavimas iš modulio (nerekomenduojamas būdas) -- - - - - - - - - - - -- - - - -

# from random import *
# parinktis = sample(['sausis', 'vasaris', 'kovas'])
# print(parinktis) #NEREKOMENDUOJAMAS KODAS / BUDAS. DAZNAI SUMAISOMAS KODAS

print(' - - - - ---------------------------- - - - - - - - -')

#  - - - - - - - - -Importai iš mūsų sukurto modulio -- - - - - - - - - - - -- - - - -
#  - - - - - - - - -Visas modulio importavimas -- - - - - - - - - - - -- - - - -

from mylib import aritmetikosmodulis, aritmetikosmodulis as ar

res = aritmetikosmodulis.dalink(10, 7)
print(res)

res = aritmetikosmodulis.daugink(10, 7)
print(res)

res = aritmetikosmodulis.atimk(10, 7)
print(res)

res = aritmetikosmodulis.sumuok(10, 7)
print(res)
print(' - - - - -----Specifinių funkcijų importavimas----------------------- - - - - - - - -')

res = aritmetikosmodulis.dalink(9, 3)
print(res)

res = aritmetikosmodulis.daugink(12, 43)
print(res)

res = aritmetikosmodulis.atimk(34, 23)
print(res)

res = aritmetikosmodulis.sumuok(23, 9)
print(res)

print(' - - - - ---Modulio trumpinimas naudojant alias------------------------- - - - - - - - -')


#  - - - - - - - - -Modulio trumpinimas naudojant alias -- - - - - - - - - - - -- - - - -

res = ar.dalink(10, 7)
print(res)

res = ar.daugink(10, 7)
print(res)

print(' - - - - ---Importai iš folderio ----------------- - - - - - - - -')
#  - - - - - - - - -Visas modulio importavimas iš folderio -- - - - - - - - - - - -- - - - -

import mylib.matematika as matem

res = matem.sumuok(1, 5)
print(res)

print(' - - - - ---Specifinių funkcijų importavimas iš folderio ----------------- - - - - - - - -')
#  - - - - - - - - -Specifinių funkcijų importavimas iš folderio -- - - - - - - - - - - -- - - - -

from mylib.matematika import sumuok, daugink

res = sumuok(1, 2)
print(res)
res = daugink(2,4 )
print(res)

#  - - - - - - - - -Importavimas viso folderio -- - - - - - - - - - - -- - - - -
# example
# import mylib

# res = mylib.aritmetika.sumuok(1, 5)
# print(res)





