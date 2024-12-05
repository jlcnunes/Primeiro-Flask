# Importação da classe Flask a partir do módulo flask

from flask import Flask, render_template
from classes.curso import Curso

# Definição do objeto que representa a aplicação

app = Flask(__name__)


# Cria a rota /, acessível a partir de: http://127.0.0.1:5000/

@app.route('/')
def index():
    titulo = 'Desenvolvimento Web é Legal'
    conteudo = 'Olha que legal, agora sabemos criar páginas dinâmicas' 
    return render_template('index.html', titulo=titulo, conteudo=conteudo)

# Cria a rota /cursos, acessível a partir de : http://127.0.0.1:5000/cursos

@app.route("/cursos")
def curso():
    lista_de_cursos = ['Desenvolvimento Web', 'Programação Orientada a Objetos', 'Banco de Dados']
    return render_template('cursos.html', lista=lista_de_cursos)

@app.route('/curso/<nome>')
def curso_por_nome(nome):
    if nome == 'devweb':
        info = Curso("Desenvolvimento Web", "Disciplina que lida com as tecnologias da web", ['HTML', 'CSS','JavaScript'], 2)
        return render_template("info_curso.html", objeto=info)
    elif nome == 'poo':
        info = Curso("Progrmação Orientada a Objetos", "Disciplina que nos ensina o paradigama orientado a objetos", ['Dicionários', 'Tratamento de exceções','Classes','Herança'], 1)
        return render_template("info_curso.html", objeto=info)
    else:
        nome == 'db'
        info= Curso("Banco de Dados", "Este curso ainda está em construção. Estamos trabalhando para oferecer o melhor curso de Banco de Dados a você!", ['MER', 'DER', 'SGBD', 'DDL', 'DML', 'DQL'], 2)
        return render_template("info_curso.html", objeto=info) 

# Inicialização do servidor

if __name__ == '__main__':
    app.run(debug=True)
