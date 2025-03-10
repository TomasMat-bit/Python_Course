from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modeliai
class Darboviete(db.Model):
    __tablename__ = 'darboviete'

    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String, nullable=False, unique=True)
    miestas = db.Column(db.String, nullable=False)
    darbuotojai = db.relationship('Darbuotojas', backref='darboviete')

    @property
    def darbuotoju_skaicius(self):
        return len(self.darbuotojai)


class Darbuotojas(db.Model):
    __tablename__ = 'darbuotojas'

    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String, nullable=False)
    pavarde = db.Column(db.String, nullable=False)
    pareigos = db.Column(db.String, nullable=False)
    darboviete_id = db.Column(db.Integer, db.ForeignKey('darboviete.id'), nullable=False)


# Endpointai
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    if search_query:
        darbovietes = Darboviete.query.filter(Darboviete.pavadinimas.ilike(f'%{search_query}%')).all()
    else:
        darbovietes = Darboviete.query.all()
    return render_template('darbovietes.html', darbovietes=darbovietes)

@app.route('/darboviete/<int:id>')
def perziureti_darboviete(id):
    darboviete = Darboviete.query.get(id)
    return render_template('darboviete.html', darboviete=darboviete)

@app.route('/prideti-darboviete', methods=['GET', 'POST'])
def prideti_darboviete():
    if request.method == 'POST':
        pavadinimas = request.form['pavadinimas']
        miestas = request.form['miestas']
        nauja_darboviete = Darboviete(pavadinimas=pavadinimas, miestas=miestas)
        db.session.add(nauja_darboviete)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('prideti_darboviete.html')

@app.route('/redaguoti-darboviete/<int:id>', methods=['GET', 'POST'])
def redaguoti_darboviete(id):
    darboviete = Darboviete.query.get(id)
    if request.method == 'POST':
        darboviete.pavadinimas = request.form['pavadinimas']
        darboviete.miestas = request.form['miestas']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('redaguoti_darboviete.html', darboviete=darboviete)

@app.route('/trinti-darboviete/<int:id>', methods=['POST'])
def trinti_darboviete(id):
    darboviete = Darboviete.query.get(id)
    if darboviete.darbuotojai:
        return 'Negalima istrinti darbovietes, kurioje yra darbuotoju!'
    db.session.delete(darboviete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/darbuotojai')
def darbuotojai():
    darbuotojai = Darbuotojas.query.all()
    return render_template('darbuotojai.html', darbuotojai=darbuotojai)

@app.route('/prideti-darbuotoja', methods=['GET', 'POST'])
def prideti_darbuotoja():
    darbovietes = Darboviete.query.all()
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        pareigos = request.form['pareigos']
        darboviete_id = request.form['darboviete_id']
        naujas_darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, pareigos=pareigos, darboviete_id= darboviete_id)
        db.session.add(naujas_darbuotojas)
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template('prideti_darbuotoja.html', darbovietes=darbovietes)

@app.route('/redaguoti-darbuotoja/<int:id>', methods=['GET', 'POST'])
def redaguoti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get(id)
    darbovietes = Darboviete.query.all()
    if request.method == 'POST':
        darbuotojas.vardas = request.form['vardas']
        darbuotojas.pavarde = request.form['pavarde']
        darbuotojas.pareigos = request.form['pareigos']
        darbuotojas.darboviete_id = request.form['darboviete_id']
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template('redaguoti_darbuotoja.html', darbuotojas=darbuotojas, darbovietes=darbovietes)

@app.route('/trinti-darbuotoja/<int:id>', methods=['POST'])
def trinti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get(id)
    db.session.delete(darbuotojas)
    db.session.commit()
    return redirect(url_for('darbuotojai'))

with app.app_context():
    db.create_all()

app.run()

