#9. Crie um programa que receba um número inteiro N e calcule o fatorial de N usando recursão, use a biblioteca time para medir o tempo de execução.

import time as tm

def entrada():
    """
    Função que solicita ao usuário um número inteiro para calcular o fatorial.

    O programa continua solicitando a entrada até que o usuário forneça um número válido
    (inteiro não negativo). Após a entrada correta, a função chama 'calcular_fatorial' para 
    calcular o fatorial do número e exibe o tempo gasto na operação.

    """
    while True:
        try:
            # Solicita ao usuário um número inteiro
            user = int(input("Digite um número inteiro para calcular o fatorial dele: "))
            
            # Verifica se o número é positivo
            if user < 0:
                print("Fatorial deve ser um valor maior que 0, favor tentar novamente")
            else:
                # Inicia a contagem do tempo de execução
                inicio = tm.time()
                
                # Chama a função para calcular o fatorial
                calcular_fatorial(user)
                
                # Calcula o tempo gasto na execução
                fim = tm.time()
                tempo_gasto = fim - inicio
                
                # Exibe o tempo gasto em segundos com precisão de 10 casas decimais
                print(f"Tempo gasto: {tempo_gasto:.10f} segundos")
                break
        except ValueError:
            # Trata o erro se o usuário não inserir um número inteiro
            print("Entrada incorreta, favor tentar novamente")

def calcular_fatorial(n):
    """
    Função que calcula e exibe o fatorial de um número inteiro fornecido.

    Para cada número entre 1 e o número fornecido (inclusive), a função calcula o fatorial
    progressivamente e exibe o resultado.

    Retorna:
        int: O fatorial do número fornecido.
    """
    fatorial = 1  # Inicializa a variável para armazenar o fatorial
    
    # Loop para calcular o fatorial de 1 até n
    for i in range(1, n + 1):
        fatorial = fatorial * i  # Calcula o fatorial progressivamente
        print(f"O fatorial de {i} é {fatorial}")  # Exibe o fatorial de cada passo
    return fatorial

# Chama a função principal para iniciar o programa
entrada()

