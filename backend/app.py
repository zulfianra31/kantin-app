from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/menu', methods=['GET'])
def get_menu():
    menu = [
        {'id': 1, 'nama': 'Nasi Goreng', 'harga': 15000},
        {'id': 2, 'nama': 'Mie Ayam', 'harga': 12000}
    ]
    return jsonify(menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)