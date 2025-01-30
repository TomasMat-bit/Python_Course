
# a = True
# while a:        # ciklas kartojasi kol komanda islieka TRUE.
#     print('123')
#     a = False
#     break #  - - - - visada sustabdo cikla - - - -
# - - - - - - - - - - - - - - - - - - - -
#   objektas = [1, 2, 3, 4, 5]
#   for elementas in objektas:
#       if elementas == 2:
#           continue
#       print(elementas)
# # ------------------------------------------------------------
# skaitiklis = 0  # kaip naudojamas paprastas while ciklas
# while skaitiklis < 5:
#     print(f'skaitiklis yra {skaitiklis}')
#     print('----------------------------')
#     skaitiklis += 1
#
# # ----While True SU BRAKE komanda ----------------------------------------------
#
# while True:
#     ivestis = input("Įveskite žodį (q - išeiti)")
#     if ivestis == 'q':
#         break
#     print("Jūs įvedėte:", ivestis)

# # ------ break ir continue naudojimas while cikle--------------
#
# while True:
#     print('kartojimo pradžia')
#     print('1. šis meniu punktas nedaro nieko\n'
#           '2. išeiti iš kartojimo bloko\n'
#           '3. vėl parodyti meniu')
#
#     pasirinkimas = input()
#     if pasirinkimas == '2':
#         break
#     elif pasirinkimas == '3':
#         continue
#     else:
#         print('nieko nebuvo pasirinkta')
#     print('kartojimo pabaiga')

# ----------- UZDUOTIS -------------------------

# 1. Sukurti programa kuri vykdytu while cikla, kuriame prasoma ivesti skaiciu nuo 1 iki 10.
# 2. Jei ivesta reiksme ne siame intervale, programa naudotu continue ir
# paprasytu pakartoti ivesti.
# 3. Jei ivesta '5', ciklas butu nutrauktas su brake.
# 4. Isspausdintu visu ivestu skaiciu suma, neskaiciuojant '5'.

# res = 0
# while True:
#     number = int(input('Provide number'))
#     if number < 1 or number > 10:
#         print('Number not in range 1-10 ')
#         continue
#     if number == 5:
#         break
#     res += number
# print(f'Sum of given number: {res} ')

# -------------- -------------------- ------------------- --------------------

#
# while True:
#     print('1. atlikti skaičiaus daugybą\n'
#           '2. išeiti')
#
#     pasirinkimas = input()
#     if pasirinkimas == '2':
#         break
#
#     if pasirinkimas == '1':
#         # daugyba tęsis, kol nebus paspausta q
#         while True:
#             print('Įvesti skaičių daugybai iš 100 arba q - grįžti')
#             ivestis = input()
#             if ivestis == 'q':
#                 break
#             elif not ivestis.isdigit():
#                 print('Įvestas ne skaičius!!!')
#                 continue
#             skaicius = int(ivestis) * 100
#             print('Daugybos iš 100 rezultatas -', skaicius)

# # ------------ Operacijos for cikle -----------------------
#
# listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# flag5 = False
# flag3 = False
#
# for elem in listas:
#     print(elem)
#     if elem % 5 == 0:
#         flag5 = True
#     if elem % 3 == 0:
#         flag3 = True
#
#     if flag5 and flag3:
#         break
# # 1
# # 2
# # 3
# # 4
# # 5
# if flag5:
#     print("Liste yra elementas kuris dalinasi iš 5")
# if flag3:
#     print("Liste yra elementas kuris dalinasi iš 3")
#
# # Liste yra elementas kuris dalinasi iš 5
# # Liste yra elementas kuris dalinasi iš 3

# #  - - - - - - - - Kaupikliai cikluose - - - - - - - - - -
#
# listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # suma
# suma = 0
# for elem in listas:
#     suma += elem  # kaupiame sumą
# print('Suma yra:', suma) # Suma yra: 45
#
# # maksimalus skaičius
# maksimalus = listas[0]
# for elem in listas:
#     if elem > maksimalus:
#         maksimalus = elem  # randame maksimalų elementą
# print('Maksimalus yra:', maksimalus) # Maksimalus yra: 9
#
# # maziausiais skaičius
# maziausias = listas[0]
# for elem in listas:
#     if elem < maziausias:
#         maziausias = elem  # randame maksimalų elementą
# print('maziausias yra:', maziausias) # maziausias yra: 1
#
# # Apibendrinimas: Šiame kode naudojami ciklai kartu su
# # kintamaisiais, kurie kaupia sumą ir maksimalų elementą
# # iš sąrašo. Tai moko, kaip rinkti ir apdoroti informaciją ciklo metu,
# # pvz., skaičiuoti sumą arba rasti didžiausią vertę sąraše.

# # - - - - - - - - UZDUOTIS - - - - - - - - - - - - - -----------
#
# #Sukurkite programa:
# # 1. Interuos per sarasa skaiciu [5, 7, 15, 6, 3, 20, 12].
# # 2. Isspausdins tik tuos, kurie yra lyginiai arba dalijasi is 5.
# # 3. Jei suras skaiciu, didesni nei 10, programa nutraukia interacija.
#
# listas = [5, 7,  6, 15, 3, 20, 12]
# flag5 = False
# flag3 = False
#
# for elem in listas:
#     print(elem)
#     if elem > 10:
#         print('Jusu skaicius daugiau uz 10')
#         break
#     if elem % 5 == 0:
#         flag5 = True
#     if elem % 2 == 0:
#         flag3 = True
#
# if flag5:
#     print("Liste yra elementas kuris dalinasi iš 5")
# if flag3:
#     print("Liste yra elementas kuris dalinasi iš 2")
# print('------------------------------------------------------------------')
#
# # Kaupikliai cikluose. Sukurkite programa:
# # 1. Naudodama for cikla iteruos per sarasa [-10, -5, 0, 5, 10, 15, 20].
# # 2. Apsakiciuos teigiamu ir neigiamu skaiciu sumas atskirai.
# # 3. Isspausdins didziausia ir maziausia reiksme sarase.
#
# kaip padaryt pvz:
# # Užduotis 7
# skaiciai = [-10, -5, 0, 5, 10, 15, 20]
# teigiama_suma = 0
# neigiama_suma = 0
# for skaicius in skaiciai:
#     if skaicius > 0:
#         teigiama_suma += skaicius
#     elif skaicius < 0:
#         neigiama_suma += skaicius
# didziausias = max(skaiciai)
# maziausias = min(skaiciai)
# print(f"Teigiamų skaičių suma: {teigiama_suma}")
# print(f"Neigiamų skaičių suma: {neigiama_suma}")
# print(f"Didžiausias skaičius: {didziausias}")
# print(f"Mažiausias skaičius: {maziausias}")


# -NAUJA TEMA- - - - - break ir continue komandos for cikle

# listas = ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']
#
# # break pavyzdys, spausdinam visus mėnesius, tačiau pasiekę balandį nutraukiam perrinkimą
# for elem in listas:
#     if elem == 'balandis':
#         break
#     print(elem)
# print('---------------------------------------')
# # continue panaudosim praleisti sausį
# for elem in listas:
#     if elem == 'sausis':
#         continue
#     print(elem)
# print("-----")


# # - - - - - - - - - - - - -  else blokas cikluose
#
# for skaicius in range(1, 5):
#     if skaicius % 2 == 0:
#         print("Skaičius", skaicius, "yra lyginis")
#     else:
#         print("Skaičius", skaicius, "yra nelyginis")
#
# print("-----")
#
# for skaicius in range(1, 5):
#     if skaicius % 2 == 0:
#         print("Skaičius", skaicius, "yra lyginis")
# else:
#     print("Ciklas baigtas")

    # ---- UZDUOTYS - - - - - -

# else blokas cikluose
#  - - - - - - - - -Užduotis 9:
# Sukurkite programą, kuri:
# 1. Naudodama for ciklą ieško pirmo lyginio skaičiaus
# sąraše [1, 3, 5, 7, 8, 10, 11].
# 2. Kai suranda lyginį skaičių, išspausdina jį ir nutraukia ciklą.
# 3. Jei ciklas baigiasi neradęs lyginio skaičiaus,
# išspausdina „Lyginių skaičių nėra“.
#   --------------1  as sprendimo variantas ----
# listas = [1, 3, 5, 7, 8, 10,  11]
# for numb in range(1, 5):
# for number in listas:
#     if number % 2 == 0:
#         print("Skaičius", number, "yra lyginis")
#         break
# else:
#     print('Lyginių skaičių nėra')
#   --------------2  as sprendimo variantas ----
# for numb in [1, 3, 5, 7, 8, 10,  11]:
#     if numb % 2 == 0:
#         print('Skaičius', numb, 'yra lyginis')
#         break
# else:
#     print('Lyginių skaičių nėra')
#   --------------3cias sprendimo variantas ----
# for numb in [1, 3, 5, 7, 8, 10,  11]:
#     if not numb % 2:
#         print(f'Skaičius', {numb}, 'yra lyginis')
#         break
# else:
#     print('Lyginių skaičių nėra')

