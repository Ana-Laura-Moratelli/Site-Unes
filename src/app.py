from flask import Flask, request, render_template, redirect #importa a classe flask e o render template importa a pasta templates para arquivos HTML
from flask_mysqldb import MySQL

app = Flask("__name__") #cria uma instância dessa classe
  

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route("/") # criando rotas com decorator

def home(): #função para retornar uma mensagem
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
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT *  FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos (email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()

        return redirect('/users')
    
    return render_template('contatos.html')



if __name__ == '__main__':
    app.run(debug=True) 