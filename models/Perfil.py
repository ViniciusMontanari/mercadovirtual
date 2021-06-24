# -*- coding: utf-8 -*-
# Importando a biblioteca do SQLAlchemy para manipular o banco de dados
from flask_sqlalchemy import SQLAlchemy 

# Importando o arquivo config com as configurações de ambiente
from config import app_active, app_config

# Criação da variável config para receber a atribuição do ambiente ativo.
config = app_config[app_active] 

# Criação da variável db para receber a atribuição de uma instância do SQLAlchemy passando a aplicação app criada.
db = SQLAlchemy(config.APP)

# classe Perfil com 2 campos, o id e o nome do perfil.
class Perfil(db.Model): 
    id=db.Column(db.Integer,primary_key=True) 
    perfil=db.Column(db.String(40),unique=True,nullable=False)

    # Adicionado para exibir da forma que é definida na chamada do objeto da classe.
    # É a forma que será exibido no campo de relacionamento.
    def __repr__(self):
        return self.perfil