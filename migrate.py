# Usado somente para criar o banco sqlite e as migrações dos modelos e sempre que alterar algum modelo, copiar novamente a classe e executar.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
from config import app_active, app_config


config = app_config[app_active]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app) 
manager.add_command('db', MigrateCommand)

# ADICIONAR AQUI OS MODELS
# IMPORTANTE, LEMBRAR DAS DEPENDÊNCIAS NA CRIAÇÃO


class Perfil(db.Model): 
    id=db.Column(db.Integer,primary_key=True) 
    perfil=db.Column(db.String(40),unique=True,nullable=False)

class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome_do_usuario=db.Column(db.String(40),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 
    recovery_code=db.Column(db.String(100),nullable=True) 
    active=db.Column(db.Boolean(),default=1,nullable=False) 
    relacao=db.Column(db.Integer,db.ForeignKey(Perfil.id),nullable=False)

class Secao(db.Model): 
    id=db.Column(db.Integer,primary_key=True) 
    secao=db.Column(db.String(10),unique=True,nullable=False) 
    descricao=db.Column(db.Text(),nullable=False)


class Produto(db.Model): 
    id=db.Column(db.Integer,primary_key=True) 
    descricao=db.Column(db.Text(),nullable=False)
    qtde=db.Column(db.Integer)
    preco_unitario=db.Column(db.Float,default=0,nullable=False)
    areaid=db.Column(db.Integer,db.ForeignKey(Secao.id),nullable=False)


if __name__ == '__main__':
    manager.run()