import unittest  # Importa o módulo unittest para criar e executar testes unitários
from main import *  # Importa todos os elementos do módulo main
from datetime import datetime  # Importa a classe datetime do módulo datetime

# Função geradora de IDs para teste
def gerador_id():
    yield 1  # Gera o ID 1

# Define uma classe de teste que herda de unittest.TestCase
class TesteTweet(unittest.TestCase):
    # Define um método de teste para o método get_id da classe Tweet
    def test_get_id(self):
        # Cria uma instância da classe Tweet usando a função geradora de ID
        tweet = Tweet("usuario_test", "mensagem_test", gerador_id())
        # Verifica se o método get_id retorna o ID correto
        self.assertEqual(tweet.get_id(), 1)

    # Define um método de teste para o método get_usuario da classe Tweet
    def test_get_usuario(self):
        # Cria uma instância da classe Tweet usando a função geradora de ID
        tweet = Tweet("usuario_test", "mensagem_test", gerador_id())
        # Verifica se o método get_usuario retorna o usuário correto
        self.assertEqual(tweet.get_usuario(), "usuario_test")

    # Define um método de teste para o método get_mensagem da classe Tweet
    def test_get_mensagem(self):
        # Cria uma instância da classe Tweet usando a função geradora de ID
        tweet = Tweet("usuario_test", "mensagem_test", gerador_id())
         # Verifica se o método get_usuario retorna o usuário correto
        self.assertEqual(tweet.get_mensagem(), "mensagem_test")
    
    def teste_get_data_postagem(self):
        # Cria uma instância da classe Tweet usando a função geradora de ID
        tweet = Tweet("usuario_test", "mensagem_teste", gerador_id())
         # Verifica se o método get_usuario retorna o usuário correto
        self.assertEqual(tweet.get_data_postagem(), datetime.now().replace(second=0, microsecond=0))

# Executa os testes se o script for executado diretamente
if __name__ == '__main__':
    unittest.main()