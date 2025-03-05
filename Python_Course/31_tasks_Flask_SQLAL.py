# Print(' - - - - - - - - - - - UZDUOTIS 1 - - - - - - - - - - - ')

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

# Print(' - - - - - - - - - - - UZDUOTIS 2 - - - - - - - - - - - ')

# 2. Pridėkite duomenų paiešką ir filtravimą
# Užduotis:
# 1. Sukurkite GET formą, kuri leidžia ieškoti mokinų pagal vardą.
# 2. Kai vartotojas įveda paieškos frazę ir paspaudžia „Ieškoti“, turi būti rodomi tik tie
# mokiniai, kurių vardas prasidės įvesta fraze.
# Papildoma užduotis:
# Leiskite naudoti dalinę paiešką (LIKE %fraze%), kad rezultatuose būtų rodomi mokiniai,
# turintys įvestą frazę bet kurioje vardo vietoje.

from flask import Flask, render_template, request
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

@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '')
    if search_query:
        mokiniai = Mokinys.query.filter(Mokinys.vardas.ilike(f'%{search_query}%')).all()
    else:
        mokiniai = Mokinys.query.all()
    return render_template('index_31.html', mokiniai=mokiniai, search_query=search_query)

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

# Print(' - - - - - - - - - - - UZDUOTIS 3 - - - - - - - - - - - ')
