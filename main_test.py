import unittest  # Importa o módulo unittest para criar e executar testes unitários
from main import *  # Importa todos os elementos do módulo main
from datetime import datetime  # Importa a classe datetime do módulo datetime

# Função geradora de IDs para teste
def gerador_id():
    yield 1  # Gera o ID 1

# Cria dois perfis para teste
perfil1 = Perfil("usuario1")
perfil2 = Perfil("usuario2")
perfil3 = Perfil("usuario3")

# Cria dois tweet para teste
tweet1 = Tweet("usuario1", "mensagem1", gerador_id())
tweet2 = Tweet("usuario1", "mensagem2", gerador_id())

# Define uma classe de teste que herda de unittest.TestCase
class TesteTweet(unittest.TestCase):
    # Define um método de teste para o método get_id da classe Tweet
    def test_get_id(self):
        # Verifica se o método get_id retorna o ID correto
        self.assertEqual(tweet1.get_id(), 1)

    # Define um método de teste para o método get_usuario da classe Tweet
    def test_get_usuario(self):
        # Verifica se o método get_usuario retorna o usuário correto
        self.assertEqual(tweet1.get_usuario(), "usuario1")

    # Define um método de teste para o método get_mensagem da classe Tweet
    def test_get_mensagem(self):
         # Verifica se o método get_usuario retorna o usuário correto
        self.assertEqual(tweet1.get_mensagem(), "mensagem1")
    
    def teste_get_data_postagem(self):
         # Verifica se o método get_usuario retorna o usuário correto
        self.assertEqual(tweet1.get_data_postagem(), datetime.today().replace(second=0, microsecond=0))

class TestPerfil(unittest.TestCase):
    def test_add_seguidor(self):
        # Adiciona perfil2 como seguidor de perfil1
        perfil1.add_seguidor(perfil2)
        # Verifica se perfil2 foi adicionado à lista de seguidores de perfil1
        self.assertIn(perfil2, perfil1.get_seguidores())
        
    def test_add_seguidos(self):
        # Adiciona perfil2 como seguido de perfil1
        perfil1.add_seguidos(perfil2)
        # Verifica se perfil2 foi adicionado à lista de seguidos de perfil1
        self.assertIn(perfil2, perfil1.get_seguidos())

    def teset_add_tweet(self):
        # Adicona o tweet ao perfil
        perfil1.add_tweet(tweet1)
        # Verifica se o tweet foi adiconado à lista de tweets do perfil
        self.assertIn(tweet1, perfil1.get_tweet())
        # Verifica se os tweets estão ordenados pela data de postagem
        self.assertEqual(tweet1, perfil1.get_tweets())

    def test_get_tweets(self):
        # Adicona os tweets ao perfil
        perfil1.add_tweet(tweet1)
        perfil2.add_tweet(tweet2)
        # Verifica se os tweets estão ordenados pela data de postagem
        tweets = perfil1.get_tweets()
        self.assertEqual(tweets, sorted(tweets, key=lambda tweet: tweet.get_data_postagem()))

    def test_get_seguidos(self):
        # Adicona perfil2 e perfil3 como seguido de perfil1
        perfil1.add_seguidos(perfil2)
        perfil1.add_seguidos(perfil3)
        # Verifica se o método get_seguidos retorna a lista correta de perfis seguidos
        self.assertEqual(perfil1.get_seguidos(), [perfil2, perfil3])
    
    def test_get_seguidores(self):
        # Adicona perfil2 e perfil3 como seguidores de perfil1
        perfil1.add_seguidor(perfil2)
        perfil1.add_seguidor(perfil3)
        # Verifica se o método get_seguidos retorna a lista correta de perfis seguidos
        self.assertEqual(perfil1.get_seguidores(), [perfil2, perfil3])

    def test_get_tweet(self):
        # Adicona tweets ao perfil
        perfil1.add_tweet(tweet1)
        perfil1.add_tweet(tweet2)
        # Verifica se o método get_tweet retorna o tweet correto pelo ID
        self.assertEqual(perfil1.get_tweet(tweet1.get_id()), tweet1)
        self.assertEqual(perfil1.get_tweet(tweet2.get_id()), tweet2) # Dando erro
        # Verifica se o método get_tweet retorna None para um ID inexistente
        self.assertIsNone(perfil1.get_tweet(999)) 


    def test_get_timeline(self):
        pass

    def test_set_usuario(self):
        pass

    def test_get_usuario(self):
        pass

    def test_set_ativo(self):
        pass

    def test_is_ativo(self):
        pass


# Executa os testes se o script for executado diretamente
if __name__ == '__main__':
    unittest.main()