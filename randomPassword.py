from operator import add
import random
import string

class Senha:

    # função checa entradas do usuário para a geração de strings semirandômicas com ou sem símbolos
    def gera_senha(qtd, escolha):
        if escolha == 2:
            chars=(string.ascii_letters + string.digits) 
            return ''.join(random.choice(chars) for x in range(qtd))
        elif escolha == 1:
            chars=(string.digits + string.ascii_letters + string.punctuation)
            return ''.join(random.choice(chars) for x in range(qtd))


    # função pergunta se usuário quer ou não símbolos na senha
    def valida_escolha():
        valor = input("Deseja adcionar símbolo? (y or n): ")
        valor.lower()
        if valor == 'y' or 's':
            return 1
        elif valor == 'n':
            return 2
        else:
            raise ValueError("Você inseriu um valor errado!")


    # função pergunta a quantidade de caracteres o usuário deseja
    def define_qtd_char():
        qtd = input("\nDigite o número de caracteres desejado: ")
        try:
            qtd = int(qtd)
            return qtd
        except ValueError:
            raise ValueError("Você inseriu um valor não inteiro!")


    #função pergunta usuário e endereço para serem utilizados com a senha a ser gerada
    def cria_cadastro():
        user = input('\nDigite o usuário dessa senha: ')
        address = input('Digite em que endereço essa conta será necessária: ')
        return (user, address)
