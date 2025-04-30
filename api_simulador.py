import random
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/atividade', methods=['GET'])

def gerar_atividade():
    atividade = {
        'passos': random.randint(1000, 15000),
        'distancia_km': round(random.uniform(1.0, 15.0), 2),
        'calorias_gastas': random.randint(100, 1000),
        'duracao_minutos': random.randint(10, 120),
        'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(atividade)
    

if __name__ == '__main__':
    app.run(debug=True)