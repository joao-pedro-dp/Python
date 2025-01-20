#3. Crie um programa para cadastrar produtos  e exiba uma lista atualizada dos produtos cadastrados

# Lista de produtos vazia para armazenar os produtos cadastrados
produtos = []

def cadastro_produto():
    """
    Função que solicita ao usuário o nome de um produto e o preço,
    cadastrando-os em uma lista de produtos sem permitir duplicatas no nome.

    A função continua solicitando a inserção de novos produtos até que o
    usuário digite 'sair' para encerrar o processo.

    """
    while True:
        try:
            # Solicitar entrada do nome do produto
            user = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
            
            # Verificar se o usuário deseja sair
            if user == 'sair':
                break
            
            # Verificar se o produto já foi cadastrado
            elif user not in produtos:
                produtos.append(user)  # Adicionar produto à lista
                print("Produto cadastrado com sucesso!")
            else:
                # Informar ao usuário que o produto já existe
                print("Produto já existe, tente novamente")
        
        except ValueError:
            # Tratamento para erros inesperados
            print("Houve um erro inesperado, tente novamente")

# Chamada da função para iniciar o cadastro dos produtos
cadastro_produto()

# Exibir a lista atualizada de produtos cadastrados
print("Lista de produtos atualizada:", produtos)
