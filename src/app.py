from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'suasenha',
    'database': 'contatos',
}

# Conectar ao banco de dados
mysql = mysql.connector.connect(**db_config)

# Criar um cursor para executar consultas SQL
cursor = mysql.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/unidades")
def unidades():
    return render_template("unidades.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/pilares")
def pilares():
    return render_template("pilares.html")

@app.route('/users')
def users():
    cursor.execute("SELECT * FROM contatos")
    userDetails = cursor.fetchall()

    return render_template("users.html", userDetails=userDetails)

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        # Executar a consulta SQL usando o cursor
        cursor.execute("INSERT INTO contatos (email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        
        # Commit para salvar as alterações no banco de dados
        mysql.commit()

        return redirect('/users')

    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(debug=True)
