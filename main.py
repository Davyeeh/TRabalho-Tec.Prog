from datetime import datetime
from exception import PEException, PIException, PDException, MFPException, SIException, UJCException, UNCException
# Início das classes

#Gabriel

class Tweet:
    def __init__(self, usuario, mensagem, gerador_id):
        self.__id = next(gerador_id) # Gera o ID único usando a função geradora
        self.__usuario = usuario # Nome do usuário que postou
        self.__mensagem = mensagem # Conteúdo do tweet
        self.__data_postagem = datetime.today().replace(second=0, microsecond=0) # Data e hora da postagem geradas automaticamente
        
    # Métodos de acesso (getters)

    def get_id(self):
        return self.__id

    def get_usuario(self):
        return self.__usuario

    def get_mensagem(self):
        return self.__mensagem

    def get_data_postagem(self):
        return self.__data_postagem

# Davi

# Classe Perfil que representa um perfil de usuário
class Perfil:
    def __init__(self, usuario):
        self.__usuario = usuario  # Nome de usuário do perfil
        self.__seguidos = []  # Perfis seguidos pelo usuário
        self.__seguidores = []  # Perfis que seguem o usuário
        self.__tweets = []  # Tweets do perfil
        self.__ativo = True  # Indica se o perfil está ativo

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
        self.__tweets.sort(key=lambda tweet: tweet.get_data_postagem())  # Ordena os tweets pela data
    
    # Método para obter todos os tweets do perfil, ordenados por data
    def get_tweets(self):
        return sorted(self.__tweets, key=lambda tweet: tweet.get_data_postagem())
    
    # Método para obter a lista de perfis seguidos
    def get_seguidos(self):
        return self.__seguidos

    # Método para obter a lista de seguidores
    def get_seguidores(self):
        return self.__seguidores

    # Método para obter um tweet específico pelo ID
    def get_tweet(self, tweet_id):
        for tweet in self.__tweets:
            if tweet.get_id() == tweet_id:
                return tweet
        return None  # Retorna None se o tweet não for encontrado

    # Método para obter a timeline do perfil, incluindo tweets dos perfis seguidos
    def get_timeline(self):
        timeline = self.__tweets[:]  # Copia os tweets do próprio perfil
        for perfil in self.__seguidos:
            timeline.extend(perfil.get_tweets())  # Adiciona tweets dos perfis seguidos
        timeline.sort(key=lambda tweet: tweet.get_data_postagem())  # Ordena os tweets pela data de postagem
        return timeline

    # Método para seguir outro perfil
    def seguir(self, perfil):
        self.add_seguidos(perfil)
        perfil.add_seguidor(self)

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
        return self.__cnpj


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
            if usuario.get_usuario() == nome_usuario:
                return usuario
        # se não, retorna None
        return None
    
    def atualizar(self, perfil):
        for i, usuario in enumerate(self.__usuarios):
            if usuario.get_usuario() == perfil.get_usuario():
                self.__usuarios[i] = perfil  # Atualiza os dados do perfil
                return
        raise UNCException("Usuário não cadastrado")  # Lança exceção se não encontrar

class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()  # Repositório para armazenar os perfis
        self.__gerador_id = self.__gerador_id_func()  # Inicializa o gerador de IDs

    def __gerador_id_func(self):
        id = 1
        while True:
            yield id
            id += 1
    
    def verificar_cpf_cnpj_existente(self, cpf_cnpj):
        """Verifica se um CPF ou CNPJ já está cadastrado."""
        for usuario in self.__repositorio._RepositorioUsuarios__usuarios:
            if isinstance(usuario, PessoaFisica) and usuario.get_cpf() == cpf_cnpj:
                return True
            elif isinstance(usuario, PessoaJuridica) and usuario.get_cnpj() == cpf_cnpj:
                return True
        return False
        
    def criar_perfil(self, perfil):
        """ Cadastra um perfil no repositório, garantindo que não haja duplicatas. """
        if self.__repositorio.buscar(perfil.get_usuario()) is not None:
            raise PEException("Perfil já existe")
        self.__repositorio.cadastrar(perfil)

    def cancelar_perfil(self, usuario):
        """ Desativa um perfil, garantindo que ele exista e esteja ativo. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil já está desativado")
        perfil.set_ativo(False)  # Desativando o perfil

    def tweetar(self, usuario, mensagem):
        """ Posta um tweet no perfil do usuário, garantindo restrições de tamanho e existência do perfil. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil desativado")
        if not (1 <= len(mensagem) <= 140):
            raise MFPException("Mensagem deve ter entre 1 e 140 caracteres")
        
        # Criando e adicionando o tweet
        tweet = Tweet(usuario, mensagem, self.__gerador_id)
        perfil.add_tweet(tweet)

    def timeline(self, usuario):
        """ Retorna a timeline do usuário, garantindo que ele exista e esteja ativo. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil desativado")
        return perfil.get_timeline()

    def tweets(self, usuario):
        """ Retorna os tweets do perfil especificado, garantindo que ele exista e esteja ativo. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil desativado")
        return perfil.get_tweets()

    def seguir(self, seguidor, seguido):
        """ Permite que um usuário siga outro, verificando restrições de existência e estado dos perfis. """
        perfil_seguidor = self.__repositorio.buscar(seguidor)
        perfil_seguido = self.__repositorio.buscar(seguido)

        if perfil_seguidor is None or perfil_seguido is None:
            raise PIException("Perfil inexistente")
        if not perfil_seguidor.is_ativo() or not perfil_seguido.is_ativo():
            raise PDException("Um dos perfis está desativado")
        if seguidor == seguido:
            raise SIException("Um usuário não pode seguir a si mesmo")

        perfil_seguidor.add_seguidos(perfil_seguido)
        perfil_seguido.add_seguidor(perfil_seguidor)

    def numero_seguidores(self, usuario):
        """ Retorna o número de seguidores do usuário, garantindo que ele exista e esteja ativo. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil desativado")
        return len(perfil.get_seguidores())

    def seguidores(self, usuario):
        """ Retorna a lista de seguidores do usuário, garantindo que ele exista e esteja ativo. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil desativado")
        return perfil.get_seguidores()

    def seguidos(self, usuario):
        """ Retorna a lista de perfis que o usuário segue, garantindo que ele exista e esteja ativo. """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil desativado")
        return perfil.get_seguidos()

