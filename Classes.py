from datetime import datetime
# Início das classes

# Davi

# Função global para obter a data e hora atual do sistema
def obter_data_hora_atual():
    return datetime.today()

# Classe Perfil que representa um perfil de usuário
class Perfil():
    def __init__(self, usuario, seguidos=None, seguidores=None, tweets=None, ativo=True):
        self.__usuario = usuario  # Nome de usuário do perfil
        self.__seguidos = []  # Perfis seguidos pelo usuário
        self.__seguidores = []  # Perfis que seguem o usuário
        self.__tweets = []  # Tweets do perfil
        self.__ativo = True  # Indica se o perfil está ativo

    # Método para obter a timeline do perfil, incluindo tweets dos perfis seguidos
    def get_timeline(self):
        timeline = self.__tweets[:]  # Copia os tweets do próprio perfil
        for perfil in self.__seguidos:
            timeline.extend(perfil.__tweets)  # Adiciona tweets dos perfis seguidos
        timeline.sort(key=lambda tweet: tweet['data'])  # Ordena os tweets pela data de postagem
        return timeline

    # Método para definir o nome de usuário
    def set_usuario(self, usuario):
        self.__usuario = usuario

    # Método para obter o nome de usuário
    def get_usuario(self):
        return self.__usuario

    # Método para definir se o perfil está ativo
    def set_ativo(self, ativo):
        self.__ativo = ativo

    # Método para verificar se o perfil está ativo
    def is_ativo(self):
        return self.__ativo

# Classe PessoaFisica que represenra um perfil de pessoa física
class PessoaFisica(Perfil):
    def __init__(self, usuario, cpf):
        super().__init__(usuario)  # Chama o construtor da superclasse Perfil
        self.__cpf = cpf  # Atributo privado para guardar o CPF associado ao perfil

    # FUnção para obter o CPF do dono do perfil
    def get_cpf(self):
        return self.__cpf

# Classe PessoaJuridica que representa um perfil de uma empresa ou pessoa juridica
class PessoaJuridica(Perfil):
    def __init__(self, usuario, cnpj):
        super().__init__(usuario) # Chama o construtor da superClasse Perfil para o atributo usuario
        self.__cnpj = cnpj
    
    # Função para obter o CNPJ do dono do perfil
    def get_cnpj(self): 
        return self.cnpj

# Exceção para usuário já cadastrado
class UJCException(Exception):
    pass

# Classe RepositorioUsuarios que armazena todos os perfis criados no sistema
class RepositorioUsuarios():
    def __init__(self):
        self.__usuarios = [] # Lista de perfil de usuários

    # FUnção para cadastrar perfis de usuários
    def cadastrar(self, perfil):
        # Verifica se o nome de usuário já está cadastrado
        for usuario in self.__usuarios:
            if usuario.get_usuario() == perfil.get_usuario():
                # Se o nome de usuário já existe, lança uma exceção
                raise UJCException('Usuário já existe')
        # Se o nome de usuário não existe, adiciona o perfil à lista de usuários
        self.__usuarios.append(perfil)
    
    def buscar(self, nome_usuario):
        # Percorre a lista de usuários
        for usuario in self.__usuarios:
            # Se o nome de usuario existe retorna o perfil encontrado
            if usuario.get_usuarios() == nome_usuario:
                return usuario
        # se não, retorna None
        return None