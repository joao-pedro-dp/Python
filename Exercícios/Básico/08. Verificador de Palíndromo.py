#8. Crie um programa que receba uma string do usuário e verifique se ela é um palíndromo (ou seja, se a palavra é a mesma quando lida de trás para frente).

def eh_palindromo(string):
    """
    Função que verifica se uma string é um palíndromo.

    Um palíndromo é uma palavra, frase ou número que pode ser lido da mesma forma, 
    independentemente de ser lido da esquerda para a direita ou da direita para a esquerda.

    A função ignora espaços e não diferencia maiúsculas de minúsculas.

    Argumentos:
        string (str): A string que será verificada.

    Retorna:
        bool: Retorna True se a string for um palíndromo, caso contrário retorna False.
    """
    # Remover espaços e transformar a string para minúsculas
    string = string.replace(" ", "").lower()
    
    # Inverter a string
    inverso_string = string[::-1]
    
    # Verificar se a string invertida é igual à original
    return inverso_string == string

def verificar_palindromos():
    """
    Função que solicita repetidamente ao usuário uma palavra, frase ou número 
    para verificar se é um palíndromo.

    A função continua solicitando entradas até que o usuário digite 'sair'. 
    No final, exibe quantos palíndromos foram encontrados durante o processo.
    """
    contagem_palindromos = 0  # Variável para contar o número de palíndromos verificados
    
    # Loop para solicitar entradas do usuário até que ele escolha encerrar
    while True:
        entrada = input("Digite uma palavra, frase ou número (ou 'sair' para terminar): ")
        
        # Verificar se o usuário deseja sair
        if entrada.lower() == 'sair':
            break
        
        # Verificar se a entrada é um palíndromo usando a função eh_palindromo
        if eh_palindromo(entrada):
            print(f"'{entrada}' é um palíndromo!")
            contagem_palindromos += 1
        else:
            print(f"'{entrada}' não é um palíndromo.")
    
    # Exibir a quantidade de palíndromos verificados
    print(f"Você verificou {contagem_palindromos} palíndromo(s).")

# Chamar a função principal para iniciar o programa
verificar_palindromos()
