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

# - - - - - - - U Z D U O T I S  - -- 1 - -- - - - - - - - - - -

# Įvadas į funkcijas
# Užduotis 1:
# Sukurkite funkciją sveikink(), kuri tris kartus iš eilės atspausdintų pasisveikinimą:
# „Labas!“. Iškvieskite šią funkciją programoje.
def pasveikink():
    for i in range(3):
        print('Sveikinu atvykus ! ! !')

pasveikink()

