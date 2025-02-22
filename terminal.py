from exception import *  # Importa as exceções
from datetime import datetime
from main import *

class TerminalTwitter:
    def __init__(self, my_twitter):
        self.my_twitter = my_twitter
    
    def menu(self):
        while True:
            print("\nMyTwitter\n")
            print("0. Meu Twitter")
            print("1. Criar perfil")
            print("2. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                self.meu_twitter()
            elif opcao == "1":
                self.criar_perfil()
            elif opcao == "2":
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def meu_twitter(self):
        usuario = input("Digite seu usuário: ")
    
        perfil = self.my_twitter._MyTwitter__repositorio.buscar(usuario)  # Busca o perfil no repositório
        if perfil is None:
            print("Erro: Usuário não encontrado! Crie um perfil primeiro.")
            return  # Sai do método caso o perfil não exista
    
        try:
            while True:
                print(f"\nMeu Twitter: {usuario}")
                print("1. Tweetar")
                print("2. Ver timeline")
                print("3. Ver seguidores")
                print("4. Ver seguidos")
                print("5. Seguir usuário")
                print("6. Voltar")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    self.tweetar(usuario)
                elif opcao == "2":
                    self.ver_timeline(usuario)
                elif opcao == "3":
                    self.ver_seguidores(usuario)
                elif opcao == "4":
                    self.ver_seguidos(usuario)
                elif opcao == "5":  
                    self.seguir_usuario(usuario)
                elif opcao == "6":
                    break
                else:
                    print("Opção inválida! Tente novamente.")
    
        except PIException:
            print("Erro: Perfil inexistente!")
        except PDException:
            print("Erro: Perfil desativado!")

    def criar_perfil(self):
        usuario = input("Digite o nome do usuário: ")
        tipo = input("Tipo de perfil (1 - Pessoa Física, 2 - Pessoa Jurídica): ")
        try:
            if tipo == "1":
                cpf = input("Digite o CPF: ")
                if self.my_twitter.verificar_cpf_cnpj_existente(cpf):
                    print("Erro: Já cadastrado!")
                    return
                perfil = PessoaFisica(usuario, cpf)
            elif tipo == "2":
                cnpj = input("Digite o CNPJ: ")
                if self.my_twitter.verificar_cpf_cnpj_existente(cnpj):
                    print("Erro: Já cadastrado!")
                    return
                perfil = PessoaJuridica(usuario, cnpj)
            else:
                print("Opção inválida!")
                return

            self.my_twitter.criar_perfil(perfil)
            print("Perfil criado com sucesso!")
        except PEException:
            print("Erro: Perfil já existe!")

    def tweetar(self, usuario):
        mensagem = input("Digite sua mensagem (máx. 140 caracteres): ")
        try:
            self.my_twitter.tweetar(usuario, mensagem)
            print("Tweet enviado com sucesso!")
        except MFPException:
            print("Erro: A mensagem deve ter entre 1 e 140 caracteres!")
        except PIException:
            print("Erro: Perfil inexistente!")
        except PDException:
            print("Erro: Perfil desativado!")

    def ver_seguidores(self, usuario):
        try:
            seguidores = self.my_twitter.seguidores(usuario)
            if not seguidores:
                print("Você ainda não tem seguidores.")
            else:
                print("\nSeus seguidores:")
                for seguidor in seguidores:
                    print(f"- {seguidor.get_usuario()}")
        except PIException:
            print("Erro: Perfil inexistente!")
        except PDException:
            print("Erro: Perfil desativado!")

    def ver_seguidos(self, usuario):
        try:
            seguidos = self.my_twitter.seguidos(usuario)
            if not seguidos:
                print("Você ainda não segue ninguém.")
            else:
                print("\nVocê segue:")
                for seguido in seguidos:
                    print(f"- {seguido.get_usuario()}")
        except PIException:
            print("Erro: Perfil inexistente!")
        except PDException:
            print("Erro: Perfil desativado!")

    def seguir_usuario(self, usuario):
        seguido = input("Digite o nome do usuário que deseja seguir: ")
        try:
            self.my_twitter.seguir(usuario, seguido)
            print(f"Agora você está seguindo {seguido}!")
        except PIException:
            print("Erro: Um dos perfis não existe!")
        except PDException:
            print("Erro: Um dos perfis está desativado!")
        except SIException:
            print("Erro: Você não pode seguir a si mesmo!")

    def ver_timeline(self, usuario):
        try:
            timeline = self.my_twitter.timeline(usuario)
            if not timeline:
                print("Sua timeline está vazia!")
            else:
                print("\nTimeline:")
                for tweet in timeline:
                    print(f"{tweet.get_usuario()} ({tweet.get_data_postagem()}): {tweet.get_mensagem()}")
        except PIException:
            print("Erro: Perfil inexistente!")
        except PDException:
            print("Erro: Perfil desativado!")


if __name__ == "__main__":
    from main import MyTwitter  # Importa a classe principal do sistema
    my_twitter = MyTwitter()
    terminal = TerminalTwitter(my_twitter)
    terminal.menu()
