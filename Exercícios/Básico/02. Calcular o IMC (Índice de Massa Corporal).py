#2. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: $P = 72,7h - 58$
#b. Para mulheres: $P = 62,1h - 44,7$


def pede_escolha():
    """
    Função que solicita ao usuário o sexo (H ou M) e retorna a escolha.
    A função lida com entradas inválidas e continua pedindo até receber uma resposta válida.
    
    Retorna:
    str: O sexo do usuário ('h' ou 'm').
    """
    while True: 
        try:
            # Solicita o sexo do usuário (H ou M)
            sexo = input("Qual o seu sexo? (H ou M): ").lower()
            if sexo in ("h", "m"):
                return sexo
        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar um número")

def pede_altura():
    """
    Função que solicita a altura do usuário em metros e retorna o valor.
    Lida com entradas inválidas e continua pedindo até receber um número válido.
    
    Retorna:
    float: A altura do usuário em metros.
    """
    while True: 
        try:
            # Solicita a altura do usuário em metros
            altura = float(input("Informe a sua altura em METROS: "))
            return altura
        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar sua altura em METROS.")

def calcula():
    """
    Função que calcula o peso ideal com base no sexo e altura fornecidos.
    Utiliza fórmulas diferentes dependendo do sexo (masculino ou feminino).
    Lida com entradas inválidas e exibe o peso ideal do usuário.
    
    Retorna:
    float: O peso ideal calculado.
    """
    while True:
        try:
            # Solicita o sexo e a altura
            sexo = pede_escolha()
            altura = pede_altura()

            # Calcula o peso ideal dependendo do sexo
            if sexo == "m":
                calculo = ((62.1 * altura) - 44.7)  # Fórmula para mulheres
            else:
                calculo = ((72.7 * altura) - 58)   # Fórmula para homens

            # Exibe o peso ideal calculado
            print(f"O seu peso ideal será: {calculo:.2f} KG ")
            break
        except ValueError: 
            # Trata qualquer erro inesperado
            print("Erro")

    return calculo

# Chamada da função
calcula()
