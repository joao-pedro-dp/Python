#10. Criar um programa que leia uma lista de 10 números e calcule o menor e o maior número da lista e a soma de todos os números que são múltiplos de 3 ou 5 da mesma.

def maior_menor(lista):
    """
    Função que recebe uma lista de números inteiros e exibe o maior e o menor número presentes nela.

    Argumentos:
        lista (list): Lista de números inteiros.
    """
    # Encontrar o maior número na lista
    maior = max(lista)
    print(f"O maior número da lista é {maior}")
    
    # Encontrar o menor número na lista
    menor = min(lista)
    print(f"O menor número da lista é {menor}")

def multiplos(lista):
    """
    Função que recebe uma lista de números inteiros, filtra os múltiplos de 3 ou 5 e calcula a soma desses múltiplos.

    Argumentos:
        lista (list): Lista de números inteiros.
    """
    # Lista para armazenar os múltiplos de 3 ou 5
    new_lista = []
    
    # Iterar sobre cada número na lista
    for i in lista:
        # Verificar se o número é múltiplo de 3 ou 5
        if i % 3 == 0 or i % 5 == 0:
            new_lista.append(i)
            print(f"O número {i} é múltiplo de 3 ou 5")
    
    # Calcular a soma dos múltiplos encontrados
    soma = sum(new_lista)
    print(f"A soma deles é: {soma}")

def pede():
    """
    Função que solicita ao usuário a inserção de 10 números inteiros, armazena-os em uma lista e chama as funções
    'maior_menor' e 'multiplos' para processar essa lista.
    """
    lista = []
    try:
        # Solicitar ao usuário a inserção de 10 números inteiros
        for i in range(10):
            user = int(input("Insira um número inteiro para a lista: "))
            lista.append(user)
            print(f"O numero inserido foi: {user}")
        
        # Chamar a função para exibir o maior e o menor número
        maior_menor(lista)
        
        # Chamar a função para exibir os múltiplos de 3 ou 5 e a soma deles
        multiplos(lista)
    
    except ValueError:
        # Tratar o erro caso o usuário insira um valor que não seja um número inteiro
        print("Por favor, insira números inteiros válidos.")

# Chamar a função principal para iniciar o programa
pede()
