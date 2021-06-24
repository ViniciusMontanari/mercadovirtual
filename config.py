import os
import random, string


# Classe Config criada com as configurações do Projeto.
class Config(object):
    # Permite o uso de criptografia em sessões do Flask.
    CSRF_ENABLED = True

    # Palavra-chave secreta utilizada para criptografar chaves e valores, como por exemplo: senhas.
    SECRET = 'ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&'

    # Caminho completo onde os templates estarão disponíveis no projeto.
    # Para capturar o endereco do arquivo atual: os.path.dirname(__file__)
    # Para capturar o caminho absoluto: os.path.abspath(variavel)
    # Para unir as strings: os.path.join(str1, str2)
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

    # Identificação do caminho completo do local do projeto
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

    # Constante inicializada com None, posteriormente ao criar o app, esta será atribuída.
    APP = None

    # Variável com o endereço do banco de dados. O método .join é utilizado para 
    # concatenar o nome completo contendo o endereço do banco de dados a ser utilizado pelo app.
    # O banco de dados será chamado de app.db. Pode ser utilizado qualquer nome.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT_DIR, 'app.db')

    # Configuração indicando que as modificações do banco de dados poderão ser exclusivamente pela aplicação.
    # Se True, permite outras formas.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CHAVE API COPIADA DO SITE - UNICA PARA CADA UM ** OMITIR ANTES DE DIVULGAR CODIGO ***
    # Inserida para enviar email por meio do serviço sendgrid. (veremos mais adiante)
    SENDGRID_API_KEY = 'Copiar a chave do site'

# Classe Development herda da classe Config, e foi criada com as configurações do Projeto para ambiente de Desenvolvimento.
class Development(Config):
    # Habilitando o modo de teste.
    TESTING = True

    # Habilitando o modo de debug.
    DEBUG = True

    # Definindo o IP do servidor Flask.
    IP_HOST = 'localhost'

    # Definindo a PORTA de acesso do servidor Flask.
    PORT_HOST = 8000

    # Definindo a URL root da aplicação Flask.
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


# Classe TestingConfig herda da classe Config, e foi criada com as configurações do Projeto para ambiente de Teste.
class TestingConfig(Config):
    TESTING = True
    DEBUG = True

    # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local.
    IP_HOST = 'localhost' 

    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


# Classe Production herda da classe Config, e foi criada com as configurações do Projeto para ambiente de Produção. 
class Production(Config):
    DEBUG = False
    TESTING = False

    # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local.
    IP_HOST = 'localhost' 

    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

# Variável com as 3 configurações dos ambientes. Será utilizada para saber qual ambiente estamos utilizando.   
app_config = {
    'development': Development(), 
    'testing': TestingConfig(), 
    'production': Production()
}

# Variável que receberá o valor do ambiente que está ativo e em uso. O método os.getenv('NOME_DA_CHAVE'). Onde NOME_DA_CHAVE é o nome da variável de ambiente, neste caso FLASK_ENV. Esta variável receberá o tipo de ambiente que está sendo utilizado antes da execução do arquivo run.py. Deve ser informada uma única vez. Porém todas as vezes que o ambiente virtual for ativado. E sempre antes de exeutar o run.py. 
app_active = os.getenv('FLASK_ENV')