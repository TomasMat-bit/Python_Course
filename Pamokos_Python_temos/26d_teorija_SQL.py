# Pamoka 25 Duomenų bazės projektavimas, constraints
# Duomenų bazės projektavimas, constraints
#
# Duomenų bazės lygmens komandos

#
# In [1]: %config SqlMagic.style = '_DEPRECATED_DEFAULT'
#
# In [2]: %load_ext sql
#
# In [3]: %sql sqlite:///coder.db
#
# In [4]: %sql sqlite:///coder.db
#
# In [5]: %% sql
#    ...: CRETE TABLE coder(
#    ...: f_name TEXT,
#    ...: l_name TEXT,
#    ...: email TEXT,
#    ...: age INTEGER,
#    ...: xp_years INTEGER
#    ...: );
#    ...:
#    ...:
# UsageError: Cell magic `%%` not found.
#
# In [6]: %%sql
#    ...: CRETE TABLE coder(
#    ...: f_name TEXT,
#    ...: l_name TEXT,
#    ...: email TEXT,
#    ...: age INTEGER,
#    ...: xp_years INTEGER
#    ...: );
#    ...:
#    ...:
#  * sqlite:///coder.db
# (sqlite3.OperationalError) near "CRETE": syntax error
# [SQL: CRETE TABLE coder(
# f_name TEXT,
# l_name TEXT,
# email TEXT,
# age INTEGER,
# xp_years INTEGER
# );]
# (Background on this error at: https://sqlalche.me/e/20/e3q8)
#
# In [7]: %%sql
#    ...: CREATE TABLE coder(
#    ...: f_name TEXT,
#    ...: l_name TEXT,
#    ...: email TEXT,
#    ...: age INTEGER,
#    ...: xp_years INTEGER
#    ...: );
#    ...:
#    ...:
#  * sqlite:///coder.db
# Done.
# Out[7]: []
#
# In [8]:
#
# In [8]: %%sql
#    ...: INSERT INTO coder VALUES('Adomas', 'Adomaitis', 'adas@gmail.com', 20, 2);
#    ...:
#    ...:
#    ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[8]: []
#
# In [9]: %%sql
#    ...: INSERT INTO coder VALUES('Darius', 'Dariumas', 'dd@gmail.com', 18, 50);
#    ...:
#    ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[9]: []
#
# In [10]:
#
# In [10]: %%sql
#     ...: INSERT INTO coder VALUES('Tomas', 'Tom', 'tt@gmail.com', 20, 5);
#     ...:
#     ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[10]: []
#
# In [11]: %%sql
#     ...: INSERT INTO coder VALUES('Karolis', 'Kar', 'kk@gmail.com', 25, 5);
#     ...:
#     ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[11]: []
#
# In [12]: %%sql
#     ...: INSERT INTO coder VALUES('Mindaugas', 'Kuzminskis', 'mk@gmail.com', 30, 10);
#     ...:
#     ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[12]: []
#
# In [13]: %%sql
#     ...: INSERT INTO coder VALUES ('Petras', 'Petrauskas', 'pp@gmail.com', NULL, NULL);
#     ...:
#     ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[13]: []
#
# In [14]: %%sql
#     ...: INSERT INTO coder VALUES ('Dalius', 'Dal', NULL, 31, 10);
#     ...:
#     ...:
#  * sqlite:///coder.db
# 1 rows affected.
# Out[14]: []
#
# In [15]: %%sql
#     ...: SELECT * FROM coder;
#     ...:
#     ...:
#  * sqlite:///coder.db
# Done.
# Out[15]:
# [('Adomas', 'Adomaitis', 'adas@gmail.com', 20, 2),
#  ('Darius', 'Dariumas', 'dd@gmail.com', 18, 50),
#  ('Tomas', 'Tom', 'tt@gmail.com', 20, 5),
#  ('Karolis', 'Kar', 'kk@gmail.com', 25, 5),
#  ('Mindaugas', 'Kuzminskis', 'mk@gmail.com', 30, 10),
#  ('Petras', 'Petrauskas', 'pp@gmail.com', None, None),
#  ('Dalius', 'Dal', None, 31, 10)]
#
# In [16]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///coder.db
# %sql sqlite:///coder.db
# %% sql
# CRETE TABLE coder(
# f_name TEXT,
# l_name TEXT,
# email TEXT,
# age INTEGER,
# xp_years INTEGER
# );
# %%sql
# CRETE TABLE coder(
# f_name TEXT,
# l_name TEXT,
# email TEXT,
# age INTEGER,
# xp_years INTEGER
# );
# %%sql
# CREATE TABLE coder(
# f_name TEXT,
# l_name TEXT,
# email TEXT,
# age INTEGER,
# xp_years INTEGER
# );
# %%sql
# INSERT INTO coder VALUES('Adomas', 'Adomaitis', 'adas@gmail.com', 20, 2);
# %%sql
# INSERT INTO coder VALUES('Darius', 'Dariumas', 'dd@gmail.com', 18, 50);
# %%sql
# INSERT INTO coder VALUES('Tomas', 'Tom', 'tt@gmail.com', 20, 5);
# %%sql
# INSERT INTO coder VALUES('Karolis', 'Kar', 'kk@gmail.com', 25, 5);
# %%sql
# INSERT INTO coder VALUES('Mindaugas', 'Kuzminskis', 'mk@gmail.com', 30, 10);
# %%sql
# INSERT INTO coder VALUES ('Petras', 'Petrauskas', 'pp@gmail.com', NULL, NULL);
# %%sql
# INSERT INTO coder VALUES ('Dalius', 'Dal', NULL, 31, 10);
# %%sql
# SELECT * FROM coder;
# history

print('CONSTRAIN TEMA')

# In [16]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///coder.db
# %%sql
# SELECT * FROM coder;
# %%sql
# DROP TABLE IF EXIST coder;
# %sql DROP TABLE IF EXISTS coder;
# %%sql
# CREATE TABLE coder(
# id INTEGER PRIMARY KEY UNIQUE,
# f_name TEXT NOT NULL,
# l_name TEXT NOT NULL,
# email TEXT NOT NULL UNIQUE,
# age INTEGER CHECK (age > 17),
# xp_years INTEGER
# )
# %%sql
# SELECT name, sql FROM sqlite_master WHERE name NOT LIKE "sqlite%";
# %%sql
# INSERT INTO coder VALUES
# ('Jonas', 'Petras', 'jonas.petras@email.com', 10, 10)
# ('Ieva', 'Smitienė', 'ieva.smitiene@email.com', 9, 5),
# ('Andrius', 'Jankauskas', 'andrius.jankauskas@email.com', 7, 8);
# %%sql
# INSERT INTO coder VALUES
# ('Jonas', 'Petras', 'jonas.petras@email.com', 10, 10),
# ('Ieva', 'Smitienė', 'ieva.smitiene@email.com', 9, 5),
# ('Andrius', 'Jankauskas', 'andrius.jankauskas@email.com', 7, 8);
# %%sql
# INSERT INTO coder (id, f_name, l_name, email, age) VALUES(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 12);
# %%sql
# INSERT INTO coder (id, f_name, l_name, email, age) VALUES(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18);
# %%sql
# INSERT INTO coder (id, f_name, l_name, email, age, xp_years) VALUES(2, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18, 2);
# %%sql
# INSERT INTO coder (id, f_name, l_name, email, age, xp_years) VALUES(2, 'Pir5mas', 'P5irmukas', 'p5irm@gmail.com', 18, 2);
# %%sql
# SELECT * FROM coder;
# history

print('Lentelės struktūros keitimas - ALTER TABLE')

# In [3]: %sql sqlite:///coder.db
#
# In [4]: %sql SELECT * FROM coder;
#  * sqlite:///coder.db
# Done.
# Out[4]:
# [(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18, None),
#  (2, 'Pir5mas', 'P5irmukas', 'p5irm@gmail.com', 18, 2)]
#
# In [5]: %sql ALTER TABLE coder DROP COLUMN xp_years;
#  * sqlite:///coder.db
# Done.
# Out[5]: []
#
# In [6]: %sql SELECT * FROM coder;
#  * sqlite:///coder.db
# Done.
# Out[6]:
# [(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18),
#  (2, 'Pir5mas', 'P5irmukas', 'p5irm@gmail.com', 18)]
#
# In [7]: %sql ALTER TABLE coder RENAME COLUMN age to years;
#  * sqlite:///coder.db
# Done.
# Out[7]: []
#
# In [8]: %sql SELECT * FROM coder;
#  * sqlite:///coder.db
# Done.
# Out[8]:
# [(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18),
#  (2, 'Pir5mas', 'P5irmukas', 'p5irm@gmail.com', 18)]
#
# In [9]: %sql SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
#  * sqlite:///coder.db
# Done.
# Out[9]: [('coder', 'CREATE TABLE coder(\nid INTEGER PRIMARY KEY UNIQUE,\nf_name TEXT NOT NULL,\nl_name TEXT NOT NULL,\nemail TEXT NOT NULL UNIQUE,\nyears INTEGER CHECK (years > 17))')]
#
# In [10]: %%sql
#     ...: ALTER TABLE coder ADD COLUMN position;
#     ...:
#     ...:
#  * sqlite:///coder.db
# Done.
# Out[10]: []
#
# In [11]:
#
# In [11]: %%sql
#     ...: SELECT * FROM coder;
#     ...:
#     ...:
#  * sqlite:///coder.db
# Done.
# Out[11]:
# [(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18, None),
#  (2, 'Pir5mas', 'P5irmukas', 'p5irm@gmail.com', 18, None)]
#
# In [12]: %%sql
#     ...: ALTER TABLE coder ADD COLUMN gender DEFAULT 'male';
#     ...:
#     ...:
#  * sqlite:///coder.db
# Done.
# Out[12]: []
#
# In [13]: %sql SELECT * FROM coder;
#  * sqlite:///coder.db
# Done.
# Out[13]:
# [(1, 'Pirmas', 'Pirmukas', 'pirm@gmail.com', 18, None, 'male'),
#  (2, 'Pir5mas', 'P5irmukas', 'p5irm@gmail.com', 18, None, 'male')]
#
# In [14]: %%sql
#     ...: PRAGMA table_info(coder)
#     ...:
#     ...:
#  * sqlite:///coder.db
# Done.
# Out[14]:
# [(0, 'id', 'INTEGER', 0, None, 1),
#  (1, 'f_name', 'TEXT', 1, None, 0),
#  (2, 'l_name', 'TEXT', 1, None, 0),
#  (3, 'email', 'TEXT', 1, None, 0),
#  (4, 'years', 'INTEGER', 0, None, 0),
#  (5, 'position', '', 0, None, 0),
#  (6, 'gender', '', 0, "'male'", 0)]
#
# In [15]: history
# %config SqlMagic.style = '_DEPRECATED_DEFAULT'
# %load_ext sql
# %sql sqlite:///coder.db
# %sql SELECT * FROM coder;
# %sql ALTER TABLE coder DROP COLUMN xp_years;
# %sql SELECT * FROM coder;
# %sql ALTER TABLE coder RENAME COLUMN age to years;
# %sql SELECT * FROM coder;
# %sql SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite%';
# %%sql
# ALTER TABLE coder ADD COLUMN position;
# %%sql
# SELECT * FROM coder;
# %%sql
# ALTER TABLE coder ADD COLUMN gender DEFAULT 'male';
# %sql SELECT * FROM coder;
# %%sql
# PRAGMA table_info(coder)
# history


print('Lentelės struktūros keitimas - ALTER TABLE')
