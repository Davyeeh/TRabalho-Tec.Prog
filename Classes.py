from datetime import datetime
# Início das classes

# Davi

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

#Métodos adicionados pelo gabriel

     # Método para adicionar um seguidor ao perfil
    def add_seguidor(self, perfil):
        if perfil not in self.__seguidores:
            self.__seguidores.append(perfil)
    
     # Método para seguir outro perfil
    def add_seguidos(self, perfil):
        if perfil not in self.__seguidos:
            self.__seguidos.append(perfil)

    # Método para adicionar um tweet à lista do perfil
    def add_tweet(self, tweet):
        self.__tweets.append(tweet)
        self.__tweets.sort(key=lambda t: t.get_data_postagem())  # Ordena os tweets pela data
    
    # Método para obter todos os tweets do perfil, ordenados por data
    def get_tweets(self):
        return sorted(self.__tweets, key=lambda t: t.get_data_postagem())
    
    # Método para obter um tweet específico pelo ID
    def get_tweet(self, tweet_id):
        for tweet in self.__tweets:
            if tweet.get_id() == tweet_id:
                return tweet
        return None  # Retorna None se o tweet não for encontrado

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
        return self.__cnpj

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
    

# Gabriel

class Tweet:
    def __init__(self, usuario, mensagem, gerador_id):
        self.__id = next(gerador_id) # Gera o ID único usando a função geradora
        self.__usuario = usuario # Nome do usuário que postou
        self.__mensagem = mensagem # Conteúdo do tweet
        self.__data_postagem = datetime.now() # Data e hora da postagem geradas automaticamente
        
    # Métodos de acesso (getters)

    def get_id(self):
        return self.__id

    def get_usuario(self):
        return self.__usuario

    def get_mensagem(self):
        return self.__mensagem

    def get_data_postagem(self):
        return self.__data_postagem