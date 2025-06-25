def menu():
    print('\nEscolha uma operação abaixo')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão\n')

opcoes = {1: 'Soma', 2: 'Subtração', 3:'Multiplicação', 4: 'Divisão'}

def selecao():
    while True:
        try:
            selecao = int(input())
            if selecao in (1, 2, 3, 4):
                if selecao in (1, 2, 3, 4):
                    print(f'Você escolheu: {selecao} - {opcoes[selecao]}')
                return selecao
            else:
                print("Número fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def obter_numeros():
    while True:
        try:
            num1 = int(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    while True:
        try:
            num2 = int(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    return num1, num2

def calcular(num1, num2, selecao):
    if selecao == 1:
        return num1 + num2
    elif selecao == 2:
        return num1 - num2    
    elif selecao == 3:
        return num1 * num2
    elif selecao == 4:
        return num1 / num2
    
def mostrar_resultado(resultado):
    print(f'O resultado é {resultado}')
    
def quer_continuar():
    while True:
        try:
            continuar = int(input('Digite 1 para jogar novamente ou 0 para sair: '))
            if continuar == 1:
                break
            elif continuar == 0:
                print('A calculadora foi encerrada pelo usuário')
                exit()
        except ValueError:
                print("Entrada inválida. Use 0 ou 1.")

while True:
    menu()
    operacao = selecao()
    numeros = obter_numeros()
    resultado = calcular(numeros[0], numeros[1], operacao)
    mostrar_resultado(resultado)
    quer_continuar()

