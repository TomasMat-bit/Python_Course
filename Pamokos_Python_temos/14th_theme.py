# Pamoka 14 Objektinis programavimas I ‐ klasės, instance objektai
# Paskaita: Objektinis programavimas – Klasės, Instancijos, Metodai, ir Objektų Valdymas

print('-------      1. Klasės kūrimas ir statiniai laukai     ----------------')

class House:
    country = "LT"

print(House.country)  # LT

print('-------      2. Konstruktorius init ir instancijos laukų inicializavimas     ----------------')

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year


print('-------  3. Statinio lauko ir instancijų naudojimas     ----------------')

print(House.country)  # LT

house_instance_1 = House(10_000, 1990)
print(house_instance_1.price)  # 10000
print(house_instance_1.year)  # 1990

house_instance_2 = House(12_000, 1920)
print(house_instance_2.price)  # 12000
print(house_instance_2.year)  # 1920

print('-------  4. Klasės instancijų atvaizdavimas   ----------------')

print(house_instance_1)  # <__main__.House object at 0x000001FDB47DB850>
print(house_instance_2)  # <__main__.House object at 0x000001FDB47DB790>


from datetime import datetime

class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        current_year = datetime.today().year #  OR SHORTER return datetime.today()year - self.year
        return current_year - self.year

print('-------  5. Savų metodų kūrimas klasėje   ----------------')

house_instance_1 = House(10_000, 1990)
age = house_instance_1.get_age()
print(age)

house_instance_2 = House(5_000_000, 2001)
age = house_instance_2.get_age()
print(age)

print('-------  6. Metodų iškvietimas ir rezultatų naudojimas   ----------------')

# from datetime import datetime
#
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#      # def __str__(self):
#      #     return f'Namas {self.year} pastatymo, kaina - {self.price}, amzius {self.get_age()}'
#
#      def get_age(self):
#          return datetime.today().year - self.year
#
# book1 = House()
# # NESPEJAU

print('-------  7. str metodas – Objektų atvaizdavimo valdymas   ----------------')

# from datetime import datetime     NESUPRATAU
#
# class House:
#     country = "LT"
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def get_age(self):
#         now = datetime.datetime.today()
#         current_year = now.year
#         return current_year - self.year
#
#     def __str__(self):
#         return f'Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}'
#
#
# for house in House:
#     print(house)

print('-------  10. Objektų pridėjimas į sąrašą naudojant vartotojo įvestį   ----------------')

from datetime import datetime


class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def __str__(self):
        return f'Namas {self.year} pastatymo, kaina - {self.price}, amžius {self.get_age()}'

    def get_age(self):
        return datetime.today().year - self.year

houses_kaupiklis = []
while True:
    year = int(input('Iveskite metus: '))
    price = int(input('Iveskite kaina: '))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)

    print('Spausdinam ka sukaupem:')
    for house in houses_kaupiklis:
        print(house)
