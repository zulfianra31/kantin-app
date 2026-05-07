import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/menu', methods=['GET'])
def get_menu():
    # MENGAMBIL DATA DARI YAML (INJECTION)
    nama_dari_env = os.getenv('NAMA_MHS', 'Nama Tidak Terdeteksi')
    nim_dari_env = os.getenv('NIM_MHS', 'NIM Tidak Terdeteksi')

    menu = [
        {'id': 1, 'nama': 'Nasi Goreng', 'harga': 15000},
        {'id': 2, 'nama': 'Mie Ayam', 'harga': 12000}
    ]

    # Kirim data identitas beserta menu ke Frontend
    return jsonify({
        'identitas': {'nama': nama_dari_env, 'nim': nim_dari_env},
        'data': menu
    })