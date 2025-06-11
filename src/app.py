from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import mysql.connector
import re
import os

app = Flask(__name__)
app.secret_key = 'chave-secreta'

# Conexão com banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="6807",
        database="sustentabilidade"
    )

# Classificação de água
def classificar_agua(valor):
    if valor < 150:
        return '🟢 Alta sustentabilidade'
    elif valor <= 200:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de energia 
def classificar_energia(valor):
    if valor < 5:
        return '🟢 Alta sustentabilidade'
    elif valor <= 10:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de residuos
def classificar_residuos(valor):
    if valor > 50:
        return '🟢 Alta sustentabilidade'
    elif valor >= 20:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de reciclado
def classificar_reciclado(valor):
    if valor >= 80:
        return '🟢 Alta sustentabilidade'
    elif valor >= 50:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de transporte
def classificar_transporte(opcao):
    if opcao in [2, 3]:
        return '🟢 Alta sustentabilidade'
    elif opcao in [5, 6]:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/inserir', methods=['POST'])
def inserir_dados():
    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = request.form['usuario'].strip()
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            flash("❌ Nome inválido. Use apenas letras e espaços.")
            return redirect(url_for('index'))

        data = datetime.strptime(request.form['data'], "%Y-%m-%d").strftime('%Y-%m-%d')
        agua = float(request.form['agua'])
        energia = float(request.form['energia'])
        residuos = float(request.form['residuos'])
        reciclado = float(request.form['reciclado'])
        transporte = request.form['transporte']

        cursor.execute("""
            INSERT INTO sustentabilidade_pessoal (
                data_registro, usuario, consumo_agua, consumo_energia,
                residuos_nao_reciclaveis, percentual_reciclados, transporte
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (data, nome, agua, energia, residuos, reciclado, transporte))

        conn.commit()
        flash("✅ Dados inseridos com sucesso!")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"❌ Erro ao inserir dados: {e}")
        return redirect(url_for('index'))
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
