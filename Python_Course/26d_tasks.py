print(' - - - - - - - - - - uzduotis 1 - - - - - - - - - - - - - - - - - - ')

# 1. Lentelės kūrimas
# Užduotis:
# Sukurkite naują lentelę teacher, kuri turės šiuos stulpelius:
# f_name (TEXT),
# l_name (TEXT),
# email (TEXT),
# subject (TEXT),
# years_experience (INTEGER).
# Įterpkite bent 3 mokytojų įrašus ir patikrinkite, ar lentelė sukurta teisingai.
#
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %%sql
# CREATE TABLE teachers(
#     f_name TEXT,
#     l_name TEXT,
#     email TEXT,
#     subject TEXT,
#     years_experience INTEGER
# );
# %%sql
# CREATE TABLE teachers(
# f_name TEXT,
# l_name TEXT,
# email TEXT,
# subject TEXT,
# years_experience INTEGER
# );
# %%sql sqlite:///teachers.db
# %%sql
# CREATE TABLE teachers(
# f_name TEXT,
# l_name TEXT,
# email TEXT,
# subject TEXT,
# years_experience INTEGER
# )
# %%sql
# INSERT INTO teacher (f_name, l_name, email, subject, years_experience)
# VALUES
#     ('Jonas', 'Petras', 'jonas.petras@email.com', 'Matematika', 10),
#     ('Ieva', 'Smitienė', 'ieva.smitiene@email.com', 'Lietuvių kalba', 5),
#     ('Andrius', 'Jankauskas', 'andrius.jankauskas@email.com', 'Fizika', 8);
# %%sql
# SELECT * FROM teacher;
# %%sql
# SELECT * FROM teachers;
# %%sql
# INSERT INTO teachers (f_name, l_name, email, subject, years_experience)
# VALUES
#     ('Jonas', 'Petras', 'jonas.petras@email.com', 'Matematika', 10),
#     ('Ieva', 'Smitienė', 'ieva.smitiene@email.com', 'Lietuvių kalba', 5),
#     ('Andrius', 'Jankauskas', 'andrius.jankauskas@email.com', 'Fizika', 8);
# %%sql
# SELECT * FROM teachers;
# history
print(' - - - - - - - - - - uzduotis 2 - - - - - - - - - - - - - - - - - - ')

# 2. CONSTRAINTS taikymas
# Užduotis:
# Sukurkite naują lentelę student, kuri turės apribojimus:
# • id (INTEGER, pirminis raktas),
# • f_name (TEXT, negali būti NULL),
# • l_name (TEXT, negali būti NULL),
# • email (TEXT, turi būti unikalus),
# • age (INTEGER, turi būti daugiau nei 6),
# • class (TEXT, numatytoji reikšmė "1A"),
# Įterpkite įrašą su age = 5 ir paaiškinkite, kokią klaidą gavote.
# Įterpkite įrašą be class reikšmės ir patikrinkite, kokia reikšmė bus naudojama.
#
#
# In[1]: %config
# SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In[2]: %load_ext
# sql
#
# In[3]: %sql
# sqlite: // / school.db
#
# In[4]: %%sql
# ...: CREATE
# TABLE
# student(
#     ...: id
# INTEGER
# PRIMARY
# KEY
# UNIQUE,
# ...: f_name
# TEXT
# NOT
# NULL,
# ...: l_name
# TEXT
# NOT
# NULL,
# ...: email
# TEXT
# NOT
# NULL
# UNIQUE,
# ...: age
# INTEGER
# CHECK(age > 6),
# ...:
#
#
# class TEXT DEFAULT '1A'
#
#
# ...: )
# ...:
# ...:
# *sqlite: // / school.db
# Done.
# Out[4]: []
#
# In[5]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(1, 'Pirmokas', 'Pirmukas', 'p5irm@gmail.com', 6, 1A);
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# (sqlite3.OperationalError)
# unrecognized
# token: "1A"
# [SQL: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(1, 'Pirmokas', 'Pirmukas', 'p5irm@gmail.com', 6, 1A);]
# (Background on this error at: https:
#
# // sqlalche.me / e / 20 / e3q8)
#
# In[6]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(1, 'Pirmokas', 'Pirmukas', 'p5irm@gmail.com', 6, '1A');
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# (sqlite3.IntegrityError)
# CHECK
# constraint
# failed: age > 6
# [SQL: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(1, 'Pirmokas', 'Pirmukas', 'p5irm@gmail.com', 6, '1A');]
# (Background on this error at: https:
#
# // sqlalche.me / e / 20 / gkpj)
#
# In[7]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(1, 'Pirmokas', 'Pirmukas', 'p5irm@gmail.com', 7, '1A');
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# 1
# rows
# affected.
# Out[7]: []
#
# In[8]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(2, 'Antrokas', 'Antrukas', 'antm@gmail.com', 5, '2A');
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# (sqlite3.IntegrityError)
# CHECK
# constraint
# failed: age > 6
# [SQL: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(2, 'Antrokas', 'Antrukas', 'antm@gmail.com', 5, '2A');]
# (Background on this error at: https:
#
# // sqlalche.me / e / 20 / gkpj)
#
# In[9]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(2, 'Antrokas', 'Antrukas', 'antm@gmail.com', 8, '2A');
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# 1
# rows
# affected.
# Out[9]: []
#
# In[10]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age)
# VALUES(2, 'Antrokas', 'Antrukas', 'antm@gmail.com', 8, '2A');
# ...:
# ...:
# *sqlite: // / school.db
# (sqlite3.OperationalError)
# 6
# values
# for 5 columns
# [
#       SQL: INSERT INTO student (id, f_name, l_name, email, age) VALUES(2, 'Antrokas', 'Antrukas', 'antm@gmail.com', 8, '2A');]
# (Background on this error at: https: // sqlalche.me / e / 20 / e3q8)
#
# In[11]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(3, 'Treciokas', 'Treciukas', 'tre@gmail.com', 9);
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# (sqlite3.OperationalError)
# 5
# values
# for 6 columns
# [SQL: INSERT INTO student (id, f_name, l_name, email, age,
#
#
# class ) VALUES(3, 'Treciokas', 'Treciukas', 'tre@gmail.com', 9);]
# (Background on this error at: https:
#
# // sqlalche.me / e / 20 / e3q8)
#
# In[12]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age)
# VALUES(3, 'Treciokas', 'Treciukas', 'tre@gmail.com', 9, '3A');
# ...:
# ...:
# *sqlite: // / school.db
# (sqlite3.OperationalError)
# 6
# values
# for 5 columns
# [
#       SQL: INSERT INTO student (id, f_name, l_name, email, age) VALUES(3, 'Treciokas', 'Treciukas', 'tre@gmail.com', 9, '3A');]
# (Background on this error at: https: // sqlalche.me / e / 20 / e3q8)
#
# In[13]: %% sql
# ...: INSERT
# INTO
# student(id, f_name, l_name, email, age,
#
#
# class ) VALUES(3, 'Treciokas', 'Treciukas', 'tre@gmail.com', 9, '3A');
# ...:
#     ...:
#     *sqlite
#
# : // / school.db
# 1
# rows
# affected.
# Out[13]: []
#
# In[14]: %% sql
# ...: SELECT * FROM
# student;
# ...:
# ...:
# *sqlite: // / school.db
# Done.
# Out[14]:
# [(1, 'Pirmokas', 'Pirmukas', 'p5irm@gmail.com', 7, '1A'),
# (2, 'Antrokas', 'Antrukas', 'antm@gmail.com', 8, '2A'),
# (3, 'Treciokas', 'Treciukas', 'tre@gmail.com', 9, '3A')]


print(' - - - - - - - - - - -  - - - - - uzduotis 3 - - - - - - - - - - -  - - - - - - - - - - - - ')

# # 3. ALTER TABLE naudojimas
# # Užduotis:
# # 1. Pridėkite naują stulpelį gender į student lentelę (TEXT, gali būti NULL).
# # 2. Pervadinkite stulpelį class į grade.
# # 3. Ištrinkite stulpelį email iš teacher lentelės.
# # 4. Naudokite PRAGMA table_info(student); ir patikrinkite atliktus pakeitimus.
#
#
# In [15]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///school.db
# %sql SELECT * FROM student;
# %%sql
# ALTER TABLE student
# ADD COLUMN gender TEXT NULL;
# %sql SELECT * FROM student;
# %sql ALTER TABLE student RENAME COLUMN class to grade;
# %sql SELECT * FROM student;
# %sql SELECT * FROM teacher;
# %sql ALTER TABLE teacher DROP COLUMN email;
# %sql SELECT * FROM teacher;
# %sql PRAG,A table_info(student)
# %sql PRAGMA table_info(student)
# %sql PRAGMA table_info(teacher)
# history


print(' - - - - - - - - - - -  - - - - - uzduotis 4 - - - - - - - - - - -  - - - - - - - - - - - - ')

# Papildoma didesnio sudėtingumo užduotis:
# Užduotis: Mokykloje nuspręsta kaupti informaciją apie tėvus. Sukurkite lentelę parent,
# kuri turės:
# • id (INTEGER, pirminis raktas),
# • f_name (TEXT, negali būti NULL),
# • l_name (TEXT, negali būti NULL),
# • phone (TEXT, turi būti unikalus),
# 1. Sukurkite bent 3 tėvų įrašus.
# 2. Bandykite įvesti du tėvus su tuo pačiu phone numeriu – kokia klaida bus išmesta?




