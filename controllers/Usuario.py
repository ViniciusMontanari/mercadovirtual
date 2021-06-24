from models.Usuario import Usuario

class UsuarioController():
    # Método construtor da classe UsuarioController.
    def __init__(self):
        # Inicializa uma instância de Usuario().
        self.usuario_model = Usuario()

    # Método que será utilizado para ligar a rota de login com a Model de Usuário
    def login(self, email, password):
        # Recebe os dados de e-mail e salva no atributo da Model de Usuário.
        self.usuario_model.email = email

        # Verifica se o usuário existe no banco de dados e atribui a resultado.
        resultado = self.usuario_model.get_usuario_by_email()

        # Caso o usuário exista o resultado não será None
        if resultado is not None: 
            # Verifica se a senha que o usuário enviou, agora convertido em hash, é igual a senha que foi pega no banco de dados para esse usuário.
            res = self.usuario_model.verify_password(password, resultado.password)

            # Se forem a mesma, retorna True.
            if res:
                return resultado
            else:
                return {}
        return {}