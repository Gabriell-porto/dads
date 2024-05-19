from flask import Flask, render_template, request
import math
from scipy.stats import norm

app = Flask(__name__)

def calcular_tamanho_amostra(N, e, Z):
    e = e / 100
    p = 0.5
    q = 1 - p
    tamanho_amostra_infinita = ((Z**2) * p * q) / (e**2)
    tamanho_amostra = tamanho_amostra_infinita / (1 + ((tamanho_amostra_infinita - 1) / N))
    return math.ceil(tamanho_amostra)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    N = int(request.form['populacao'])
    e = float(request.form['erro'])
    confianca = float(request.form['confianca'])
    Z = norm.ppf(1 - (1 - (confianca / 100)) / 2)
    tamanho_amostra = calcular_tamanho_amostra(N, e, Z)
    return render_template('resultado.html', tamanho_amostra=tamanho_amostra)

if __name__ == '__main__':
    app.run(debug=True)
