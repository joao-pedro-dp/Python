#7. Crie um programa que gerencie um dicionário de contatos telefônicos. O programa deve permitir ao usuário adicionar, remover e buscar contatos. Além disso, o programa deve exibir todos os contatos cadastrados.

def adicionar(calendario_contatos):
    """
    Função que adiciona um novo contato ao calendário de contatos.

    Solicita ao usuário um nome e um número de telefone.
    Se o número não estiver presente no calendário de contatos, o novo contato é adicionado.
    Caso o número já exista, o usuário é informado e solicitado a tentar novamente.
    
    """
    while True:
        nome = input("Adicione um Nome: ")
        numero = input("Adicione um Telefone: ")

        # Verificar se o número já existe no calendário
        if numero not in calendario_contatos.values():
            calendario_contatos[nome] = numero
            print(f"Contato {nome} adicionado com sucesso!")
            break
        else:
            print("Número existente na lista, tente novamente.")

def deletar(calendario_contatos):
    """
    Função que remove um contato do calendário de contatos.

    Solicita ao usuário o nome de um contato e remove-o, caso ele esteja presente.
    Se o contato não existir, o usuário é informado.
    
    """
    nome = input("Digite um nome para remover: ")
    
    # Verificar se o contato existe no calendário
    if nome in calendario_contatos:
        del calendario_contatos[nome]
        print(f"Contato {nome} removido com sucesso!")
    else:
        print("Contato não existente na lista.")

def buscar(calendario_contatos):
    """
    Função que busca e exibe o número de telefone de um contato específico.

    Solicita ao usuário o nome de um contato e exibe o número de telefone correspondente.
    Caso o nome não exista, o usuário é informado.
    
    """
    nome = input("Digite um nome que deseja buscar: ")

    # Verificar se o contato existe no calendário
    if nome in calendario_contatos:
        print(f"O telefone de {nome} é {calendario_contatos[nome]}")
    else:
        print("Contato não existente na lista.")

def todos(calendario_contatos):
    """
    Função que exibe todos os contatos presentes no calendário.

    Percorre o calendário de contatos e exibe os nomes e seus respectivos números.
    Se o calendário estiver vazio, o usuário é informado.
    
    """
    # Verificar se o calendário está vazio
    if calendario_contatos:
        print("Os contatos cadastrados são:")
        for nome, numero in calendario_contatos.items():
            print(f"O telefone de {nome} é {numero}")
    else:
        print("Nenhum contato existente na lista.")

def menu():
    """
    Função que exibe um menu de opções para gerenciar o calendário de contatos.

    O usuário pode escolher adicionar, remover, buscar contatos, exibir todos os contatos ou encerrar o programa.
    O processo continua até que o usuário escolha a opção de sair.

    """
    # Dicionário para armazenar os contatos
    calendario_contatos = {}
    
    # Loop contínuo para o menu de opções
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Exibir todos os contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        # Verificar a escolha do usuário e chamar a função correspondente
        if opcao == "1":
            adicionar(calendario_contatos)
        elif opcao == "2":
            deletar(calendario_contatos)
        elif opcao == "3":
            buscar(calendario_contatos)
        elif opcao == "4":
            todos(calendario_contatos)
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o menu
menu()
