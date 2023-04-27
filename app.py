from flask import Flask, render_template, request, redirect, url_for
from mongoengine import connect, Document, StringField, DateTimeField, ListField,disconnect

class Users(Document):
    login = StringField(require=True, unique=True)
    senha = StringField(require=True)
class Tarefas(Document):
    nome = StringField(require=True, unique=True)
    descr = StringField(require=True)
class Projetos(Document):
    nome = StringField(require=True, unique=True)
    descr = StringField(require=True)


app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def login():
    
    if request.method == 'POST':
        text = request.form['login']
        user = Users(
            login = request.form['login'],
            senha = request.form['senha']
        )
        connect(host='mongodb+srv://dba:dba123@odr.ookqkat.mongodb.net/test')
        user.save()
        return render_template('cadastroUser.html', title='Homepage', heading='Cadastro usuário')
    else:
        text = ''
    return render_template('login.html', title='Homepage', heading='Login', login=text)

@app.route("/home", methods = ['POST','GET'])
def index():
    text = ''
    
    if request.method == 'POST':
        connect(host='mongodb+srv://dba:dba123@odr.ookqkat.mongodb.net/test')
    for user in Users.objects:    
        if request.form['login'] == user.login and request.form['senha'] == user.senha :
            return render_template('index.html', title='Home', heading='Bem vindo!')
    if text == '':
        return render_template('login.html', title='Home', heading='Usuário ou senha inválidos!')


@app.route("/create/<user>", methods =['POST','GET'])
def create(user):
 
    if user == 'login':
        user = Users(
        login = request.form['login'],
        senha = request.form['senha']
        )
        text = user.login
        connect(host='mongodb+srv://dba:dba123@odr.ookqkat.mongodb.net/test')
        user.save()
        disconnect()
        return render_template('login.html', title='Homepage', heading='Login', login=text)
    
    if user == 'user':
        user = Users(
            login = request.form['login'],
            senha = request.form['senha']
        )
        user.save()
    
    if user == 'tarefa':
        tarefa = Tarefas(
            nome = request.form['nome'],
            descr = request.form['descricao']
        )
        tarefa.save()

    if user == 'projeto':
        projeto = Projetos(
            nome = request.form['nome'],
            descr = request.form['descricao']
        )
        projeto.save()
    
    return render_template('index.html', title='Homepage', heading='Bem vindo!')

@app.route("/read/<user>", methods =['POST','GET'])
def read(user):
    return




@app.route("/user/cadastro")
def cadastroUser():

    return render_template('cadastroUser.html', title='User', heading='Cadastro usuário')


@app.route("/projeto/cadastro")
def cadastroProjeto():

    return render_template('cadastroProjetos.html', title='Projeto', heading='Cadastro projeto')


@app.route("/tarefa/cadastro")
def cadastroTarefa():

    return render_template('cadastroTarefas.html', title='Tarefa', heading='Cadastro Tarefa')



