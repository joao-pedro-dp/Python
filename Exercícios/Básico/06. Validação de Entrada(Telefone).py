#6. Faça um programa que leia um número de telefone, e corrija o número no caso deste faltar dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

import re

def validar_telefone(telefone):
    """
    Função que valida um número de telefone no formato brasileiro.
    O formato válido é (XX) XXXXX-XXXX, onde X representa dígitos.

    Retorno:
    - bool: Retorna True se o telefone estiver no formato correto, caso contrário retorna False.
    """
    # Expressão regular para validar o formato do telefone (XX) XXXXX-XXXX
    padrao = r'^\(\d{2}\) \d{5}-\d{4}$'
    
    # Verifica se o telefone corresponde ao padrão
    return bool(re.match(padrao, telefone))

def corrige_telefone(telefone):
    """
    Função que corrige um número de telefone adicionando dígitos extras caso o número
    não tenha o comprimento correto de 11 dígitos (DDD + número).

    Retorno:
    - telefone_corrigido (str): O número de telefone formatado corretamente no padrão (XX) XXXXX-XXXX.
    """
    while True:
        # Remove todos os caracteres que não são dígitos
        numeros = re.sub(r'\D', '', telefone)
        
        # Verifica se o telefone tem 11 dígitos
        if len(numeros) == 11:
            # Formata o telefone para o padrão (XX) XXXXX-XXXX
            telefone_corrigido = f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
            return telefone_corrigido
        else:
            # Adiciona '3' ao final do telefone caso o número tenha menos de 11 dígitos
            telefone += "3"

# Loop para solicitar ao usuário um telefone válido
while True:
    telefone = input("Digite seu telefone ((XX) XXXXX-XXXX): ")

    # Valida o telefone usando a função validar_telefone
    if validar_telefone(telefone):
        break
    else:
        # Se o telefone for inválido, tenta corrigir o formato e exibe a versão corrigida
        print(f"O telefone possui somente {len(telefone)} números, vou adicionar o valor (3) até validar.")
        telefone_corrigido = corrige_telefone(telefone)
        print(telefone_corrigido)
        break
