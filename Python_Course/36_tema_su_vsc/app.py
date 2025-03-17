from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

produktai = [
    {"id": 1, "produkto_pavadinimas": "Kavos puodelis", "kaina": 10},
    {"id": 2,"produkto_pavadinimas": "Pyragas", "kaina": 5},
    {"id": 3,"produkto_pavadinimas": "Saldainiai", "kaina": 2},
    {"id": 4,"produkto_pavadinimas": "Pica", "kaina": 15},
    {"id": 5,"produkto_pavadinimas": "Alus", "kaina": 8}
]

# API endpointas
@app.route('/api/produktai', methods=['GET'])
def get_produktai():
    return jsonify(produktai)

app.run(port=5000)
