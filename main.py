from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/novoComentario", methods=['POST'])
def novoComentario():

    nome = request.form.get("nome")
    celular = request.form.get("celular")
    email = request.form.get("email")
    comentario = request.form.get("comentario")
    
    try:
        conexao = mysql.connector.connect (
        host='localhost', 
        database='nomeDoBanco', 
        user='root', 
        password='123456'
    )

        inserirNovoComentario = f'INSERT INTO nomeDaTabela (nome, celular, email, comentario) VALUES ("{nome}","{celular}", "{email}", "{comentario}")'


        cursor = conexao.cursor()
        cursor.execute(inserirNovoComentario)
        conexao.commit()
        print(cursor.rowcount, "Registros inseridos na tabela!")
        cursor.close()
    except Error as erro:
        print("Falha ao inserir dados no MySQL: {}".format(erro))
    finally:
        if (conexao.is_connected()):
            conexao.close()
            print("Conexão ao MySQL finalizada")

    return render_template("index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
