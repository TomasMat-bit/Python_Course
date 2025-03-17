from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/zmones')
def get_zmones():
    zmones = [
        {'id': 1, 'vardas': 'Jonas', 'amzius': 25},
        {'id': 2, 'vardas': 'Laura', 'amzius': 30},
        {'id': 3, 'vardas': 'Petras', 'amzius': 40}
    ]
    return jsonify(zmones)

app.run(port=5000)
