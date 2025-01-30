# numb1 = 65
# numb2 = 1.75
# text = "Jonas"
#
# print(type(numb1))
# print(type(numb2))
# print(type(text))
#
# res =  text, numb1 / (numb2 / 100) ** 2
# print(res)
#
# user_input = input('Jusu BMI: ')
# print(type(user_input))
#
# user_input1 = float(input('Number 1: '))
# user_input2 = float(input('Number 2: '))
#
# print(user_input1 + user_input2)

print(    f"Hello, {input('Name: ')} {input('Surname: ')}!")

mase = float(input('Mase (kg): '))
ugis = float(input('Ugis (cm): '))
res = 'Jusu BMI: ' + str(mase / ((ugis / 100) ** 2))
print(res)

# print(f"Your BMI: {float(input('Mass kg: ')) / ((float(input('Ugis M: ')) / 100) ** 2)}")

# -  BMI APSKAICIAVIMS UP -----------------------------------------------------------------------

# text1 = 'ABCDE'
# print(text1[0])
# print(text1[1])
# print(text1[2])
# print(text1[3])
# print(text1[4])
# print('-----------')
# print(text1[-1])
# print(text1[-2])

#--------------------Slicing----------------------------------
# text1 = 'ABCDE'
# print(text1[0:2]) #AB
# print(text1[1:4])#BCD
# print(text1[1:-1])#BCD
# print(text1[1:]) #BCDE
# print(text1[:4]) #ABCD
# #TASK 1
# text2 = 'Hello world!'
# print(text2[0:5])# Hello
# print(text2[:-6])# Hello
# print(text2[6:])# world
# print(text2[:7])# Hello W
# print(text2[1:7])# ello W
# print(text2[1:-2])# ello Worl
# print(text2[5])# ' ' - Tarpas
# print("'" + text2[5] + "'")
# print("Task Done!")


# text2 = 'Hello World'
# print(text2[1:10:1])
# print(text2[1:10:2])
# print(text2[::2]) # PASIIMI KAS 2 SIMBOLI
# print(text2[::-1]) # PASIIMI KAS 1 SIMBOLI bet apvercia


# -----------------SEKANTI TEMA --- STRING --- METODAI --------------
# konvertavimas i DIDZIASIAS RAIDES
# text = 'hello world'
# text2 = text.upper()
#
# print('text - ' + text)
# print('text2 - ' + text2) # padidina raides
# text = 'hello world'
# print(text.count('l')) # String skaiciuokle--------------------
# print(text.count('ll'))

# # ----------------Mazinimo metodas LOWER--------------
# text3 = 'Hello World'
# print(text3.lower())
#
# user = 'TOMAS'
# imported_user = 'TOMas'


# text = 'hello world'
# print(text.index('r')) # skaiciuoja kelintame indexe
# print(text.index('l')) # skaiciuoja kelintame indexe, sustoja ties pirmu rastu simboliu.
# print(text.index('world'))
# print(text.index('abra'))

# text = 'hello world' #Find naudoti saugiau, nelauzo programos nei INDEX
# print(text.find('r'))
# print(text.find('l'))
# print(text.find('world'))
# print(text.find('abra'))

# --------------text replace--------------------
# text = 'hello world'
# text2 = text.replace('l', 'w')
# text3 = text.replace( 'hello','how are you ')
#
# print(text2)
# print(text3)

# #----- Ivesto lauko tarpu naikinimas------------
# user = '     Tomas Matukas    '
# user2 = 'Tomas Matukas'
#
# user = user.strip()
#
# print(user)
# print(user == user2)

# month = 'sausis'
# day = 14
# ftext = f'''Menesis yra {
# month
# }, diena yra {day / 3}d.
# '''
# print(ftext)




