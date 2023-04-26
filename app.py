from flask import Flask, render_template, request
from mongoengine import connect, Document, StringField, DateTimeField, ListField

app = Flask(__name__)

# Criando a rota como decorator
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        class Users(Document):
            login = StringField(require=True, unique=True)
            senha = StringField(require=True)
        
        connect(host='mongodb+srv://dba:dba123@odr.ookqkat.mongodb.net/test')
        user = Users(
            login = request.form['login'],
            senha = request.form['senha']
        )
        user.save()

        

    return render_template('index.html', title='Homepage', heading='Bem vindo', content='Conexão feita com sussesso!')

@app.route("/login")
def login():

    return render_template('login.html', title='Login', heading='Login')






