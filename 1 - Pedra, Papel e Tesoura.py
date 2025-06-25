# Github: jessicaevelin
# Data: 25/06/2025
# Azimov - Python Starter

import random

opcoes = {0: 'Papel', 1: 'Pedra', 2: 'Tesoura'}

resultado = []

def jogo(esc, comp):
    print('===========================================')
    print(f'Sua jogada: {esc} - {opcoes[esc]}')
    print(f'Jogada do computador: {comp} - {opcoes[comp]}')

    if esc == comp:
        print('Empate!')
        resultado.append('Empate')
    elif (esc == 0 and comp == 1) or (esc == 1 and comp == 2) or (esc == 2 and comp == 0):
        print('Você venceu!')
        resultado.append('Usuário')
    else:
        print('O Computador venceu')
        resultado.append('Computador')
    print('===========================================')


# Introdução
print('===========================================')
print('Bem vindo ao jogo de Papel, Pedra e Tesoura')
print('===========================================')

# Loop de entrada
while True:
    try:
        print('Escolha seu lance:')
        print('0 - Papel | 1 - Pedra | 2 - Tesoura')
        esc = int(input("Digite um número entre 0 e 2: "))
        if 0 <= esc <= 2:
            comp = random.randint(0, 2)
            jogo(esc, comp)
            
            print('Placar')
            print(f'Você: {resultado.count("Usuário")}')
            print(f'Computador: {resultado.count("Computador")}')
            print(f'Empate: {resultado.count("Empate")}')
            print('===========================================')
            
            # Perguntar se quer continuar
            while True:
                try:
                    continuar = int(input("Digite 0 para jogar novamente ou 1 para sair: "))
                    print('===========================================')
                    if continuar == 0:
                        break  # volta ao início do loop
                    elif continuar == 1:
                        print("Jogo encerrado!")
                        exit()
                    else:
                        print("Digite apenas 0 ou 1.")
                except ValueError:
                    print("Entrada inválida. Use 0 ou 1.")
    
        else:
            print("Número fora do intervalo. Tente novamente.\n")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")

print('Jogo encerrado!')
