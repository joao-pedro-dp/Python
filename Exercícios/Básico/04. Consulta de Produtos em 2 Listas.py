#4. Crie um sistema de consulta de preços seu sistema deve:
#a. Pedir para o usuário o nome de um produto
#b. Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#c. Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

# Listas de produtos e seus respectivos preços
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

# Função para consultar o preço de um produto
def consulta():
    """
    Função que solicita ao usuário o nome de um produto e exibe o preço correspondente.
    O processo continua até que o produto seja encontrado na lista de produtos.
    
    Caso o produto não seja encontrado, a função solicita uma nova tentativa.

    """
    while True:
        try:
            # Solicitar entrada do nome do produto
            user = input("Digite o nome do produto: ").lower()
            
            # Verificar se o produto está na lista
            if user in produtos:
                # Obter o índice do produto e exibir o preço
                indice = produtos.index(user)
                print(f"O preço do {user} é: R${precos[indice]}")
                break
            else:
                print("Produto não encontrado, tente novamente!")
        except ValueError:
            print("Houve um erro inesperado, tente novamente.")

# Chamada da função para realizar a consulta
consulta()
