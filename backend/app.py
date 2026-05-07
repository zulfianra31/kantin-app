import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/menu', methods=['GET'])
def get_menu():
    # Mengambil identitas dari Environment Variable (YAML Injection)
    nama = os.getenv('NAMA_MHS', 'Nama Belum Disetting')
    nim = os.getenv('NIM_MHS', 'NIM Belum Disetting')
    
    menu = [
        {'id': 1, 'nama': 'Nasi Goreng', 'harga': 15000},
        {'id': 2, 'nama': 'Mie Ayam', 'harga': 12000},
        {'id': 3, 'nama': 'Ayam Geprek', 'harga': 18000},
        {'id': 4, 'nama': 'Es Teh Manis', 'harga': 5000}
    ]
    
    return jsonify({
        'biodata': {'nama': nama, 'nim': nim},
        'menu': menu
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)