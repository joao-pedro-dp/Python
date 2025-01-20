#1. Você tem uma lista de tuplas representando pessoas e suas idades. Cada tupla contém o nome da pessoa e sua idade. Seu objetivo é:
#a.Encontrar a pessoa mais velha.
#b.Encontrar a pessoa mais jovem.
#c.Calcular a média de idade das pessoas

# Lista de tuplas contendo nomes e idades
pessoas = [
    ('João', 25),
    ('Julia', 30),
    ('Marcus', 22),
    ('Maria', 28),
    ('Ana', 35),
    ('Alon', 21)
]

def lista_tupla():
    """
    Função que percorre uma lista de tuplas contendo nomes e idades, e exibe:
    - O nome e idade da pessoa de maior idade.
    - O nome e idade da pessoa de menor idade.
    - A média das idades.
    """
    
    # Listas para armazenar nomes e idades separadamente
    lista_nome = []
    lista_idade = []

    # Preenchendo as listas de nomes e idades a partir da lista de tuplas
    for nome, idade in pessoas:
        lista_idade.append(idade)
        lista_nome.append(nome)

    # Encontrando o índice da pessoa com a maior idade
    maior_idade = lista_idade.index(max(lista_idade))
    print(f"A pessoa de maior idade é {lista_nome[maior_idade]} que tem {lista_idade[maior_idade]} anos")

    # Encontrando o índice da pessoa com a menor idade
    menor_idade = lista_idade.index(min(lista_idade))
    print(f"A pessoa de menor idade é {lista_nome[menor_idade]} que tem {lista_idade[menor_idade]} anos")

    # Calculando a média das idades
    media_idades = sum(lista_idade)/len(lista_idade)
    print(f"A média das idades é {media_idades:.2f}")

# Chamada da função para exibir os resultados
lista_tupla()
