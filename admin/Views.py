# Componente dentro do flask_admin para ativar as views em nossa aplicação, baseadas em nossas models.
# Será utilizado aqui como superclasse da classe UsuarioView (herdará todas as configurações e poderá ser modificada)
from flask_admin.contrib.sqla import ModelView

# Adicionado para adequar a Home da aplicação
# A classe AdminIndexView que será herdada pela classe HomeView para que a 
# classe HomeView tenha todas as características da página de home 
# Importando o decorator @expose('/home')para indicar qual rota está sendo modificada.
# http://localhost:8000/admin/.
from flask_admin import AdminIndexView, expose

# É importado do arquivo config.py, as variáveis app_config, app_active que app_config: possui as configurações e o tipo de ambiente a ser utilizado (Desenvolvimento, Teste ou Producao). E app_active: possui as configurações de qual ambiente está sendo utilizado por meio da variável de ambiente FLASK_ENV.
from config import app_config, app_active

# Adicionado para renderizar os cálculos das quantidades de cada tabela.
from models.Usuario import Usuario
from models.Secao import Secao
from models.Produto import Produto

# A variável config recebe a atribuição do ambiente ativo.
config = app_config[app_active]

# Adicionada a classe HomeView que herda de AdminIndexView todas as caracteírsticas.
# Substitui a home com o temnplate customizado admin.html (vamos criá-lo)
class HomeView(AdminIndexView):
    # Indicando que os arquivos css de formatação devem ser usados. Tanto o home quanto o cdn online.
    extra_css = [config.URL_MAIN + 'static/css/home.css','https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']
    @expose('/')
    def index(self):
        usuario_model = Usuario() 
        secao_model = Secao() 
        produto_model = Produto()

        usuarios = usuario_model.get_total_usuarios()
        secoes = secao_model.get_total_secoes() 
        produtos = produto_model.get_total_produtos()

        # Adicionado para exibir os últimos 5 registros (definido no models/Componente.py em limit(). 
        last_produtos = produto_model.get_last_produtos()

        return self.render('admin.html', report={
            'usuarios': 0 if not usuarios else usuarios[0],
            'secoes': 0 if not secoes else secoes[0], 
            'produtos': 0 if not produtos else produtos[0]
        },  last_produtos=last_produtos )

# Classe criada para ser customizada a partir da ModelView (superclasse)
class UsuarioView(ModelView):
    # propriedades descritas anteriormente para que servem.
    column_exclude_list = ['password', 'recovery_code'] 
    form_excluded_columns = ['last_update', 'recovery_code']
    form_widget_args = { 
        'password': {'type': 'password' }
    }

    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email'] 
    column_filters = ['username', 'email', 'relacao']
    column_editable_list = ['username', 'email', 'relacao', 'active' ]
    create_modal = True
    edit_modal = True
    can_export = True
    export_types = ['json', 'yaml', 'csv', 'xls', 'df']
    column_sortable_list = ['username']
    column_default_sort = ('username', True) 

    column_labels = {
        'perfil': 'Perfil',
        'username': 'Nome de usuário', 
        'email': 'E-mail',
        'date_created': 'Data de criação', 
        'last_update': 'Última atualização', 
        'active': 'Ativo',
        'password': 'Senha',
    }

    column_descriptions = {
        'perfil': 'Perfil no painel administrativo',
        'username': 'Nome de usuário no sistema',
        'email': 'E-mail do usuário no sistema',
        'date_created': 'Data de criação do usuário no sistema', 
        'last_update': 'Última atualização desse usuário no sistema', 
        'active': 'Estado ativo ou inativo no sistema',
        'password': 'Senha do usuário no sistema', 
    }

    
    column_details_exclude_list = ['password', 'recovery_code'] 
    column_export_exclude_list = ['password', 'recovery_code'] 
