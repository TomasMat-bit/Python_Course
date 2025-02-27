
# UZDUOCIU SORENDIMAS SU SQLTable
#
# 8. Teksto operacijos (||)
# Užduotis:
# Sukurkite naują stulpelį, kuris rodo mokytojo pilną vardą ir pavardę.
# %%sql
# SELECT vardas || ' ' || pavarde AS "Pilnas Vardas" FROM mokytojai;
# Sukurkite naują stulpelį "Dėsto", kuris rodo mokytojo dėstomą dalyką, pvz.:
# "Jonas Jonaitis dėsto Matematiką".

# In [10]: exit
# (.venv) PS C:\Users\PROMAR\Desktop\STUDIJOS\Python> ipython
# Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#    ...: %sql sqlite:///mokykla.db
#
# In [3]: %%sql
#    ...: SELECT vardas, pavarde  AS 'mokytojas'  FROM mokytojai;
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# Done.
# Out[3]:
# [('Jonas', 'Jonaitis'),
#  ('Jonas', 'Jonaitis'),
#  ('Virginija', 'Mokytpja'),
#  ('Petras', 'Petrauskas')]
#
# In [4]: %%sql
#    ...: SELECT vardas || ' ' ||  pavarde  AS 'Pilnas vardas'  FROM mokytojai;
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# Done.
# Out[4]:
# [('Jonas Jonaitis',),
#  ('Jonas Jonaitis',),
#  ('Virginija Mokytpja',),
#  ('Petras Petrauskas',)]
#
# In [5]: %%sql
#    ...: SELECT vardas || ' ' ||  pavarde  AS 'Pilnas vardas'  FROM mokytojai AND "Desto: " dalykas FROM dalykas;
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# (sqlite3.OperationalError) near "AND": syntax error
# [SQL: SELECT vardas || ' ' ||  pavarde  AS 'Pilnas vardas'  FROM mokytojai AND "Desto: " dalykas FROM dalykas;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [6]: %%sql
#    ...: SELECT vardas || ' ' || pavarde || ' dėsto ' || dalykas AS 'Dėsto' FROM mokytojai;
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# Done.
# Out[6]:
# [('Jonas Jonaitis dėsto Matematika',),
#  ('Jonas Jonaitis dėsto Matematika',),
#  ('Virginija Mokytpja dėsto Muzika',),
#  ('Petras Petrauskas dėsto Fizika',)]

## 9. Matematiniai skaičiavimai
# Užduotis:
# Apskaičiuokite, kiek metų vidutiniškai dirba mokytojai, jei žinoma, kad vidutinis mokytojo
# darbo pradžios metai – 2005.
# %%sql
# SELECT 2024 - 2005 AS "Vidutinis patirties amžius";
# Apskaičiuokite atlyginimą be mokesčių (įvertinant, kad PVM 21%).
# %%sql
# SELECT vardas, pavarde, atlyginimas, ROUND(atlyginimas / 1.21, 2) AS
# "Be Mokesčių" FROM mokytojai;


# In [7]: %%sql
#    ...: SELECT 2024 - 2005 AS "Vidutinis patirties amžius";
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# Done.
# Out[7]: [(19,)]
#
# In [8]: %%sql
#    ...: SELECT vardas, pavarde, atlyginimas, ROUND(atlyginimas / 1.21, 2) AS
#    ...: "Be Mokesčių" FROM mokytojai;
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# Done.
# Out[8]:
# [('Jonas', 'Jonaitis', 1600, 1322.31),
#  ('Jonas', 'Jonaitis', 1600, 1322.31),
#  ('Virginija', 'Mokytpja', 1400, 1157.02),
#  ('Petras', 'Petrauskas', 1000, 826.45)]
#
# In [9]:

print(' - - - - - - -  Grupavimas ir agregavimo funkcijos - - -  ')

# %load_ext sql
# %sql sqlite:///cars.db
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# SELECT * FROM cars;
# %sql SELECT * FROM cars;
# %%sql
# SELECT MIN(price), MAX(price), AVG(price) FROM cars;
# %%sql
# SELECT AVG(2025 - year) FROM cars;
# %%sql
# SELECT make, AVG(price) FROM cars;
# %%sql
# SELECT make, count(*) FROM cars;
# %%sql
# SELECT make, count(*) FROM cars GROUP BY make;
# %%sql
# SELECT make, AVG(price) FROM cars GROUP BY make;
# %%sql
# SELECT color, max(price), make, model FROM cars GROUP BY color ORDER BY price DESC;
# %%sql
# SELECT make, model, year, MAX(price) AS "maxas"
# FROM cars
# WHERE make NOT IN ('Toyota', 'Mercury', 'Volvo')
# GROUP BY make
# ORDER BY year;
# %%sql
# SELECT make, model, year, MAX(price) AS "maxas"
# FROM cars
# WHERE make NOT IN ('Toyota', 'Mercury', 'Volvo')
# GROUP BY make
# HAVING maxas < 80000
# ORDER BY year;






# # UZDUOCIU SORENDIMAS SU SQLTable
# 1. Mokytojų atlyginimų analizė
# • Suskaičiuokite, kiek yra mokytojų kiekviename dalyke.
# • Atrinkite dalykus, kuriuose dirba daugiau nei 3 mokytojai.
# • Suskaičiuokite vidutinį atlyginimą kiekviename dalyke ir atrinkite tuos, kur vidurkis
# viršija 2500
#
# In [9]: %%sql
#    ...: SELECT dalykas, COUNT(*) AS mokytoju_skaicius FROM mokytojai GROUP BY dalykas;
#    ...:
#    ...:
#  * sqlite:///mokykla.db
# Done.
# Out[9]:
# [('Anglų', 2),
#  ('Biologija', 1),
#  ('Chemija', 2),
#  ('Fizika', 3),
#  ('Istorija', 2),
#  ('Lietuvių', 3),
#  ('Matematika', 5),
#  ('Muzika', 1)]
#
#
# In [11]: %%sql
#     ...: SELECT dalykas, COUNT(*) AS 'mokytoju kiekis' FROM mokytojai GROUP BY dalykas;
#     ...:
#     ...:
#  * sqlite:///mokykla.db
# Done.
# Out[11]:
# [('Anglų', 2),
#  ('Biologija', 1),
#  ('Chemija', 2),
#  ('Fizika', 3),
#  ('Istorija', 2),
#  ('Lietuvių', 3),
#  ('Matematika', 5),
#  ('Muzika', 1)]
#
# In [12]: %%sql
#     ...: SELECT dalykas, COUNT(*) AS 'mokytoju kiekis'
#     ...: FROM mokytojai
#     ...: GROUP BY dalykas
#     ...: HAVING COUNT(*) > 3;
#     ...:
#     ...:
#  * sqlite:///mokykla.db
# Done.
# Out[12]: [('Matematika', 5)]
#
# In [13]:
#
# In [13]: %%sql
#     ...: SELECT dalykas, AVG(atlyginimas) AS 'vidutinė alga'
#     ...: FROM mokytojai
#     ...: GROUP BY dalykas
#     ...: HAVING AVG(atlyginimas) > 2500;
#     ...:
#     ...:
#  * sqlite:///mokykla.db
# Done.
# Out[13]: []
#
# In [14]: %%sql
#     ...: SELECT dalykas, AVG(atlyginimas) AS 'vidutinė alga'
#     ...: FROM mokytojai
#     ...: GROUP BY dalykas
#     ...: HAVING AVG(atlyginimas) > 1500;
#     ...:
#     ...:
#  * sqlite:///mokykla.db
# Done.
# Out[14]: [('Anglų', 1650.0), ('Biologija', 1800.0), ('Matematika', 1550.0)]
#
# In [15]: his
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[15], line 1
# ----> 1 his
#
# NameError: name 'his' is not defined
#
# In [16]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///mokykla.db
# %%sql
# SELECT dalykas, COUNT(*) AS mokytoju_skaicius
# FROM dalykai
# GROUP BY dalykas;
# %%sql
# SELECT dalykas, COUNT(*) AS mokytoju_skaicius
# FROM dalykas
# GROUP BY dalykas;
# %%sql
# SELECT vardas, pavarde  AS 'mokytojas'  FROM mokytojai;
# %%sql
# SELECT dalykas, COUNT(*) AS mokytoju_skaicius FROM dalykai GROUP BY dalykas;
# %%sql
# SELECT dalykas, COUNT(*) AS 'mokytoju_skaicius' FROM dalykai GROUP BY dalykas;
# %%sql
# SELECT mokytojai, COUNT(*) FROM dalykas GROUP BY dalykas;
# %%sql
# SELECT dalykas, COUNT(*) AS mokytoju_skaicius FROM mokytojai GROUP BY dalykas;
# %%sql
# SELECT dalykas, COUNT(*) AS mokytoju kiekis FROM mokytojai GROUP BY dalykas;
# %%sql
# SELECT dalykas, COUNT(*) AS 'mokytoju kiekis' FROM mokytojai GROUP BY dalykas;
# %%sql
# SELECT dalykas, COUNT(*) AS 'mokytoju kiekis'
# FROM mokytojai
# GROUP BY dalykas
# HAVING COUNT(*) > 3;
# %%sql
# SELECT dalykas, AVG(atlyginimas) AS 'vidutinė alga'
# FROM mokytojai
# GROUP BY dalykas
# HAVING AVG(atlyginimas) > 2500;
# %%sql
# SELECT dalykas, AVG(atlyginimas) AS 'vidutinė alga'
# FROM mokytojai
# GROUP BY dalykas
# HAVING AVG(atlyginimas) > 1500;
# his
# history


# 2. Brangiausių automobilių analizė
# • Atrinkite brangiausią kiekvieno gamintojo automobilį.
# • Suskaičiuokite vidutinę automobilių kainą kiekvienam gamintojui ir atrinkite tik
# tuos, kurių vidutinė kaina viršija 40 000.
# • Suskaičiuokite, kiek skirtingų spalvų turi kiekvienas gamintojas ir išrikiuokite pagal
# spalvų kiekį mažėjančia tvarka.
#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#    ...:
#
# In [2]: %load_ext sql
#    ...: %sql sqlite:///cars.db
#
# In [3]: %sql SELECT * FROM cars;
#    ...:
#  * sqlite:///cars.db
# Done.
# Out[3]:
# [('Saturn', 'VUE', 'Yellow', 2004, 22408),
#  ('Volvo', 'C30', 'Green', 2011, 15618),
#  ('Hyundai', 'XG350', 'Violet', 2004, 26829),
#  ('Toyota', 'Camry Solara', 'Violet', 2007, 95856),
#  ('Ford', 'F250', 'Crimson', 1998, 1638),
#  ('Audi', '5000S', 'Orange', 1984, 67168),
#  ('Jeep', 'Patriot', 'Violet', 2012, 40333),
#  ('Cadillac', 'Escalade', 'Turquoise', 2010, 89848),
#  ('BMW', 'X6', 'Maroon', 2010, 95169),
#  ('Mercury', 'Grand Marquis', 'Maroon', 2008, 52632),
#  ('Audi', 'V8', 'Red', 1992, 95940),
#  ('Tesla', 'Roadster', 'Violet', 2012, 85425),
#  ('Mercedes-Benz', 'C-Class', None, 1998, 59297),
#  ('Plymouth', 'Colt Vista', 'Puce', 1994, 78124),
#  ('Acura', 'TSX', None, 2011, 41092),
#  ('Kia', 'Forte', 'Blue', 2010, 71514),
#  ('Panoz', 'Esperante', None, 2007, 67409),
#  ('Chevrolet', 'Silverado 1500', 'Puce', 2012, 62033),
#  ('Subaru', 'Outback', 'Turquoise', 2009, 97827),
#  ('Subaru', 'SVX', 'Aquamarine', 1993, 14128),
#  ('Volvo', '850', 'Turquoise', 1995, 34992),
#  ('Mercury', 'Cougar', 'Puce', 1988, 2997),
#  ('Chevrolet', 'Monte Carlo', 'Turquoise', 1996, 62308),
#  ('Pontiac', 'Bonneville', 'Orange', 1991, 94076),
#  ('Ford', 'Fusion', 'Red', 2006, 89698),
#  ('GMC', '3500', 'Red', 1998, 40258),
#  ('Volkswagen', 'Golf', 'Indigo', 1998, 30819),
#  ('Lexus', 'SC', 'Crimson', 2003, 45669),
#  ('Mercury', 'Sable', 'Indigo', 1999, 73840),
#  ('Volvo', 'S40', 'Pink', 2005, 57147),
#  ('Ford', 'Focus', 'Crimson', 2002, 45851),
#  ('Toyota', 'Solara', 'Indigo', 2004, 29817),
#  ('GMC', 'Envoy', 'Blue', 2005, 74711),
#  ('Dodge', 'Viper', 'Green', 2005, 33875),
#  ('Mercury', 'Cougar', 'Crimson', 1984, 13660),
#  ('Land Rover', 'Freelander', 'Turquoise', 2004, 90783),
#  ('Infiniti', 'FX', 'Fuscia', 2003, 38088),
#  ('Mercury', 'Tracer', 'Indigo', 1996, 54304),
#  ('Ford', 'Probe', 'Orange', 1992, 54203),
#  ('Nissan', 'Xterra', 'Teal', 2005, 82388),
#  ('Mazda', 'Mazda6', 'Fuscia', 2013, 85112),
#  ('Dodge', 'Daytona', 'Green', 1993, 18199),
#  ('Jaguar', 'XJ', 'Fuscia', 2010, 78405),
#  ('BMW', '750', 'Orange', 2006, 57629),
#  ('Buick', 'Riviera', 'Aquamarine', 1986, 36976),
#  ('Ford', 'EXP', 'Turquoise', 1985, 31144),
#  ('Lexus', 'ES', 'Orange', 1989, 83231),
#  ('GMC', 'Suburban 1500', 'Puce', 1997, 96533),
#  ('Maybach', '62', 'Red', 2010, 52324),
#  ('BMW', '5 Series', 'Pink', 2001, 8041),
#  ('Subaru', 'A', 'A', 2000, 10000),
#  ('Subaru', 'A', 'Turquoise', 2000, 10000),
#  ('Subaru', 'A3', 'Turquoise', 2000, 20000),
#  ('Subaru', 'A4', 'Turquoise', 2000, 200000)]
#
#
# In [8]: %%sql
#    ...: SELECT make, MAX(price) FROM cars GROUP BY make;
#    ...:
#    ...:
#  * sqlite:///cars.db
# Done.
# Out[8]:
# [('Acura', 41092),
#  ('Audi', 95940),
#  ('BMW', 95169),
#  ('Buick', 36976),
#  ('Cadillac', 89848),
#  ('Chevrolet', 62308),
#  ('Dodge', 33875),
#  ('Ford', 89698),
#  ('GMC', 96533),
#  ('Hyundai', 26829),
#  ('Infiniti', 38088),
#  ('Jaguar', 78405),
#  ('Jeep', 40333),
#  ('Kia', 71514),
#  ('Land Rover', 90783),
#  ('Lexus', 83231),
#  ('Maybach', 52324),
#  ('Mazda', 85112),
#  ('Mercedes-Benz', 59297),
#  ('Mercury', 73840),
#  ('Nissan', 82388),
#  ('Panoz', 67409),
#  ('Plymouth', 78124),
#  ('Pontiac', 94076),
#  ('Saturn', 22408),
#  ('Subaru', 200000),
#  ('Tesla', 85425),
#  ('Toyota', 95856),
#  ('Volkswagen', 30819),
#  ('Volvo', 57147)]
#
# In [9]: %%sql
#    ...: SELECT make, model, year, AVG(price) AS "maxas"
#    ...: FROM cars
#    ...: GROUP BY make
#    ...: HAVING maxas > 40000
#    ...: ORDER BY year;
#    ...:
#    ...:
#  * sqlite:///cars.db
# Done.
# Out[9]:
# [('Audi', '5000S', 1984, 81554.0),
#  ('Pontiac', 'Bonneville', 1991, 94076.0),
#  ('Plymouth', 'Colt Vista', 1994, 78124.0),
#  ('Ford', 'F250', 1998, 44506.8),
#  ('GMC', '3500', 1998, 70500.66666666667),
#  ('Mercedes-Benz', 'C-Class', 1998, 59297.0),
#  ('Lexus', 'SC', 2003, 64450.0),
#  ('Land Rover', 'Freelander', 2004, 90783.0),
#  ('Nissan', 'Xterra', 2005, 82388.0),
#  ('Panoz', 'Esperante', 2007, 67409.0),
#  ('Toyota', 'Camry Solara', 2007, 62836.5),
#  ('Subaru', 'Outback', 2009, 58659.166666666664),
#  ('BMW', 'X6', 2010, 53613.0),
#  ('Cadillac', 'Escalade', 2010, 89848.0),
#  ('Jaguar', 'XJ', 2010, 78405.0),
#  ('Kia', 'Forte', 2010, 71514.0),
#  ('Maybach', '62', 2010, 52324.0),
#  ('Acura', 'TSX', 2011, 41092.0),
#  ('Chevrolet', 'Silverado 1500', 2012, 62170.5),
#  ('Jeep', 'Patriot', 2012, 40333.0),
#  ('Tesla', 'Roadster', 2012, 85425.0),
#  ('Mazda', 'Mazda6', 2013, 85112.0)]
#
# In [10]: %%sql
#     ...: SELECT make, COUNT(DISTINCT color) AS "skirtingos spalvos"
#     ...: FROM cars
#     ...: GROUP BY make
#     ...: ORDER BY "skirtingos spalvos" DESC;
#     ...:
#     ...:
#  * sqlite:///cars.db
# Done.
# Out[10]:
# [('Mercury', 4),
#  ('Ford', 4),
#  ('Volvo', 3),
#  ('Subaru', 3),
#  ('GMC', 3),
#  ('BMW', 3),
#  ('Toyota', 2),
#  ('Lexus', 2),
#  ('Chevrolet', 2),
#  ('Audi', 2),
#  ('Volkswagen', 1),
#  ('Tesla', 1),
#  ('Saturn', 1),
#  ('Pontiac', 1),
#  ('Plymouth', 1),
#  ('Nissan', 1),
#  ('Mazda', 1),
#  ('Maybach', 1),
#  ('Land Rover', 1),
#  ('Kia', 1),
#  ('Jeep', 1),
#  ('Jaguar', 1),
#  ('Infiniti', 1),
#  ('Hyundai', 1),
#  ('Dodge', 1),
#  ('Cadillac', 1),
#  ('Buick', 1),
#  ('Panoz', 0),
#  ('Mercedes-Benz', 0),
#  ('Acura', 0)]
