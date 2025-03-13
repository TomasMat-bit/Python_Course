# print(' - - - - - - - UZDUOCIU SPRENDIMAS - - - - - - - - - - - - ')
#
# # 1. SQL aplinkos paruošimas
# # Užduotis:
# # Įdiekite reikalingą ipython-sql modulį (pip install ipython-sql).
# # Jupyter Notebook įkelkite SQL plėtinį ir prisijunkite prie mokykla.db duomenų bazės.
# # %load_ext sql
# # %sql sqlite:///mokykla.db
# # Jei neturite duomenų bazės, sukurkite lentelę mokytojai su laukais:
# # • id (pirminis raktas, INTEGER)
# # • vardas (TEXT)
# # • pavarde (TEXT)
# # • dalykas (TEXT)
# # • atlyginimas (INTEGER)
#
# # 2. Duomenų atrinkimas (SELECT)
# # Užduotis:
# # Atrinkite visus mokytojus ir išveskite jų duomenis.
# # Atrinkite mokytojus, kurie dėsto matematiką.
# # %%sql
# # SELECT * FROM mokytojai WHERE dalykas = 'Matematika';
# # Atrinkite mokytojus, kurių atlyginimas didesnis nei 1500.
# # Atrinkite tik mokytojų vardus ir pavardes.
# #
# # 3. Filtravimas su BETWEEN ir IN
# # Užduotis:
# # Atrinkite mokytojus, kurių atlyginimas yra tarp 1000 ir 2000.
# # Atrinkite mokytojus, kurie dėsto "Lietuvių", "Anglų" arba "Istoriją".%%sql
# # SELECT * FROM mokytojai WHERE atlyginimas BETWEEN 1000 AND 2000;
# # Atrinkite mokytojus, kurie dėsto tik gamtos mokslus (pvz., "Biologiją" arba "Chemiją").
# #
# # 4. Paieška pagal teksto fragmentą (LIKE)
# # Užduotis:
# # Atrinkite mokytojus, kurių pavardė prasideda raide "J".
# # Atrinkite mokytojus, kurių vardas baigiasi raide "s".
# # %%sql
# # SELECT * FROM mokytojai WHERE vardas LIKE '%s';
# # Atrinkite mokytojus, kurių antra vardo raidė yra "e".
#
#
# # %%sql
# # INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) (VALUES
# # ('Jonas', 'Jonaitis', 'Matematika', 1600),
# # ('Petras', 'Petraitis', 'Lietuvių', 1400),
# # ('Marius', 'Jankauskas', 'Istorija', 1200),
# # ('Elena', 'Kavaliauskienė', 'Biologija', 1800),
# # ('Simona', 'Simonaitytė', 'Chemija', 1100),
# # ('Rita', 'Juodgalvė', 'Anglų', 2000),
# # ('Tomas', 'Jurgelevičius', 'Matematika', 1700),
# # ('Aistis', 'Bieliauskas', 'Fizika', 900),
# # ('Eglė', 'Žilinskaitė', 'Anglų', 1300),
# # ('Vytas', 'Grigonis', 'Lietuvių', 1550),
# # ('Darius', 'Medelis', 'Chemija', 1450),
# # ('Justina', 'Jakutytė', 'Istorija', 1750),
# # ('Gabrielė', 'Kučinskaitė', 'Matematika', 1250),
# # ('Saulius', 'Januškevičius', 'Fizika', 1900),
# # ('Edvinas', 'Kvedaras', 'Lietuvių', 1000));
#
#
# print('uzduoties sprendimas')
# # %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# # %load_ext sql
# # %sql sqlite:///mokykla.db
# # %%sql
# # CREATE TABLE IF NOT EXISTS mokytojai (
# #     id INTEGER PRIMARY KEY,
# #     vardas TEXT,
# #     pavarde TEXT,
# #     dalykas TEXT,
# #     atlyginimas INTEGER
# # );
# # %%sql
# # INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
# # ('Jonas', 'Jonaitis', 'Matematika', 1600),
# # ('Petras', 'Petraitis', 'Lietuvių', 1400),
# # ('Marius', 'Jankauskas', 'Istorija', 1200),
# # ('Elena', 'Kavaliauskienė', 'Biologija', 1800),
# # ('Simona', 'Simonaitytė', 'Chemija', 1100),
# # ('Rita', 'Juodgalvė', 'Anglų', 2000),
# # ('Tomas', 'Jurgelevičius', 'Matematika', 1700),
# # ('Aistis', 'Bieliauskas', 'Fizika', 900),
# # ('Eglė', 'Žilinskaitė', 'Anglų', 1300),
# # ('Vytas', 'Grigonis', 'Lietuvių', 1550),
# # ('Darius', 'Medelis', 'Chemija', 1450),
# # ('Justina', 'Jakutytė', 'Istorija', 1750),
# # ('Gabrielė', 'Kučinskaitė', 'Matematika', 1250),
# # ('Saulius', 'Januškevičius', 'Fizika', 1900),
# # ('Edvinas', 'Kvedaras', 'Lietuvių', 1000);
# # %%sql
# # SELECT * FROM mokytojai;
# # %%sql
# # SELECT * FROM mokytojai WHERE dalykas = 'Matematika';
# # %%sql
# # SELECT * FROM mokytojai WHERE atlyginimas > 1500;
# # %%sql
# # SELECT vardas, pavarde FROM mokytojai;
# # %%sql
# # SELECT * FROM mokytojai WHERE atlyginimas BETWEEN 1000 AND 2000;
# # %%sql
# # SELECT * FROM mokytojai WHERE dalykas IN ('Lietuvių', 'Anglų', 'Istorija');
# # %%sql
# # SELECT * FROM mokytojai WHERE dalykas IN ('Biologija', 'Chemija');
# # %%sql
# # SELECT * FROM mokytojai WHERE pavarde ILIKE 'J%';
# # %%sql
# # SELECT * FROM mokytojai WHERE pavarde LIKE 'J%';
# # %%sql
# # SELECT * FROM mokytojai WHERE pavarde LIKE '%s';
# # %%sql
# # SELECT * FROM mokytojai WHERE vardas LIKE '%s';
# # %%sql
# # SELECT * FROM mokytojai WHERE vardas LIKE '_e%';
#
# print('KAIP ISSITRAUKTI LENTELES SKYRIU NAMES')
# # In [6]: %sql SELECT sql FROM sqlite_master WHERE type='table' AND name='cars';
# #    ...:
# #    ...:
# #  * sqlite:///cars.db
# # Done.
# # Out[6]: [('CREATE TABLE cars(\r\n\tmake VARCHAR(30),\r\n\tmodel VARCHAR(30),\r\n\tcolor VARCHAR(30),\r\n\tyear INTEGER,\r\n\tprice INTEGER\r\n)',)]
#
# print('--------------------------------')
#
# In [23]: %%sql
#     ...: SELECT * FROM cars ORDER BY price DESC LIMIT  5;
#     ...:
#     ...:
#  * sqlite:///cars.db
# Done.
# Out[23]:
# [('Subaru', 'A4', 'Turquoise', 2000, 200000),
#  ('Subaru', 'Outback', 'Turquoise', 2009, 97827),
#  ('GMC', 'Suburban 1500', 'Puce', 1997, 96533),
#  ('Audi', 'V8', 'Red', 1992, 95940),
#  ('Toyota', 'Camry Solara', 'Violet', 2007, 95856)]
#
# In [24]: %%sql
#     ...: SELECT * FROM cars WHERE make = 'Toyota';
#     ...:
#     ...:
#  * sqlite:///cars.db
# Done.
# Out[24]:
# [('Toyota', 'Camry Solara', 'Violet', 2007, 95856),
#  ('Toyota', 'Solara', 'Indigo', 2004, 29817)]
#
# In [25]: %%sql
#     ...: SELECT * FROM cars WHERE make = 'toyota' COLLATE NOCASE;
#     ...:
#     ...:
#  * sqlite:///cars.db
# Done.
# Out[25]:
# [('Toyota', 'Camry Solara', 'Violet', 2007, 95856),
#  ('Toyota', 'Solara', 'Indigo', 2004, 29817)]
#
# In [26]:
#
#
# print('2nd task answer')
# %load_ext sql
# %sql sqlite:///mokykla.db
# SELECT * FROM mokytojai;
# %sql SELECT * FROM mokytojai;
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %sql SELECT * FROM mokytojai;
# %%sql
# SELECT * FROM mokytojai ORDER BY atlyginimas DESC;
# %%sql
# SELECT * FROM mokytojai ORDER BY pavarde;
# %%sql
# SELECT * FROM mokytojai ORDER BY dalykas ASC, atlyginimas ASC;
# %%sql
# SELECT * FROM mokytojai WHERE dalykas = 'Matematika' AND atlyginimas > 2000;
# %%sql
# SELECT * FROM mokytojai WHERE dalykas = 'Matematika' AND atlyginimas > 1600;
# %%sql
# SELECT * FROM mokytojai WHERE dalykas in ('Fizika', 'Chemija');
# %%sql
# SELECT * FROM mokytojai WHERE dalykas NOT IN ('Lietuvių', 'Istorija');
#
#
#
#
#
#
#
#
#
#
#
#
#
