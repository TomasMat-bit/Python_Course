#Paskaita: datetime modulis ir laiko valdymas
# datetime klasė ir datos-laiko skaičiavimai

import datetime
# from http.cookiejar import month

print(type(datetime))  # <class 'module'>

# kreipiamės į funkcionalumą aprašytą datetime faile
# todėl kode 2 kartus kartojam datetime
# antrasis datetime yra kreipimasis į klasę
# .today() metodas sukuria šio laiko momento datos-laiko objektą
# rezultatas yra datetime.datetime objektas

dt_res = datetime.datetime.today()
print(dt_res)  # 2024-10-10 10:33:24.596796
print(type(dt_res))  # <class 'datetime.datetime'>

print('------Atskiri datos-laiko laukai iš datetime objekto---------')

# datetime.datetime objektas turi savybes(laukus)
# į kuriuos galima kreiptis, jie saugo atskiras datos-laiko
# sudedamąsias dalis(keisis vis išnaujo paleidus, nes ėmėm šio momento datą laiką)
res_year = dt_res.year
print(res_year)  # 2024
print(type(res_year))  # <class 'int'>

print(dt_res.month)
print(dt_res.day)
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)
print(dt_res.microsecond)

print('------ Norimos datos ir laiko objekto sukūrimas ---------')

# patys sukuriam norimos datos ir laiko objektą
# pilnai užpildome datos ir laiko laukus

my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)
print(my_datetime)  # 2011-12-31 23:59:59

# today_dt = datetime.datetime.today()
# print(my_datetime)
# if my_datetime < today_dt:
#     print('YES')
# laiką paduoti nebūtina, užtenka datos

my_datetime = datetime.datetime(2000, 1, 1)
print(my_datetime)  # 2000-01-01 00:00:00
# ----------------------------------------------------------------------------

time_from_2000 = datetime.datetime.today() - datetime.datetime(2000, 1, 1)
print(time_from_2000)
# ----------------------------------------------------------------------------


last_payment_dt = datetime.datetime(2000, 1, 1)

print('------ Datos ir laiko įvedimas naudojant str formatą ---------')

# ĮVESTIS
# sukursime savo ivesties formatą, naudojant kaukes - formato apibrėžimui
# ir str - įvesčiai
# .strptime - metodas naudoja kaukes, duomenų atpažinimui - https://strftime.org/

ivestis = '2020-02-11'
my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
print(my_datetime)

ivestis = '2020.02.15, 10:11:59'
my_datetime = datetime.datetime.strptime(ivestis, '%Y.%m.%d, %H:%M:%S')
print(my_datetime)

print('------ Datos ir laiko išvedimas naudojant strftime formatą ---------')
months = {
    1: 'Sausis',
    2: 'Vasaris'
}

# IŠVESTIS,
# taip pačiai sudaroma kaukė, tačiau naudojamas kitas metodas,
# įvesties nepateikiama, naudojamas jau sukurtas datetime objektas
# strftime metodas

print(my_datetime)  # 2020-02-15 10:11:59
print(my_datetime.strftime('%d %m %Y'))  # 15 02 2020
print(my_datetime.strftime('%d %B %Y'))  # 15 February 2020

print(months.get(my_datetime.month)) # Vasaris
print(my_datetime.strftime('%d %B %Y'))  # 15 February 2020


print('------ Laiko skirtumo (timedelta) objekto gavimas atliekant datų atimtį ---------')

dabar = datetime.datetime.today()
mileniumas = datetime.datetime(2000, 1, 1)

skirtumas = dabar - mileniumas
print(skirtumas)
print(type(skirtumas))

print('------ Skaičiavimai su timedelta objektais ---------')

# laiko skirtumo objektą mes galim pridėti arba atimti iš datos laiko,
# gaudami kitą datetime objektą
# skaičiavimams dažniausiai patogiau sudaryti naują timedelta objektą,
# iškvietus jo klasę

skirtumas = datetime.timedelta(hours=1000)
print(skirtumas)
res = dabar + skirtumas
print(res)

skirtumas = datetime.timedelta(days=1000, hours=100, minutes=100)
print(skirtumas)
res = dabar - skirtumas
print(res)

print('------ timedelta objekto laukų prieiga ---------')

skirtumas = datetime.timedelta(days=1000, hours=100, minutes=100)
print(skirtumas)
print(skirtumas.days)
print(skirtumas.seconds)
print(skirtumas.seconds / 60 / 60)

sekundes = skirtumas.total_seconds()
print(sekundes)