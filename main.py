# from randomPassword import cria_cadastro, define_qtd_char, gera_senha, valida_escolha
from randomPassword import Senha

#inicia aplicação
print("Welcome to NwT Password Generator! v. 1.0\n")
print("Essa aplicação gera senhas com letras miaúsculas e minúsculas, números por padrão.")

#usuário escolhe com ou sem símbolos
escolha = Senha.valida_escolha()

#usuário escolhe quantidade de dígitos
qtd_char = Senha.define_qtd_char()

#usuário informa usuario e endereço para utilização da senha
user, address = Senha.cria_cadastro()

#aplicação imprime usuário, endereço e senha
print(f"\nUsuário: {user}  -  Endereço: {address}  -  Senha: {Senha.gera_senha(qtd_char, escolha)}")