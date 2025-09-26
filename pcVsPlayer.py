# Importa a biblioteca random para gerar números aleatórios
import random

# Gera um número aleatório entre 0 e 10 (inclusive) e armazena na variável 'pc'
pc = random.randint(0, 10)  # Computador pensa em um número

# Informa ao jogador que deve tentar adivinhar o número
print("vou pensar em um numero entre 0 a 10, adivinhe o numero: ")

# Solicita que o jogador digite um número
jogador = int(input("em que numero pensei? "))  # Jogador tenta adivinhar

# Verifica se o número digitado pelo jogador é igual ao número sorteado
if jogador == pc:
    print("O numero sorteado foi {}"
          "\nVocê ganhou! Parabéns!".format(pc))
# Se os números forem diferentes, o jogador errou
else:
    print("O numero sorteado foi {} "
          "\nNão foi dessa vez, tente novamente!".format(pc))
