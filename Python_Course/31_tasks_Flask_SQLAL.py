from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Mokinys(db.Model):
    __tablename__ = 'mokinys'

    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String)
    pavarde = db.Column(db.String)
    klase = db.Column(db.Integer)
    sukurimo_data = db.Column(db.DateTime, default=lambda x: datetime.utcnow)

    def __repr__(self):
        return f'<Mokinys {self.vardas} {self.pavarde}, klase {self.klase}>'

@app.route('/')
def index():
    mokiniai = Mokinys.query.all()
    return render_template('index_31.html', mokiniai=mokiniai)

with app.app_context():
    db.create_all()

app.run()