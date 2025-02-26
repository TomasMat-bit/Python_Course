# (.venv) PS C:\Users\PROMAR\Desktop\STUDIJOS\Python> ipython
# Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///cars.db
#
# In [4]: exit
# (.venv) PS C:\Users\PROMAR\Desktop\STUDIJOS\Python> ipython
# Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///personal_cars.db
#
# In [4]: %%sql
#    ...: SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[4]:
# [('car', 'CREATE TABLE car (\r\n\tid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\r\n\tmake VARCHAR(50),\r\n\tmodel VARCHAR(50),\r\n\tplate VARCHAR(50)\r\n)'),
#  ('company', 'CREATE TABLE company (\r\n\tid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\r\n\tname VARCHAR(50)\r\n)'),
#  ('person', 'CREATE TABLE person (\r\n\tid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\r\n\tfirst_name VARCHAR(50),\r\n\tlast_name VARCHAR(50),\r\n\temail  ... (5 characters truncated) ... AR(50),\r\n\tcar_id INT,\r\n\tcompany_id INT,\r\n\tFOREIGN KEY (car_id) REFERENCES car(id),\r\n\tFOREIGN KEY (company_id) REFERENCES company(id)\r\n)')]
#
# In [5]:  SELECT * FROM car;
#   Cell In[5], line 1
#     SELECT * FROM car;
#                   ^
# SyntaxError: invalid syntax
#
#
# In [6]: %%sql
#    ...: SELECT * FROM car;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[6]:
# [(1, 'BMW', 'M3', 'LNP 014 '),
#  (2, 'Kia', 'Spectra', 'FRJ 254 '),
#  (3, 'Ford', 'Escape', 'YUJ 630 '),
#  (4, 'Suzuki', 'XL-7', 'AWF 961 '),
#  (5, 'Hyundai', 'Accent', 'ZPG 590 '),
#  (6, 'Ford', 'F150', 'LND 949 '),
#  (7, 'Volvo', 'C70', 'JVC 825 '),
#  (8, 'Ford', 'Aspire', 'VTQ 735 '),
#  (9, 'Chevrolet', 'Impala', 'CTF 751 '),
#  (10, 'Mercury', 'Mariner', 'QMI 970 '),
#  (11, 'Ford', 'Escape', 'KUO 362 '),
#  (12, 'Land Rover', 'Freelander', 'HPS 491 '),
#  (13, 'Chrysler', 'Concorde', 'DJK 821 '),
#  (14, 'Buick', 'Century', 'YZD 474 ')]
#
# In [7]: %%sql
#    ...: SELECT * FROM car LIMIT 3;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[7]:
# [(1, 'BMW', 'M3', 'LNP 014 '),
#  (2, 'Kia', 'Spectra', 'FRJ 254 '),
#  (3, 'Ford', 'Escape', 'YUJ 630 ')]
#
# In [8]: %%sql
#    ...: SELECT * FROM person LIMIT 8;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[8]:
# [(1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1),
#  (2, 'Claudetta', 'Dewey', 'cdewey1@mit.edu', 4, 3),
#  (3, 'Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 3, 4),
#  (4, 'Andras', 'Brownsea', 'abrownsea3@webnode.com', 12, 5),
#  (5, 'Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 9, 5),
#  (6, 'Lenore', 'Whatson', 'lwhatson5@diigo.com', 11, 4),
#  (7, 'Shelba', 'Gummer', 'sgummer6@devhub.com', 1, 5),
#  (8, 'Nanny', 'Severns', 'nseverns7@cnbc.com', 7, 5)]
#
# In [9]: %%sql
#    ...: SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[9]:
# [('car', 'CREATE TABLE car (\r\n\tid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\r\n\tmake VARCHAR(50),\r\n\tmodel VARCHAR(50),\r\n\tplate VARCHAR(50)\r\n)'),
#  ('company', 'CREATE TABLE company (\r\n\tid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\r\n\tname VARCHAR(50)\r\n)'),
#  ('person', 'CREATE TABLE person (\r\n\tid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\r\n\tfirst_name VARCHAR(50),\r\n\tlast_name VARCHAR(50),\
# r\n\temail  ... (5 characters truncated) ... AR(50),\r\n\tcar_id INT,\r\n\tcompany_id INT,\r\n\tFOREIGN KEY (car_id) REFERENCES car(id),\r\n\tFOREIGN KEY (company_id) REFERENCES company(id)\r\n)')]
#
# In [10]: %%sql
#     ...: SELECT first_name, car_id, company_id  FROM person WHERE id=1;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[10]: [('Innis', 10, 1)]
#
# In [11]: %%sql
#     ...: SELECT * FROM company;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[11]: [(1, 'Google'), (2, 'Facebook'), (3, 'Amazon'), (4, 'Apple'), (5, 'Netflix')]
#
# In [12]: %%scl
#     ...: SELECT * FROM person, car WHERE person.car_id=car.id;
#     ...:
#     ...:
# UsageError: Cell magic `%%scl` not found.
#
# In [13]: %%sql
#     ...: SELECT * FROM person, car WHERE person.car_id=car.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[13]:
# [(1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 10, 'Mercury', 'Mariner', 'QMI 970 '),
#  (2, 'Claudetta', 'Dewey', 'cdewey1@mit.edu', 4, 3, 4, 'Suzuki', 'XL-7', 'AWF 961 '),
#  (3, 'Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 3, 4, 3, 'Ford', 'Escape', 'YUJ 630 '),
#  (4, 'Andras', 'Brownsea', 'abrownsea3@webnode.com', 12, 5, 12, 'Land Rover', 'Freelander', 'HPS 491 '),
#  (5, 'Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 9, 5, 9, 'Chevrolet', 'Impala', 'CTF 751 '),
#  (6, 'Lenore', 'Whatson', 'lwhatson5@diigo.com', 11, 4, 11, 'Ford', 'Escape', 'KUO 362 '),
#  (7, 'Shelba', 'Gummer', 'sgummer6@devhub.com', 1, 5, 1, 'BMW', 'M3', 'LNP 014 '),
#  (8, 'Nanny', 'Severns', 'nseverns7@cnbc.com', 7, 5, 7, 'Volvo', 'C70', 'JVC 825 '),
#  (9, 'Irvine', 'Kenewell', 'ikenewell8@cnn.com', 2, 3, 2, 'Kia', 'Spectra', 'FRJ 254 '),
#  (10, 'Randy', 'Hanscomb', 'rhanscomb9@dagondesign.com', 13, 4, 13, 'Chrysler', 'Concorde', 'DJK 821 '),
#  (11, 'Dun', 'Zarfai', 'dzarfaia@istockphoto.com', 5, 5, 5, 'Hyundai', 'Accent', 'ZPG 590 '),
#  (12, 'Regan', 'Halliday', 'rhallidayb@mlb.com', 14, 1, 14, 'Buick', 'Century', 'YZD 474 '),
#  (14, 'Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 8, 2, 8, 'Ford', 'Aspire', 'VTQ 735 '),
#  (16, 'Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 6, 3, 6, 'Ford', 'F150', 'LND 949 ')]
#
# In [14]: %%sql
#     ...: SELECT * FROM person where car_id IS NULL;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[14]:
# [(13, 'Abbott', 'Sharphurst', 'asharphurstc@boston.com', None, 1),
#  (15, 'Drucy', 'Whittles', 'dwhittlese@bbb.org', None, 5)]
#
# In [15]: %%sql
#     ...: SELECT * FROM ca, person, company
#     ...: WHEHE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) near "person": syntax error
# [SQL: SELECT * FROM ca, person, company
# WHEHE person.car_id=car.id AND person.company_id=company.id;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [16]: %%sql
#     ...: SELECT * FROM person, car, company
#     ...: WHEHE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) near "person": syntax error
# [SQL: SELECT * FROM person, car, company
# WHEHE person.car_id=car.id AND person.company_id=company.id;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [17]: %%sql
#     ...: SELECT * FROM person, car, company;
#     ...: WHEHE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# (sqlite3.OperationalError) near "WHEHE": syntax error
# [SQL: WHEHE person.car_id=car.id AND person.company_id=company.id;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [18]: %%sql
#     ...: SELECT * FROM person, car, company
#     ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[18]:
# [(1, 'Innis', 'Netley', 'inetley0@cornell.edu', 10, 1, 10, 'Mercury', 'Mariner', 'QMI 970 ', 1, 'Google'),
#  (2, 'Claudetta', 'Dewey', 'cdewey1@mit.edu', 4, 3, 4, 'Suzuki', 'XL-7', 'AWF 961 ', 3, 'Amazon'),
#  (3, 'Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 3, 4, 3, 'Ford', 'Escape', 'YUJ 630 ', 4, 'Apple'),
#  (4, 'Andras', 'Brownsea', 'abrownsea3@webnode.com', 12, 5, 12, 'Land Rover', 'Freelander', 'HPS 491 ', 5, 'Netflix'),
#  (5, 'Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 9, 5, 9, 'Chevrolet', 'Impala', 'CTF 751 ', 5, 'Netflix'),
#  (6, 'Lenore', 'Whatson', 'lwhatson5@diigo.com', 11, 4, 11, 'Ford', 'Escape', 'KUO 362 ', 4, 'Apple'),
#  (7, 'Shelba', 'Gummer', 'sgummer6@devhub.com', 1, 5, 1, 'BMW', 'M3', 'LNP 014 ', 5, 'Netflix'),
#  (8, 'Nanny', 'Severns', 'nseverns7@cnbc.com', 7, 5, 7, 'Volvo', 'C70', 'JVC 825 ', 5, 'Netflix'),
#  (9, 'Irvine', 'Kenewell', 'ikenewell8@cnn.com', 2, 3, 2, 'Kia', 'Spectra', 'FRJ 254 ', 3, 'Amazon'),
#  (10, 'Randy', 'Hanscomb', 'rhanscomb9@dagondesign.com', 13, 4, 13, 'Chrysler', 'Concorde', 'DJK 821 ', 4, 'Apple'),
#  (11, 'Dun', 'Zarfai', 'dzarfaia@istockphoto.com', 5, 5, 5, 'Hyundai', 'Accent', 'ZPG 590 ', 5, 'Netflix'),
#  (12, 'Regan', 'Halliday', 'rhallidayb@mlb.com', 14, 1, 14, 'Buick', 'Century', 'YZD 474 ', 1, 'Google'),
#  (14, 'Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 8, 2, 8, 'Ford', 'Aspire', 'VTQ 735 ', 2, 'Facebook'),
#  (16, 'Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 6, 3, 6, 'Ford', 'F150', 'LND 949 ', 3, 'Amazon')]
#
# In [19]: %%sql
#     ...: SELECT person.first_name, person.last_name, person.email, car.name, car.model, car.plate, company.name
#     ...: FROM person, car, company
#     ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) no such column: car.name
# [SQL: SELECT person.first_name, person.last_name, person.email, car.name, car.model, car.plate, company.name
# FROM person, car, company
# WHERE person.car_id=car.id AND person.company_id=company.id;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [20]: %%sql
#     ...: SELECT person.first_name, person.last_name, person.email, car.make, car.model, car.plate, company.name
#     ...: FROM person, car, company
#     ...: WHERE person.car_id=car.id AND person.company_id=company.id;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[20]:
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
# In [21]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///personal_cars.db
# %%sql
# SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
#  SELECT * FROM car;
# %%sql
# SELECT * FROM car;
# %%sql
# SELECT * FROM car LIMIT 3;
# %%sql
# SELECT * FROM person LIMIT 8;
# %%sql
# SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
# %%sql
# SELECT first_name, car_id, company_id  FROM person WHERE id=1;
# %%sql
# SELECT * FROM company;
# %%scl
# SELECT * FROM person, car WHERE person.car_id=car.id;
# %%sql
# SELECT * FROM person, car WHERE person.car_id=car.id;
# %%sql
# SELECT * FROM person where car_id IS NULL;
# %%sql
# SELECT * FROM ca, person, company
# WHEHE person.car_id=car.id AND person.company_id=company.id;
# %%sql
# SELECT * FROM person, car, company
# WHEHE person.car_id=car.id AND person.company_id=company.id;
# %%sql
# SELECT * FROM person, car, company;
# WHEHE person.car_id=car.id AND person.company_id=company.id;
# %%sql
# SELECT * FROM person, car, company
# WHERE person.car_id=car.id AND person.company_id=company.id;
# %%sql
# SELECT person.first_name, person.last_name, person.email, car.name, car.model, car.plate, company.name
# FROM person, car, company
# WHERE person.car_id=car.id AND person.company_id=company.id;
# %%sql
# SELECT person.first_name, person.last_name, person.email, car.make, car.model, car.plate, company.name
# FROM person, car, company
# WHERE person.car_id=car.id AND person.company_id=company.id;
# ------------------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------------------
print(' - - - - - - - - - - - - - JOIN & GRUPAVIMAS - - -- - - - - - - - - - - - - - - ')

# (.venv) PS C:\Users\PROMAR\Desktop\STUDIJOS\Python> ipython
# Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
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
#
# In [8]: exit
# (.venv) PS C:\Users\PROMAR\Desktop\STUDIJOS\Python> ipython
# Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.
#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///personal_cars.db
#
# In [4]: %%sql
#    ...: SELECT first_name, last_name, email, make, model, plate
#    ...: FROM person
#    ...: JOIN var ON person.car_id=car.id;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) no such table: var
# [SQL: SELECT first_name, last_name, email, make, model, plate
# FROM person
# JOIN var ON person.car_id=car.id;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [5]: %%sql
#    ...: SELECT first_name, last_name, email, make, model, plate
#    ...: FROM person
#    ...: JOIN car ON person.car_id=car.id;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[5]:
# [('Innis', 'Netley', 'inetley0@cornell.edu', 'Mercury', 'Mariner', 'QMI 970 '),
#  ('Claudetta', 'Dewey', 'cdewey1@mit.edu', 'Suzuki', 'XL-7', 'AWF 961 '),
#  ('Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 'Ford', 'Escape', 'YUJ 630 '),
#  ('Andras', 'Brownsea', 'abrownsea3@webnode.com', 'Land Rover', 'Freelander', 'HPS 491 '),
#  ('Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 'Chevrolet', 'Impala', 'CTF 751 '),
#  ('Lenore', 'Whatson', 'lwhatson5@diigo.com', 'Ford', 'Escape', 'KUO 362 '),
#  ('Shelba', 'Gummer', 'sgummer6@devhub.com', 'BMW', 'M3', 'LNP 014 '),
#  ('Nanny', 'Severns', 'nseverns7@cnbc.com', 'Volvo', 'C70', 'JVC 825 '),
#  ('Irvine', 'Kenewell', 'ikenewell8@cnn.com', 'Kia', 'Spectra', 'FRJ 254 '),
#  ('Randy', 'Hanscomb', 'rhanscomb9@dagondesign.com', 'Chrysler', 'Concorde', 'DJK 821 '),
#  ('Dun', 'Zarfai', 'dzarfaia@istockphoto.com', 'Hyundai', 'Accent', 'ZPG 590 '),
#  ('Regan', 'Halliday', 'rhallidayb@mlb.com', 'Buick', 'Century', 'YZD 474 '),
#  ('Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 'Ford', 'Aspire', 'VTQ 735 '),
#  ('Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 'Ford', 'F150', 'LND 949 ')]
#
# In [6]: %%sql
#    ...: SELECT first_name, last_name, email, make, model, plate
#    ...: FROM person
#    ...: JOIN car ON person.car_id=car.id
#    ...: ORDER BY make;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[6]:
# [('Shelba', 'Gummer', 'sgummer6@devhub.com', 'BMW', 'M3', 'LNP 014 '),
#  ('Regan', 'Halliday', 'rhallidayb@mlb.com', 'Buick', 'Century', 'YZD 474 '),
#  ('Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 'Chevrolet', 'Impala', 'CTF 751 '),
#  ('Randy', 'Hanscomb', 'rhanscomb9@dagondesign.com', 'Chrysler', 'Concorde', 'DJK 821 '),
#  ('Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 'Ford', 'Escape', 'YUJ 630 '),
#  ('Lenore', 'Whatson', 'lwhatson5@diigo.com', 'Ford', 'Escape', 'KUO 362 '),
#  ('Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 'Ford', 'Aspire', 'VTQ 735 '),
#  ('Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 'Ford', 'F150', 'LND 949 '),
#  ('Dun', 'Zarfai', 'dzarfaia@istockphoto.com', 'Hyundai', 'Accent', 'ZPG 590 '),
#  ('Irvine', 'Kenewell', 'ikenewell8@cnn.com', 'Kia', 'Spectra', 'FRJ 254 '),
#  ('Andras', 'Brownsea', 'abrownsea3@webnode.com', 'Land Rover', 'Freelander', 'HPS 491 '),
#  ('Innis', 'Netley', 'inetley0@cornell.edu', 'Mercury', 'Mariner', 'QMI 970 '),
#  ('Claudetta', 'Dewey', 'cdewey1@mit.edu', 'Suzuki', 'XL-7', 'AWF 961 '),
#  ('Nanny', 'Severns', 'nseverns7@cnbc.com', 'Volvo', 'C70', 'JVC 825 ')]
#
# In [7]: %%sql
#    ...: SELECT first_name, last_name, email, make, model, plate
#    ...: FROM person
#    ...: JOIN car ON person.car_id=car.id
#    ...: JOIN company ON person.company_id=company.id
#    ...: ORDER BY name;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[7]:
# [('Claudetta', 'Dewey', 'cdewey1@mit.edu', 'Suzuki', 'XL-7', 'AWF 961 '),
#  ('Irvine', 'Kenewell', 'ikenewell8@cnn.com', 'Kia', 'Spectra', 'FRJ 254 '),
#  ('Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 'Ford', 'F150', 'LND 949 '),
#  ('Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 'Ford', 'Escape', 'YUJ 630 '),
#  ('Lenore', 'Whatson', 'lwhatson5@diigo.com', 'Ford', 'Escape', 'KUO 362 '),
#  ('Randy', 'Hanscomb', 'rhanscomb9@dagondesign.com', 'Chrysler', 'Concorde', 'DJK 821 '),
#  ('Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 'Ford', 'Aspire', 'VTQ 735 '),
#  ('Innis', 'Netley', 'inetley0@cornell.edu', 'Mercury', 'Mariner', 'QMI 970 '),
#  ('Regan', 'Halliday', 'rhallidayb@mlb.com', 'Buick', 'Century', 'YZD 474 '),
#  ('Andras', 'Brownsea', 'abrownsea3@webnode.com', 'Land Rover', 'Freelander', 'HPS 491 '),
#  ('Philippe', 'Longhirst', 'plonghirst4@paginegialle.it', 'Chevrolet', 'Impala', 'CTF 751 '),
#  ('Shelba', 'Gummer', 'sgummer6@devhub.com', 'BMW', 'M3', 'LNP 014 '),
#  ('Nanny', 'Severns', 'nseverns7@cnbc.com', 'Volvo', 'C70', 'JVC 825 '),
#  ('Dun', 'Zarfai', 'dzarfaia@istockphoto.com', 'Hyundai', 'Accent', 'ZPG 590 ')]
#
# In [8]: %%sql
#    ...: SELECT first_name, last_name, email, make, model, plate
#    ...: FROM person
#    ...: JOIN car ON person.car_id=car.id
#    ...: JOIN company ON person.company_id=company.id
#    ...: WHERE make='Ford'
#    ...: ORDER BY name;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[8]:
# [('Frankie', 'Yaknov', 'fyaknovf@bandcamp.com', 'Ford', 'F150', 'LND 949 '),
#  ('Carri', 'Sharpus', 'csharpus2@telegraph.co.uk', 'Ford', 'Escape', 'YUJ 630 '),
#  ('Lenore', 'Whatson', 'lwhatson5@diigo.com', 'Ford', 'Escape', 'KUO 362 '),
#  ('Westbrook', 'Stirtle', 'wstirtled@ustream.tv', 'Ford', 'Aspire', 'VTQ 735 ')]
#
# In [9]: %%sql
#    ...: SELECT name, COUNT() AS 'people'
#    ...: FROM person
#    ...: JOIN company ON person.company_id=company.id
#    ...: GROUP BY name
#    ...: ORDER BY people DESC;
#    ...:
#    ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[9]: [('Netflix', 6), ('Google', 3), ('Apple', 3), ('Amazon', 3), ('Facebook', 1)]
#
# In [10]: %%sql
#     ...: SELECT name, COUNT() AS 'people'
#     ...: FROM person
#     ...: JOIN company ON person.company_id=company.id
#     ...: GROUP BY name
#     ...: HAVING people > 3;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[10]: [('Netflix', 6)]
#
# In [11]: %%sql
#     ...: SELECT name, COUNT(person.car_id)
#     ...: FROM person
#     ...: JOIN company ON person.company_id=company.id
#     ...: GROUP BY name;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[11]: [('Amazon', 3), ('Apple', 3), ('Facebook', 1), ('Google', 2), ('Netflix', 5)]
#
# In [12]: %%sql
#     ...: SELECT name COUNT() AS 'autos'
#     ...: FROM person
#     ...: JOIN company ON person.company_id=company.id
#     ...: JOIN car ON person.car_id=car.id
#     ...: GROUP BY name
#     ...: HAVING autos > 2
#     ...: ORDER BY COUNT() DESC;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# (sqlite3.OperationalError) near "(": syntax error
# [SQL: SELECT name COUNT() AS 'autos'
# FROM person
# JOIN company ON person.company_id=company.id
# JOIN car ON person.car_id=car.id
# GROUP BY name
# HAVING autos > 2
# ORDER BY COUNT() DESC;]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [13]: %%sql
#     ...: SELECT name, COUNT() AS 'autos'
#     ...: FROM person
#     ...: JOIN company ON person.company_id=company.id
#     ...: JOIN car ON person.car_id=car.id
#     ...: GROUP BY name
#     ...: HAVING autos > 2
#     ...: ORDER BY COUNT() DESC;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[13]: [('Netflix', 5), ('Apple', 3), ('Amazon', 3)]
#
# In [14]: %%sql
#     ...: SELECT name, COUNT() AS 'autos'
#     ...: FROM person
#     ...: JOIN company ON person.company_id=company.id
#     ...: JOIN car ON person.car_id=car.id
#     ...: GROUP BY name
#     ...: HAVING autos > 2
#     ...: ORDER BY COUNT() ASC;
#     ...:
#     ...:
#  * sqlite:///personal_cars.db
# Done.
# Out[14]: [('Amazon', 3), ('Apple', 3), ('Netflix', 5)]
#
# In [15]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///personal_cars.db
# %%sql
# SELECT first_name, last_name, email, make, model, plate
# FROM person
# JOIN var ON person.car_id=car.id;
# %%sql
# SELECT first_name, last_name, email, make, model, plate
# FROM person
# JOIN car ON person.car_id=car.id;
# %%sql
# SELECT first_name, last_name, email, make, model, plate
# FROM person
# JOIN car ON person.car_id=car.id
# ORDER BY make;
# %%sql
# SELECT first_name, last_name, email, make, model, plate
# FROM person
# JOIN car ON person.car_id=car.id
# JOIN company ON person.company_id=company.id
# ORDER BY name;
# %%sql
# SELECT first_name, last_name, email, make, model, plate
# FROM person
# JOIN car ON person.car_id=car.id
# JOIN company ON person.company_id=company.id
# WHERE make='Ford'
# ORDER BY name;
# %%sql
# SELECT name, COUNT() AS 'people'
# FROM person
# JOIN company ON person.company_id=company.id
# GROUP BY name
# ORDER BY people DESC;
# %%sql
# SELECT name, COUNT() AS 'people'
# FROM person
# JOIN company ON person.company_id=company.id
# GROUP BY name
# HAVING people > 3;
# %%sql
# SELECT name, COUNT(person.car_id)
# FROM person
# JOIN company ON person.company_id=company.id
# GROUP BY name;
# %%sql
# SELECT name COUNT() AS 'autos'
# FROM person
# JOIN company ON person.company_id=company.id
# JOIN car ON person.car_id=car.id
# GROUP BY name
# HAVING autos > 2
# ORDER BY COUNT() DESC;
# %%sql
# SELECT name, COUNT() AS 'autos'
# FROM person
# JOIN company ON person.company_id=company.id
# JOIN car ON person.car_id=car.id
# GROUP BY name
# HAVING autos > 2
# ORDER BY COUNT() DESC;
# %%sql
# SELECT name, COUNT() AS 'autos'
# FROM person
# JOIN company ON person.company_id=company.id
# JOIN car ON person.car_id=car.id
# GROUP BY name
# HAVING autos > 2
# ORDER BY COUNT() ASC;
# history



# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///personal_cars.db
#
# In [4]: %%sql
#    ...: SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
