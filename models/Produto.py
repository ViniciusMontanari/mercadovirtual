# -*- coding: utf-8 -*-
# Importando a biblioteca do SQLAlchemy para manipular o banco de dados
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para utilizarmos as funções (queries) do SQLAlchemy
from sqlalchemy import func

# Importando o arquivo config com as configurações de ambiente
from config import app_active, app_config

# Adicionado para permitir relacionamento entre as classes. O campo criado exibirá as informações do relacionamento.
from sqlalchemy.orm import relationship


from models.Secao import Secao

# Criação da variável config para receber a atribuição do ambiente ativo.
config = app_config[app_active] 

# Criação da variável db para receber a atribuição de uma instância do SQLAlchemy passando a aplicação app criada.
db = SQLAlchemy(config.APP)

# classe Componente com 6 campos, sendo o id, a descrição, quantidade de produtos e a area.
class Produto(db.Model): 
    id=db.Column(db.Integer,primary_key=True) 
    descricao=db.Column(db.Text(),nullable=False)
    qtde=db.Column(db.Integer) 
    preco_unitario=db.Column(db.Float,default=0,nullable=False)
    areaid=db.Column(db.Integer,db.ForeignKey(Secao.id),nullable=False)

    # Método que criará um campo no formulário de criação e edição para representar
    # o elemento que faz relacionamento com aquela tabela.
    
    secao=relationship(Secao)

    # Adicionado para exibir da forma que é definida na chamada do objeto da classe.
    # É a forma que será exibido no campo de relacionamento.
    def __repr__(self):
        return '%s - %s' % (self.id, self.sigla)

    # Método adicionado para contar quantos componentes estão cadastrados.
    # Executa uma query no banco de dados na tabela, utilizando o count()
    # E obtem somente o primeiro first().
    def get_total_produtos(self):
        try:
            res = db.session.query(func.count(Produto.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally: 
            db.session.close() 
            return res

    # Método adicionado para buscar os últimos componentes inseridos com o limite de 5.
    def get_last_produtos(self): 
        try:
            res = db.session.query(Produto).order_by(Produto.descricao).limit(5).all()
        except Exception as e:
            res = []
            print(e)
        finally: 
            db.session.close() 
            return res