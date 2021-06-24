# -*- coding: utf-8 -*-
# from flask_admin import Admin: Ela possui vários recursos para criação 
# de views customizadas para nossa aplicação
from flask_admin import Admin

# Componente dentro do flask_admin para ativar as views em nossa aplicação, baseadas em nossas models.
from flask_admin.contrib.sqla import ModelView
from models.Perfil import Perfil
from models.Usuario import Usuario
from models.Secao import Secao
from models.Produto import Produto

# Adicionado para utilizar a view personalizada criada em Views.py (dentro da pasta admin)
# class UsuarioView(ModelView).
from admin.Views import UsuarioView, HomeView 


def start_views(app, db):
    # Utilização do bootstrap4 por meio do construtor do Admin.
    admin = Admin(app, name='Mercado Virtual', base_template='admin/base.html', template_mode='bootstrap4', index_view=HomeView())
    # Método que é utilizado para criar uma view em nossa aplicação Admin.
    # ModelView: é um recurso do flask_admin que permite a criação Admin, as telas do administrador baseadas na estrutura das models.
    # category é utilizado para agrupar os itens de menus.
    admin.add_view(ModelView(Perfil, db.session, "Perfis Acesso", category= "Configurações"))
    admin.add_view(ModelView(Usuario, db.session, "Usuários", category="Usuários"))
    admin.add_view(ModelView(Secao, db.session, "Seções do Mercado", category="Configurações"))
    admin.add_view(ModelView(Produto, db.session, "Produtos", category="Produtos"))