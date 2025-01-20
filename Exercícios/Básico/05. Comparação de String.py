#5. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Variáveis com as strings para comparação
primeira = "Brasil Hexa 2006"
segunda = "Brasil! Hexa 2006!"

def string(dado, dado2):
    """
    Função que compara duas strings fornecidas pelo usuário, verificando o tamanho, 
    a igualdade de conteúdo e se ambos os dados são strings.

    A função exibe:
    1. O tamanho das strings.
    2. Se as strings possuem o mesmo tamanho.
    3. Se as strings possuem o mesmo conteúdo.

    """
    while True:
        try:
            # Verifica se ambos são strings
            if isinstance(dado, str) and isinstance(dado2, str):
                tamanho = len(dado)
                tamanho2 = len(dado2)
                
                print(f"O tamanho da primeira string é {tamanho} caracteres")
                print(f"O tamanho da segunda string é {tamanho2} caracteres")
                
                # Verifica se os tamanhos são iguais
                if tamanho == tamanho2:
                    print("As duas strings são de mesmo tamanho.")
                else:
                    print("As duas strings são de tamanhos diferentes.")
                    
                # Verifica se o conteúdo é igual
                if dado == dado2:
                    print("As duas strings possuem o mesmo conteúdo.")
                else:
                    print("As duas strings possuem conteúdo diferente.")
                break

            else:
                print("Os dados inseridos não são strings")
                break
            
        except ValueError:
            print("Houve um erro inesperado, tente novamente")
            break

# Chamada da função para realizar a comparação das strings
string(primeira, segunda)
