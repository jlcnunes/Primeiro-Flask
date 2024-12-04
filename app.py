# Importação da classe Flask a partir do módulo flask

from flask import Flask
from flask import render_template

# Definição do objeto que representa a aplicação

app = Flask(__name__)


# Cria a rota /, acessível a partir de: http://127.0.0.1:5000/

@app.route('/')
def index():
    return render_template('index.html')

# Cria a rota /saudacao, acessível a partir de : http://127.0.0.1:5000/saudacao

@app.route('/saudacao')
def saudacao():
    return render_template('saudacao.html')

@app.route("/curso")
def curso():
    return render_template('cursos.html')

@app.route('/curso/<nome>')
def curso_por_nome(nome):
    if nome == 'devweb':
        return render_template('curso_devweb.html')
    elif nome == 'poo':
        return render_template('curso_poo.html')
    else:
        return "Curso inexistente"
    
@app.route('/curso/<nome>/<int:ano>')
def curso_com_dois_parametros(nome, ano):
   return "Rota de demonstração que recebe dois valores: nome={0} e ano={1}".format(nome, ano)

# Inicialização do servidor

if __name__ == '__main__':
    app.run(debug=True)
