from flask import Flask, render_template, request
from mongoengine import connect, Document, StringField, DateTimeField, ListField

app = Flask(__name__)

# Criando a rota como decorator
@app.route('/')
def index():
    return render_template('index.html', title='Homepage', heading='Bem vindo', content='Pagina Principal')

@app.route("/login")
def login():
    return render_template('login.html', title='Login', heading='Login')




# Conecta ao banco de dados MongoDB
connect(host='mongodb+srv://dba:dba123@odr.ookqkat.mongodb.net/test')




# # Define o modelo para o documento
# class Projeto(Document):
#     nome_do_projeto = StringField(required=True)
#     data_de_entrega = DateTimeField(required=True)
#     lider = StringField(required=True)
#     integrantes = ListField(StringField())

# # Cria um novo projeto
# projeto = Projeto(
#     nome_do_projeto='Projeto A',
#     data_de_entrega='2023-12-31',
#     lider='João',
#     integrantes=['Maria', 'Pedro']
# )
# projeto.save()

# # Lista todos os projetos
# projetos = Projeto.objects()
# for projeto in projetos:
#     print(projeto.nome_do_projeto)

# # # Atualiza um projeto existente
# projeto = Projeto.objects(nome_do_projeto='Projeto A').first()
# projeto.lider = 'José'
# projeto.save()

# # Deleta um projeto existente
# projeto = Projeto.objects(nome_do_projeto='Projeto A').first()
# projeto.delete()