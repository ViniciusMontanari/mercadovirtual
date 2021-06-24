# -*- coding: utf-8 -*-
# Importando a biblioteca do SQLAlchemy para manipular o banco de dados
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para utilizarmos as funções (queries) do SQLAlchemy
from sqlalchemy import func

# Adicionado para permitir relacionamento entre as classes Usuario e Perfil
from sqlalchemy.orm import relationship  

# Importando o arquivo config com as configurações de ambiente
from config import app_active, app_config
from models.Perfil import Perfil  

# Biblioteca adicionada para criptografia de senha
from passlib.hash import pbkdf2_sha256

# Importando a classe Perfil para ser utilizada na criação do relacionamento do usuario um-um.
# perfil=db.Column(db.Integer,db.ForeignKey(Perfil.id),nullable=False)
from models.Perfil import Perfil 

# Criação da variável config para receber a atribuição do ambiente ativo.
config = app_config[app_active] 

# Criação da variável db para receber a atribuição de uma instância do SQLAlchemy passando a aplicação app criada.
db = SQLAlchemy(config.APP)

# classe Usuario com 9 campos, sendo o id e o nome do usuario, email, senha, data de criação, última atualização, código de recuperação de senha que senha encriptado, se é perfil ativo e a chave estrangeira para a classe Perfil por meio do id do perfil.
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

    # Adicionado para permitir a relação entre a classe Usuário e a classe Perfil.
    perfil = relationship(Perfil)

    # Adicionado para exibir da forma que é definida na chamada do objeto da classe.
    # É a forma que será exibido no campo de relacionamento.
    def __repr__(self):
        return '%s - %s' % (self.id, self.username)


    # Métodos adicionados para configuração posterior
    def get_usuario_by_email(self): 
        # Método para validar se usuário existe ou não
        return ' '

    def get_usuario_by_id(self): 
        # Método para listar dados do usuário perfil
        return ' '

    def update_usuario(self, obj): 
        # Método para atualizar o usuário 
        return ' '

    # Adicionando os métodos para criptografia de senha
    # Metodo de conversão de senha de string para string criptografada
    def hash_password(self, password): 
        try:
            return pbkdf2_sha256.hash(password) 
        except Exception as e:
            print("Erro ao tentar criptografar a senha %s" % e) 

    # Método para atualizar senha
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    # Método para verificar se a senha informada é igual a que está no banco de dados
    def verify_password(self, password_no_hash, password_database): 
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False

    # Método adcionado para contar quantos usuários estão cadastrados.
    # Executa uma query no banco de dados na tabela, utilizando o count()
    # E obtem somente o primeiro first().
    def get_total_usuarios(self):
        try:
            res = db.session.query(func.count(Usuario.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally: 
            db.session.close() 
            return res