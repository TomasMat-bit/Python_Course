print(' - - - - - - - - - - - -  UZDUOTIS 1  - - - - - - - - - - - ')

# 1. Apsaugoti Atributai (Protected Attributes)
# Užduotis:
# Sukurkite klasę Studentas, kuri turi atributus vardas, pavarde ir apsaugotą atributą
# _pazymiai.+
# • Pridėkite metodą prideti_pazymi(), kuris leidžia pridėti pažymį, jei jis yra tarp 1 ir
# 10.+
# • Sukurkite metodą rodyti_vidurki(), kuris apskaičiuoja pažymių vidurkį.+
# Papildoma užduotis:
# Paveldėkite klasę Studentas ir sukurkite klasę StudentasLyderis, kuri papildomai gali
# pridėti „bonus“ taškų prie vidurkio.

class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10 :
            self._pazymiai.append(pazymys)
        else:
            print('Pazymys negali būti < 0 ir > 10')

    def rodyti_vidurki(self):
        if len(self._pazymiai) == 0:
            return 0
        return sum(self._pazymiai) / len(self._pazymiai)

studentas = Studentas('Petriukas', 'Petrauskis')
studentas.prideti_pazymi(8)
studentas.prideti_pazymi(4)
studentas.prideti_pazymi(2)
studentas.prideti_pazymi(10)
studentas.prideti_pazymi(9)
studentas.prideti_pazymi(9)
print(f'Studento {studentas.vardas} vidurkis: {studentas.rodyti_vidurki()}')

print('-' * 30)

# Paveldėkite klasę Studentas ir sukurkite klasę StudentasLyderis, kuri papildomai gali
# pridėti „bonus“ taškų prie vidurkio.


class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonusai = 0):
        super().__init__(vardas, pavarde)
        self.bonusai = bonusai

    def rodyti_vidurki(self):
        vidurkis = super().rodyti_vidurki()
        bendras_skaicius = len(self._pazymiai) + 1
        galutinis_vidurkis = (sum(self._pazymiai) + self.bonusai) / bendras_skaicius
        return galutinis_vidurkis

studentas_lyderis = StudentasLyderis('Petriukas', 'Petrauskis', bonusai=3)
studentas_lyderis.prideti_pazymi(10)
studentas_lyderis.prideti_pazymi(10)
studentas_lyderis.prideti_pazymi(10)

print(f'Studento  {studentas_lyderis.vardas} {studentas_lyderis.pavarde} galutinis vidurkis su bonusais: {studentas_lyderis.rodyti_vidurki()}')
print('-' * 30)
#destytojo kodas: zemiau:


class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10:
            self._pazymiai.append(pazymys)
        else:
            print("Pažymys turi būti tarp 1 ir 10.")

    def rodyti_vidurki(self):
        if self._pazymiai:
            vidurkis = sum(self._pazymiai) / len(self._pazymiai)
            print(f"{self.vardas} {self.pavarde} pažymių vidurkis: {vidurkis:.2f}")
        else:
            print("Pažymių nėra.")

class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonus_taskai=0):
        super().__init__(vardas, pavarde)
        self.bonus_taskai = bonus_taskai

    def rodyti_vidurki(self):
        if self._pazymiai:
            vidurkis = sum(self._pazymiai) / len(self._pazymiai)
            vidurkis_su_bonus = vidurkis + self.bonus_taskai
            print(f"{self.vardas} {self.pavarde} pažymių vidurkis su bonus: {vidurkis_su_bonus:.2f}")
        else:
            print("Pažymių nėra.")


studentas = Studentas("Jonas", "Jonaitis")
studentas.prideti_pazymi(8)
studentas.prideti_pazymi(9)
studentas.rodyti_vidurki()

lyderis = StudentasLyderis("Agnė", "Petrauskaitė", bonus_taskai=0.5)
lyderis.prideti_pazymi(7)
lyderis.prideti_pazymi(10)
lyderis.rodyti_vidurki()


print('-' * 30)
print(' - - - - - - - - - - - -  UZDUOTIS 2  - - - - - - - - - - - ')

# 2. Privatūs Atributai (Private Attributes)
# Užduotis:
# Sukurkite klasę BankoSaskaita, kuri turi atributus savininkas ir privatų atributą
# __balansas.+
# • Sukurkite metodus gauti_balansa() ir prideti_pinigus(), kad būtų galima
# saugiai valdyti balansą.
# • Įsitikinkite, kad negalima tiesiogiai pasiekti __balansas atributo iš išorės.
# Papildoma užduotis:
# Pridėkite metodą nuskaičiuoti_pinigus(), kuris leis nuskaičiuoti pinigus tik tada, jei
# sąskaitoje pakanka lėšų.

# class BankoSaskaita:
#     def __init__(self, savininkas):
#         self.savininkas = savininkas
#         self.__balansas = 0
#
#     def gauti_balansa(self):
#         return self.__balansas
#
#     def prideti_pinigus(self, suma):
#         if suma > 0:
#             self.__balansas += suma
#         else:
#             print('Klaida: Suma turi buti didene uz 0')
#
#
#
#
#
# saskaita = BankoSaskaita('Adomas', '1000')
# # print(f'Savininko {saskaita.savininkas} balansas: {saskaita.gauti_balansa()} EUR')
# print(f"Po papildymo, balansas: {saskaita.gauti_balansa()} EUR")

print('-' * 30)
#destytojo kodas: zemiau:

class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.__balansas = 0

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
            print(f"Pridėta {suma} EUR. Dabartinis balansas: {self.__balansas} EUR.")
        else:
            print("Suma turi būti didesnė nei 0.")

    def nuskaičiuoti_pinigus(self, suma):
        if suma > 0 and suma <= self.__balansas:
            self.__balansas -= suma
            print(f"Nuskaičiuota {suma} EUR. Dabartinis balansas: {self.__balansas} EUR.")
        elif suma > self.__balansas:
            print("Nepakanka lėšų sąskaitoje.")
        else:
            print("Suma turi būti didesnė nei 0.")


saskaita = BankoSaskaita("Petras Petraitis")
saskaita.prideti_pinigus(500)
print(f"Balansas: {saskaita.gauti_balansa()} EUR")

saskaita.nuskaičiuoti_pinigus(200)
print(f"Balansas po nuskaičiavimo: {saskaita.gauti_balansa()} EUR")

try:
    print(saskaita.__balansas)
except AttributeError as e:
    print(f"Klaida: {e}")


print('-' * 30)

print(' - - - - - - - - - - - -  UZDUOTIS 3  - - - - - - - - - - - ')

# 3. @property Dekoratorius
# Užduotis:
# Sukurkite klasę Darbuotojas, kuri turi atributus vardas, pavarde ir privatų atributą
# __atlyginimas.+
# • Naudokite @property dekoratorių, kad galėtumėte gauti ir nustatyti atlyginimą.
# • Užtikrinkite, kad atlyginimas negali būti mažesnis nei minimalus (pvz., 500).
# Papildoma užduotis:
# Pridėkite papildomą @property metodą mokesciai, kuris apskaičiuoja mokesčius (pvz.,
# 20% nuo atlyginimo).

class Darbuotojas:
    def __init__(self, vardas, pavarde, asmens_kodas, atlyginimas = 500):
        self.vardas = vardas
        self.pavarde = pavarde
        self.asmens_kodas = asmens_kodas
        self.__atlyginimas = atlyginimas

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, suma):
        if suma >= 500:
            self.__atlyginimas = suma
        else:
            raise ValueError('Min atlyginimas 500 pinigu')

    @property
    def mokesciai(self):
        return self.__atlyginimas * 0.20

    @property
    def lytis(self):
        return 'Vyras' if self.asmens_kodas[0] == '3' else 'Moteris'

darbuotojas = Darbuotojas('Jonas', 'Jonavicius', '39694030284')

print(darbuotojas.lytis)
print(darbuotojas.atlyginimas)
print(darbuotojas.mokesciai)

print('-' * 30)

darbuotojas.atlyginimas = 2000
print(darbuotojas.atlyginimas)
print(darbuotojas.mokesciai)

print('-' * 30)

try:
    darbuotojas.atlyginimas = 400
except ValueError as e:
    print(e)

print(' - - - - - - - - - - - -  UZDUOTIS 4  - - - - - - - - - - - ')
