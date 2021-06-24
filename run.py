# Importa a biblioteca que permite a execução de intruções no sistema.
import sys

# do pacote app.py importa o método create_app, o qual criará uma instância da aplicação.
from app import create_app

# do módulo config importa o as variáveis app_config, app_active que possuem as configurações do ambiente.
from config import app_config, app_active

# Importa da biblioteca importlib, o método reload para que a cada alteração em algum arquivo, o servidor Flask seja reiniciado.
from importlib import reload

# A variável config foi criada para receber o ambiente ativo.
config = app_config[app_active] 

# A variável config.APP, APP constante definida no arquivo config.py foi criada para receber a aplicação ativa. A aplicação ativa, é definida no arquivo app.py e importada pelo run.py.
config.APP = create_app(app_active)

# Verificar se o arquivo run.py está sendo executado de forma direta ou não. Se for importado, o if não será executado. Para que seja executado: no terminal digitar python run.py de dentro da pasta projeto.
# Ao ser executado diretamente run.py, será iniciado o servidor Flask. com as configurações definidas no arquivo config.py para o ip do host e porta.
if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST) 
    # executado sempre que ocorrer alguma alteração em um arquivo do projeto.
    reload(sys)