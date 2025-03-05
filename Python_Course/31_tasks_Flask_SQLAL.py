# Print(' - - - - - - - - - - - UZDUOTIS 1 - - - - - - - - - - - ')
# from crypt import methods

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class Mokinys(db.Model):
#     __tablename__ = 'mokinys'
#
#     id = db.Column(db.Integer, primary_key=True)
#     vardas = db.Column(db.String)
#     pavarde = db.Column(db.String)
#     klase = db.Column(db.Integer)
#     sukurimo_data = db.Column(db.DateTime, default=lambda x: datetime.utcnow)
#
#     def __repr__(self):
#         return f'<Mokinys {self.vardas} {self.pavarde}, klase {self.klase}>'
#
# @app.route('/')
# def index():
#     mokiniai = Mokinys.query.all()
#     return render_template('index_31.html', mokiniai=mokiniai)
#
# with app.app_context():
#     db.create_all()
#
# app.run()

# # Print(' - - - - - - - - - - - UZDUOTIS 2 - - - - - - - - - - - ')
#
# # 2. Pridėkite duomenų paiešką ir filtravimą
# # Užduotis:
# # 1. Sukurkite GET formą, kuri leidžia ieškoti mokinų pagal vardą.
# # 2. Kai vartotojas įveda paieškos frazę ir paspaudžia „Ieškoti“, turi būti rodomi tik tie
# # mokiniai, kurių vardas prasidės įvesta fraze.
# # Papildoma užduotis:
# # Leiskite naudoti dalinę paiešką (LIKE %fraze%), kad rezultatuose būtų rodomi mokiniai,
# # turintys įvestą frazę bet kurioje vardo vietoje.
#
# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class Mokinys(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vardas = db.Column(db.String)
#     pavarde = db.Column(db.String)
#     klase = db.Column(db.Integer)
#     sukurimo_data = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f'<Mokinys {self.vardas} {self.pavarde}, klase {self.klase}>'
#
# @app.route('/', methods=['GET'])
# def index():
#     search_query = request.args.get('search', '')
#     if search_query:
#         mokiniai = Mokinys.query.filter(Mokinys.vardas.ilike(f'%{search_query}%')).all()
#     else:
#         mokiniai = Mokinys.query.all()
#     return render_template('index_31.html', mokiniai=mokiniai, search_query=search_query)
#
# with app.app_context():
#     db.create_all()
#     # if not Mokinys.query.first():
#     #     test_mokiniai = [
#     #         Mokinys(vardas='Jonas', pavarde='Jonaitis', klase=5),
#     #         Mokinys(vardas='Petras', pavarde='Petraitis', klase=6),
#     #         Mokinys(vardas='Marius', pavarde='Maraitis', klase=7),
#     #         Mokinys(vardas='Lina', pavarde='Linaitė', klase=5),
#     #         Mokinys(vardas='Austėja', pavarde='Austaitė', klase=8)
#     #     ]
#     #     db.session.bulk_save_objects(test_mokiniai)
#     #     db.session.commit()
#
# app.run()

print(' - - - - - - - - - - - UZDUOTIS 3 - - - - - - - - - - - ')

# 3. Apskaičiuojamas property
# Užduotis:
# 1. Pridėkite metodą @property, kuris kiekvienam mokiniui apskaičiuoja sekančią
# klasė (pvz klasė + 1).
# 2. Pagrindiniame puslapyje atvaizduokite ne tik klasę bet ir sekanti klasė

# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class Mokinys(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vardas = db.Column(db.String)
#     pavarde = db.Column(db.String)
#     klase = db.Column(db.Integer)
#     sukurimo_data = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f'<Mokinys {self.vardas} {self.pavarde}, klase {self.klase}>'
#
#     @property
#     def next_class(self):
#         return self.klase + 1
#
# @app.route('/', methods=['GET'])
# def index():
#     search_query = request.args.get('search', '')
#     if search_query:
#         mokiniai = Mokinys.query.filter(Mokinys.vardas.ilike(f'%{search_query}%')).all()
#     else:
#         mokiniai = Mokinys.query.all()
#     return render_template('index_31.html', mokiniai=mokiniai, search_query=search_query)
#
# with app.app_context():
#     db.create_all()
#     # if not Mokinys.query.first():
#     #     test_mokiniai = [
#     #         Mokinys(vardas='Jonas', pavarde='Jonaitis', klase=5),
#     #         Mokinys(vardas='Petras', pavarde='Petraitis', klase=6),
#     #         Mokinys(vardas='Marius', pavarde='Maraitis', klase=7),
#     #         Mokinys(vardas='Lina', pavarde='Linaitė', klase=5),
#     #         Mokinys(vardas='Austėja', pavarde='Austaitė', klase=8)
#     #     ]
#     #     db.session.bulk_save_objects(test_mokiniai)
#     #     db.session.commit()
#
# app.run()

print(' - - - - - - - - - - - UZDUOTIS 4 - - - - - - - - - - - ')

# 4. Pridėkite naujų projektų įterpimo funkcionalumą (CREATE)
# Užduotis:
# 1. Sukurkite puslapį /prideti-mokini, kuris rodo POST formą su laukais:
# a. Vardas
# b. Pavarde
# c. Klasė
# 2. Kai vartotojas pateikia formą, duomenys turi būti išsaugoti duomenų bazėje.
# Papildoma užduotis:
# Padarykite, kad po mokinio pridėjimo vartotojas būtų nukreiptas atgal į pagrindinį puslapį.

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Mokinys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String)
    pavarde = db.Column(db.String)
    klase = db.Column(db.Integer)
    sukurimo_data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Mokinys {self.vardas} {self.pavarde}, klase {self.klase}>'

    @property
    def next_class(self):
        return self.klase + 1

@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '')
    if search_query:
        mokiniai = Mokinys.query.filter(Mokinys.vardas.ilike(f'%{search_query}%')).all()
    else:
        mokiniai = Mokinys.query.all()
    return render_template('index_31.html', mokiniai=mokiniai, search_query=search_query)

@app.route('/prideti-mokini', methods=['GET', 'POST'])
def prideti_mokini():
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        klase = request.form['klase']

        naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=int(klase))


        db.session.add(naujas_mokinys)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('prideti_mokini.html')


with app.app_context():
    db.create_all()
    # if not Mokinys.query.first():
    #     test_mokiniai = [
    #         Mokinys(vardas='Jonas', pavarde='Jonaitis', klase=5),
    #         Mokinys(vardas='Petras', pavarde='Petraitis', klase=6),
    #         Mokinys(vardas='Marius', pavarde='Maraitis', klase=7),
    #         Mokinys(vardas='Lina', pavarde='Linaitė', klase=5),
    #         Mokinys(vardas='Austėja', pavarde='Austaitė', klase=8)
    #     ]
    #     db.session.bulk_save_objects(test_mokiniai)
    #     db.session.commit()

app.run()