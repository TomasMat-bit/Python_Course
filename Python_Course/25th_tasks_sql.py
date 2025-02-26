print(' - - - - - - - - - - - - - uzduotis 1 - - -- - - - - - - - - - - - - - - ')

# 1. Lentelių peržiūra ir analizė
# 1. Peržiūrėkite visų lentelių struktūrą ir išsiaiškinkite, kokius duomenis jos saugo.
# 2. Atrinkite 10 pirmųjų įrašų iš kiekvienos lentelės (person, car, company).
# 3. Atraskite visus unikalius automobilių gamintojus (make) iš car lentelės.

# In [23]: %%sql
#     ...: SELECT * FROM person, car, company LIMIT 10;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[23]:
# [(1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 1, 'BMW', 'M3', 'LNP 014 ', 1, 'Google'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 1, 'BMW', 'M3', 'LNP 014 ', 2, 'Facebook'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 1, 'BMW', 'M3', 'LNP 014 ', 3, 'Amazon'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 1, 'BMW', 'M3', 'LNP 014 ', 4, 'Apple'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 1, 'BMW', 'M3', 'LNP 014 ', 5, 'Netflix'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 2, 'Kia', 'Spectra', 'FRJ 254 ', 1, 'Google'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 2, 'Kia', 'Spectra', 'FRJ 254 ', 2, 'Facebook'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 2, 'Kia', 'Spectra', 'FRJ 254 ', 3, 'Amazon'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 2, 'Kia', 'Spectra', 'FRJ 254 ', 4, 'Apple'),
#  (1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 2, 'Kia', 'Spectra', 'FRJ 254 ', 5, 'Netflix')]
#
# In [24]: %%sql
#     ...: SELECT * FROM car.make;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) no such table: car.make
# [SQL: SELECT * FROM car.make;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [25]: %%sql
#     ...: SELECT car.make
#     ...: FROM car
#     ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) no such column: person.car_id
# [SQL: SELECT car.make
# FROM car
# WHERE person.car_id=car.id AND person.company_id=company.id;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [26]: %%sql
#     ...: SELECT person.first_name, person.last_name, person.email, car.make, car.model, car.plate, company.name
#     ...: FROM person, car, company
#     ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[26]:
# [('Innis', 'Netley', 'inetley0@cornell.edu', 'Mercury', 'Mariner', 'QMI 970 ', 'Google'),
#  ('Claudetta', 'Dewey', 'cdewey1@mit.edu', 'Suzuki', 'XL-7', 'AWF 961 ', 'Amazon'),
#  ('Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 'Ford', 'Escape', 'YUJ 630 ', 'Apple'),
#  ('Andras', 'Brownsea', 'abrownsea3@webnode.com', 'Land Rover', 'Freelander', 'HPS 491 ', 'Netflix'),
#  ('Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 'Chevrolet', 'Impala', 'CTF 751 ', 'Netflix'),
#  ('Lenore', 'Whatson', 'lwhatson5@diigo.com', 'Ford', 'Escape', 'KUO 362 ', 'Apple'),
#  ('Shelba', 'Gummer', 'sgummer6@devhub.com', 'BMW', 'M3', 'LNP 014 ', 'Netflix'),
#  ('Nanny', 'Severns', 'nseverns7@cnbc.com', 'Volvo', 'C70', 'JVC 825 ', 'Netflix'),
#  ('Irvine', 'Kenewell', 'ikenewell8@cnn.com', 'Kia', 'Spectra', 'FRJ 254 ', 'Amazon'),
#  ('Randy', 'Hanscomb', 'rhanscomb9@dagondesign.com', 'Chrysler', 'Concorde', 'DJK 821 ', 'Apple'),
#  ('Dun', 'Zarfai', 'dzarfaia@istockphoto.com', 'Hyundai', 'Accent', 'ZPG 590 ', 'Netflix'),
#  ('Regan', 'Halliday', 'rhallidayb@mlb.com', 'Buick', 'Century', 'YZD 474 ', 'Google'),
#  ('Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 'Ford', 'Aspire', 'VTQ 735 ', 'Facebook'),
#  ('Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 'Ford', 'F150', 'LND 949 ', 'Amazon')]
#
# In [27]: %%sql
#     ...: SELECT car.make
#     ...: FROM person, car, company
#     ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[27]:
# [('Mercury',),
#  ('Suzuki',),
#  ('Ford',),
#  ('Land Rover',),
#  ('Chevrolet',),
#  ('Ford',),
#  ('BMW',),
#  ('Volvo',),
#  ('Kia',),
#  ('Chrysler',),
#  ('Hyundai',),
#  ('Buick',),
#  ('Ford',),
#  ('Ford',)]

print(' - - - - - - - - - - - - - uzduotis 2 - - -- - - - - - - - - - - - - - - ')

# # 2. Lentelių jungimas naudojant WHERE
# # 1. Suraskite visų žmonių vardus, pavardes ir jų vairuojamus automobilius (make,
# # model).
# # 2. Suraskite žmones, kurie neturi priskirto automobilio (car_id IS NULL).
# # 3. Sujunkite visas tris lenteles (person, car, company) ir išveskite žmonių vardus,
# # pavardes, jų automobilius ir kompanijos pavadinimą
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///personal_cars.db
#
# In [4]: %%sql
#    ...: SELECT person.first_name, person.last_name, car.make, car.model
#    ...: FROM person, car, company
#    ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[4]:
# [('Innis', 'Netley', 'Mercury', 'Mariner'),
#  ('Claudetta', 'Dewey', 'Suzuki', 'XL-7'),
#  ('Carri', 'Sharpus', 'Ford', 'Escape'),
#  ('Andras', 'Brownsea', 'Land Rover', 'Freelander'),
#  ('Philippe', 'Longhirst', 'Chevrolet', 'Impala'),
#  ('Lenore', 'Whatson', 'Ford', 'Escape'),
#  ('Shelba', 'Gummer', 'BMW', 'M3'),
#  ('Nanny', 'Severns', 'Volvo', 'C70'),
#  ('Irvine', 'Kenewell', 'Kia', 'Spectra'),
#  ('Randy', 'Hanscomb', 'Chrysler', 'Concorde'),
#  ('Dun', 'Zarfai', 'Hyundai', 'Accent'),
#  ('Regan', 'Halliday', 'Buick', 'Century'),
#  ('Westbrook', 'Stirtle', 'Ford', 'Aspire'),
#  ('Frankie', 'Yaknov', 'Ford', 'F150')]
#
# In [5]:  %%sql
#    ...:     ...: SELECT * FROM person where car_id IS NULL;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[5]:
# [(13, 'Abbott', 'Sharphurst', 'asharphurstc@boston.com', None, 1),
#  (15, 'Drucy', 'Whittles', 'dwhittlese@bbb.org', None, 5)]
#
# In [6]: %%sql
#    ...: SELECT person.first_name, person.last_name, car.make, car.model, company.name
#    ...: FROM person, car, company
#    ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[6]:
# [('Innis', 'Netley', 'Mercury', 'Mariner', 'Google'),
#  ('Claudetta', 'Dewey', 'Suzuki', 'XL-7', 'Amazon'),
#  ('Carri', 'Sharpus', 'Ford', 'Escape', 'Apple'),
#  ('Andras', 'Brownsea', 'Land Rover', 'Freelander', 'Netflix'),
#  ('Philippe', 'Longhirst', 'Chevrolet', 'Impala', 'Netflix'),
#  ('Lenore', 'Whatson', 'Ford', 'Escape', 'Apple'),
#  ('Shelba', 'Gummer', 'BMW', 'M3', 'Netflix'),
#  ('Nanny', 'Severns', 'Volvo', 'C70', 'Netflix'),
#  ('Irvine', 'Kenewell', 'Kia', 'Spectra', 'Amazon'),
#  ('Randy', 'Hanscomb', 'Chrysler', 'Concorde', 'Apple'),
#  ('Dun', 'Zarfai', 'Hyundai', 'Accent', 'Netflix'),
#  ('Regan', 'Halliday', 'Buick', 'Century', 'Google'),
#  ('Westbrook', 'Stirtle', 'Ford', 'Aspire', 'Facebook'),
#  ('Frankie', 'Yaknov', 'Ford', 'F150', 'Amazon')]
#
# In [7]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///personal_cars.db
# %%sql
# SELECT person.first_name, person.last_name, car.make, car.model
# FROM person, car, company
# WHERE person.car_id=car.id AND person.company_id=company.id;
#  %%sql
#     ...: SELECT * FROM person where car_id IS NULL;
# %%sql
# SELECT person.first_name, person.last_name, car.make, car.model, company.name
# FROM person, car, company
# WHERE person.car_id=car.id AND person.company_id=company.id;
# history

print(' - - - - - - - - - - - - - uzduotis 3 - - -- - - - - - - - - - - - - - - ')

# # 3. Lentelių jungimas naudojant JOIN
# # 1. Išveskite žmonių vardus, pavardes ir jų automobilius naudojant JOIN.
# # 2. Rikiuokite rezultatą pagal automobilio markę (make).
# # 3. Pridėkite ir kompanijos pavadinimą į užklausą.
#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///personal_cars.db
#
# In [4]: %%sql
#    ...: SELECT first_name, last_name, make, model, company_name
#    ...: FROM person
#    ...: JOIN car ON person.car_id=car.id
#    ...: JOIN company ON person.company_id=company.id
#    ...: ORDER BY make;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) no such column: company_name
# [SQL: SELECT first_name, last_name, make, model, company_name
# FROM person
# JOIN car ON person.car_id=car.id
# JOIN company ON person.company_id=company.id
# ORDER BY make;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [5]: %%sql
#    ...: SELECT first_name, last_name, make, model, company.name
#    ...: FROM person
#    ...: JOIN car ON person.car_id=car.id
#    ...: JOIN company ON person.company_id=company.id
#    ...: ORDER BY make;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[5]:
# [('Shelba', 'Gummer', 'BMW', 'M3', 'Netflix'),
#  ('Regan', 'Halliday', 'Buick', 'Century', 'Google'),
#  ('Philippe', 'Longhirst', 'Chevrolet', 'Impala', 'Netflix'),
#  ('Randy', 'Hanscomb', 'Chrysler', 'Concorde', 'Apple'),
#  ('Carri', 'Sharpus', 'Ford', 'Escape', 'Apple'),
#  ('Lenore', 'Whatson', 'Ford', 'Escape', 'Apple'),
#  ('Westbrook', 'Stirtle', 'Ford', 'Aspire', 'Facebook'),
#  ('Frankie', 'Yaknov', 'Ford', 'F150', 'Amazon'),
#  ('Dun', 'Zarfai', 'Hyundai', 'Accent', 'Netflix'),
#  ('Irvine', 'Kenewell', 'Kia', 'Spectra', 'Amazon'),
#  ('Andras', 'Brownsea', 'Land Rover', 'Freelander', 'Netflix'),
#  ('Innis', 'Netley', 'Mercury', 'Mariner', 'Google'),
#  ('Claudetta', 'Dewey', 'Suzuki', 'XL-7', 'Amazon'),
#  ('Nanny', 'Severns', 'Volvo', 'C70', 'Netflix')]
#
# In [6]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///personal_cars.db
# %%sql
# SELECT first_name, last_name, make, model, company_name
# FROM person
# JOIN car ON person.car_id=car.id
# JOIN company ON person.company_id=company.id
# ORDER BY make;
# %%sql
# SELECT first_name, last_name, make, model, company.name
# FROM person
# JOIN car ON person.car_id=car.id
# JOIN company ON person.company_id=company.id
# ORDER BY make;
# history

print(' - - - - - - - - - - - - - uzduotis 4 - - -- - - - - - - - - - - - - - - ')

# # 4. Grupavimas ir skaičiavimai
# # 1. Suskaičiuokite, kiek žmonių dirba kiekvienoje kompanijoje.
# # 2. Suskaičiuokite, kiek žmonių neturi priskirto automobilio.

# In [11]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///personal_cars.db
# %%sql
# SELECT name, COUNT() AS 'people'
# FROM person
# JOIN company ON person.company_id=company.id
# GROUP BY name;
# %%sql
# SELECT name, COUNT() AS "autos"
# FROM person
# JOIN company ON person.company_id=company.id
# JOIN car ON person.car_id=car.id
# GROUP BY name
# HAVING autos NULL
# ORDER BY COUNT() DESC;
# %%sql
# SELECT name, COUNT() AS "autos"
# FROM person
# JOIN company ON person.company_id=company.id
# JOIN car ON person.car_id=car.id
# GROUP BY name
# WHERE car_id IS NULL;
# ORDER BY COUNT() DESC;
# %%sql
# SELECT company.name, COUNT(*) AS people_without_cars
# FROM person
# JOIN company ON person.company_id = company.id
# JOIN car ON person.car_id = car.id
# WHERE person.car_id IS NULL
# GROUP BY company.name;
# %%sql
# SELECT company.name, COUNT(person.id) AS darbuotoju_sk
# FROM person
# JOIN company ON person.company_id = company.id
# GROUP BY company.name;
# %%sql
# SELECT company.name, COUNT(*) AS be_auto
# FROM person
# WHERE car_id IS NULL;
# %%sql
# SELECT COUNT(*) AS be_auto
# FROM person
# WHERE car_id IS NULL;
# history


print(' - - - - - - - - - - - - - uzduotis 5 - - -- - - - - - - - - - - - - - - ')

# 5. JOIN variantai (LEFT JOIN, INNER JOIN)
# 1. Raskite visus žmones, įskaitant tuos, kurie neturi automobilio (LEFT JOIN).
#
# In [11]: %%sql
#     ...: SELECT person.first_name, person.last_name, car.make, car.model
#     ...: FROM person
#     ...: LEFT JOIN car ON person.car_id = car.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
#
# 2. Raskite visus žmones, įskaitant tuos, kurie neturi kompanijos (LEFT JOIN).
#
# In [12]: %%sql
#     ...: SELECT person.first_name, person.last_name, company.name AS company_name
#     ...: FROM person
#     ...: LEFT JOIN company ON person.company_id = company.id;
#     ...:
#
# 3. Raskite tik tuos žmones, kurie turi tiek automobilį, tiek priskirtą kompaniją (INNER
# JOIN).
#
# In [14]:  %%sql
#     ...:  SELECT person.first_name, person.last_name, car.make, car.model, company.name AS company_name
#     ...:  FROM person
#     ...:  INNER JOIN car ON person.car_id = car.id
#     ...:  INNER JOIN company ON person.company_id = company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
