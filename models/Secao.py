# -*- coding: utf-8 -*-
# Importando a biblioteca do SQLAlchemy para manipular o banco de dados
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para utilizarmos as funções (queries) do SQLAlchemy
from sqlalchemy import func  

# Importando o arquivo config com as configurações de ambiente
from config import app_active, app_config

# Criação da variável config para receber a atribuição do ambiente ativo.
config = app_config[app_active] 

# Criação da variável db para receber a atribuição de uma instância do SQLAlchemy passando a aplicação app criada.
db = SQLAlchemy(config.APP)

# classe Area com 3 campos, sendo o id, o sigla da área e a descrição.
class Secao(db.Model): 
    id=db.Column(db.Integer,primary_key=True) 
    secao=db.Column(db.String(10),unique=True,nullable=False) 
    descricao=db.Column(db.Text(),nullable=False)

    # Adicionado para exibir da forma que é definida na chamada do objeto da classe.
    # É a forma que será exibido no campo de relacionamento.
    def __repr__(self):
        return self.secao

    # Método adicionado para contar quantos areas estão cadastrados.
    # Executa uma query no banco de dados na tabela, utilizando o count()
    # E obtem somente o primeiro first().
    def get_total_secoes(self):
        try:
            res = db.session.query(func.count(Secao.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally: 
            db.session.close() 
            return res