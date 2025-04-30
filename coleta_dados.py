import csv
import requests 
import time
import os

url = "http://127.0.0.1:5000/atividade"
arquivo = "dados_atividade.csv"
campos = ["passos", "distancia_km", "calorias_gastas", "duracao_minutos", "data_hora"]
    
def coletar_dados():
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()

            arquivo_existe = os.path.exists(arquivo)

            with open(arquivo, mode="a", newline="", encoding="utf-8") as arquivo_csv:
                escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

                if not arquivo_existe:
                    escritor.writeheader()

                escritor.writerow(dados)

            print(f"Dados coletados: {dados}")
        else:
            print(f"Erro ao acessar a API: {resposta.status_code}")
    except Exception as err:
        print(f"Erro durante a coleta: {err}")

for _ in range(200):
    coletar_dados()
    time.sleep(2)