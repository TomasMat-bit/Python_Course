from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

CORS(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

def add_sample_books():
    books = [
        {"title": "Programavimo pagrindai", "author": "Tomas Tamošaitis", "year": 2020},
        {"title": "Python programavimas", "author": "Marius Paliulis", "year": 2018},
        {"title": "Mokymasis iš duomenų", "author": "Petras Juknys", "year": 2021},
        {"title": "Algoritmai ir duomenų struktūros", "author": "Dainius Sereika", "year": 2019},
        {"title": "Web programavimas", "author": "Kęstutis Vilimas", "year": 2022}
    ]
    for book in books:
        existing_book = Book.query.filter_by(title=book["title"]).first()
        if not existing_book:
            new_book = Book(title=book["title"], author=book["author"], year=book["year"])
            db.session.add(new_book)
    db.session.commit()

# Pirmas kartas, kai paleidžiamas serveris, įrašome pavyzdines knygas
with app.app_context():
    add_sample_books()

# API maršrutai
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], year=data['year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"id": new_book.id, "title": new_book.title, "author": new_book.author, "year": new_book.year}), 201

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Knyga nerasta"}), 404

if __name__ == "__main__":
    app.run(debug=True)
