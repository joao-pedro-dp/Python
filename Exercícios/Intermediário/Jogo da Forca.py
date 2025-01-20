"""
Este é um jogo da forca.

O jogo seleciona aleatoriamente uma palavra de uma lista predefinida. O jogador tem 7 tentativas para adivinhar as letras da palavra. 
A cada erro, o desenho da forca vai ficando mais completo, até que o jogador perca ao atingir o número máximo de tentativas.

As funcionalidades incluem:
- Receber uma letra do usuário e verificar se ela já foi tentada.
- Exibir o progresso da palavra com as letras acertadas e as erradas.
- Exibir o desenho da forca correspondente ao número de tentativas restantes.
- Informar se o jogador ganhou ou perdeu ao final do jogo.
"""
import random

# Lista de palavras para o jogo
palavras_forca = [
    "python", "sintax", "forca", "humano", "jogos",
    "trator", "antagonismo", "anotacao", "gerenciamento",
    "armazenamento", "memoria"
]

# Desenhos da forca para os diferentes níveis
forca_desenhos = [
    """
     -----
         |
         |
         |
         |
         |
    =========
    """,  # Nenhuma tentativa feita
    r"""
     -----
     |   |
         |
         |
         |
         |
    =========
    """,  # 1ª tentativa errada
    r"""
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,  # 2ª tentativa errada
    r"""
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,  # 3ª tentativa errada
    r"""
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,  # 4ª tentativa errada
    r"""
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,  # 5ª tentativa errada
    r"""
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,  # 6ª tentativa errada
    r"""
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """  # 7ª tentativa errada (perda do jogo)
]

# Função para receber a letra do usuário
def receber_letra():
    while True:
        user_input = input("Digite uma letra: ").lower()  # Pede a letra e converte para minúscula
        if len(user_input) == 1 and user_input.isalpha():  # Verifica se é uma única letra válida
            return user_input
        else:
            print("Por favor, digite apenas uma letra válida.")  # Caso o input seja inválido

# Função principal do jogo
def jogo(palavra):
    tentativas_restantes = 7  # O jogador começa com 7 tentativas
    desenhos = forca_desenhos  # Desenhos da forca
    letras_acertadas = set()  # Conjunto de letras acertadas
    letras_erradas = set()  # Conjunto de letras erradas

    print("A palavra tem {} letras.".format(len(palavra)))  # Informa o número de letras da palavra

    # Loop do jogo
    while tentativas_restantes > 0:
        # Mostrar o progresso atual da palavra
        palavra_formada = "".join([letra if letra in letras_acertadas else "_" for letra in palavra])
        print("\nPalavra: ", palavra_formada)
        print(f"Tentativas restantes: {tentativas_restantes}")
        print("Letras erradas: ", ", ".join(sorted(letras_erradas)))

        # Mostrar o desenho da forca baseado no número de tentativas restantes
        if tentativas_restantes < len(desenhos):
            print(desenhos[len(desenhos) - tentativas_restantes - 1])

        # Verificar se o jogador venceu
        if palavra_formada == palavra:
            print("Parabéns! Você ganhou!")
            return

        # Receber a letra do usuário
        letra = receber_letra()

        # Verificar se a letra já foi tentada
        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue  # Caso o jogador já tenha tentado a letra

        # Atualizar estado do jogo com base na letra
        if letra in palavra:
            letras_acertadas.add(letra)
            print("Boa! Essa letra está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas_restantes -= 1
            print("Ops! Essa letra não está na palavra.")

    # Caso o jogador perca
    print("\nVocê perdeu! A palavra era: {}".format(palavra))
    print(desenhos[-1])  # Mostrar o desenho final (quando o jogador perde)
    print("Tente novamente!")  # Mensagem de incentivo

# Escolher uma palavra aleatória e iniciar o jogo
palavra_escolhida = random.choice(palavras_forca).lower()  # Seleciona uma palavra aleatória
jogo(palavra_escolhida)  # Inicia o jogo com a palavra escolhida
