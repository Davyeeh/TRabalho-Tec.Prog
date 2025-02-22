# Exceções específicas do sistema

class PEException(Exception):  # Perfil Existente
    pass

class PIException(Exception):  # Perfil Inexistente
    pass

class PDException(Exception):  # Perfil Desativado
    pass

class MFPException(Exception):  # Mensagem Fora do Padrão
    pass

class SIException(Exception):  # Seguidor Inválido
    pass

# Exceção para usuário já cadastrado
class UJCException(Exception):
    pass

class UNCException(Exception):  # Usuário Não Cadastrado
    pass