from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///darbovietes.db'
db = SQLAlchemy(app)


# ----------------------------------------------Duomenų modeliai-------------------------------------------------------
class Darboviete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(100), nullable=False)
    miestas = db.Column(db.String(100), nullable=False)
    darbuotoju_skaicius = db.Column(db.Integer, default=0)


class Darbuotojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(100), nullable=False)
    pavarde = db.Column(db.String(100), nullable=False)
    pareigos = db.Column(db.String(100), nullable=False)
    darboviete_id = db.Column(db.Integer, db.ForeignKey('darboviete.id'), nullable=False)
    darboviete = db.relationship('Darboviete', backref=db.backref('darbuotojai', lazy=True))

#------------------------------------------ROUTE DARBOVIETE-----------------------------------------------------------

@app.route('/')
def index():
    darbovietes = Darboviete.query.all()
    return render_template('index.html', darbovietes=darbovietes)


@app.route('/prideti-darboviete', methods=['GET', 'POST'])
def prideti_darboviete():
    if request.method == 'POST':
        pavadinimas = request.form['pavadinimas']
        miestas = request.form['miestas']
        darbuotoju_skaicius = request.form['darbuotoju_skaicius']
        new_darboviete = Darboviete(pavadinimas=pavadinimas, miestas=miestas, darbuotoju_skaicius=darbuotoju_skaicius)
        db.session.add(new_darboviete)
        db.session.commit()
        return redirect('/')

    return render_template('prideti_darboviete.html')


@app.route('/redaguoti-darboviete/<int:id>', methods=['GET', 'POST'])
def redaguoti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)

    if request.method == 'POST':
        darboviete.pavadinimas = request.form['pavadinimas']
        darboviete.miestas = request.form['miestas']
        darboviete.darbuotoju_skaicius = request.form['darbuotoju_skaicius']
        db.session.commit()
        return redirect('/')

    return render_template('redaguoti_darboviete.html', darboviete=darboviete)


@app.route('/trinti-darboviete/<int:id>', methods=['GET'])
def trinti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)
    if len(darboviete.darbuotojai) == 0:
        db.session.delete(darboviete)
        db.session.commit()
    return redirect('/')

#----------------------------ROUTE DARBUOTOJAi------------------------------------------------------------------

@app.route('/darbuotojai')
def darbuotojai():
    darbuotojai = Darbuotojas.query.all()
    return render_template('darbuotojai.html', darbuotojai=darbuotojai)


@app.route('/prideti-darbuotoja', methods=['GET', 'POST'])
def prideti_darbuotoja():
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        pareigos = request.form['pareigos']
        darboviete_id = request.form['darboviete_id']

        darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, pareigos=pareigos, darboviete_id=darboviete_id)
        db.session.add(darbuotojas)
        db.session.commit()


        return redirect(url_for('darbuotojai'))

    darbovietes = Darboviete.query.all()
    return render_template('prideti_darbuotoja.html', darbovietes=darbovietes)


@app.route('/redaguoti-darbuotoja/<int:id>', methods=['GET', 'POST'])
def redaguoti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)

    if request.method == 'POST':
        darbuotojas.vardas = request.form['vardas']
        darbuotojas.pavarde = request.form['pavarde']
        darbuotojas.pareigos = request.form['pareigos']
        darbuotojas.darboviete_id = request.form['darboviete_id']

        db.session.commit()
        return redirect(url_for('darbuotojai'))

    darbovietes = Darboviete.query.all()
    return render_template('redaguoti_darbuotoja.html', darbuotojas=darbuotojas, darbovietes=darbovietes)


@app.route('/trinti-darbuotoja/<int:id>', methods=['GET', 'POST'])
def trinti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    db.session.delete(darbuotojas)
    db.session.commit()
    return redirect(url_for('darbuotojai'))

#----------------------------DARBOVIECIU PAIESKA / PERZIURA------------------------------------------------------------------

@app.route('/paieska', methods=['POST'])
def paieska():
    pavadinimas = request.form.get('pavadinimas')
    if pavadinimas:
        darbovietes = Darboviete.query.filter(Darboviete.pavadinimas.ilike(f'%{pavadinimas}%')).all()
    else:
        darbovietes = Darboviete.query.all()

    return render_template('index.html', darbovietes=darbovietes, pavadinimas=pavadinimas)




@app.route('/darboviete/<int:id>')
def darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)
    darbuotojai = Darbuotojas.query.filter_by(darboviete_id=id).all()
    darbuotoju_skaicius = len(darbuotojai)
    return render_template('darboviete.html', darboviete=darboviete, darbuotojai=darbuotojai, darbuotoju_skaicius=darbuotoju_skaicius)







# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
app.run(debug=True)
