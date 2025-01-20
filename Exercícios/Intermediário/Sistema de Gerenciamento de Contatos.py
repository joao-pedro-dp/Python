"""
Este código implementa um sistema de gerenciamento de contatos que permite adicionar, remover, modificar, buscar e exibir contatos, 
além de realizar backup e exportação em formato CSV.

Validação e correção de números de telefone: Garante que os números sigam um formato padrão e, se necessário, corrige números incorretos.
Validação de nomes: Assegura que os nomes contenham apenas letras e espaços.
Operações com contatos: Permite ao usuário adicionar, remover, modificar e buscar contatos, com persistência de dados em arquivos JSON.
Registro de logs: Toda ação (adicionar, deletar, alterar) é registrada em um arquivo de log para manter o histórico de alterações.
Backup e exportação de contatos: Os contatos podem ser salvos em arquivos de backup ou exportados para CSV.

Futuramente posso fazer um aplicativo pra esse sistema.
"""

import re
import json
import os
import time

# Função que valida se o número de telefone segue o formato (XX) XXXXX-XXXX
def validar_telefone(numero):
    padrao = r'^\(\d{2}\) \d{5}-\d{4}$'  # Padrão de regex para validar o telefone
    return bool(re.match(padrao, numero))  # Retorna True se o número bater com o padrão

# Função que valida se o nome contém apenas letras e espaços
def validar_nome(nome):
    return bool(re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", nome))  # Valida apenas letras e espaços

# Função que corrige um número de telefone, removendo caracteres não numéricos e completando com "3" até ter 11 caracteres
def corrige_telefone(numero):
    numeros = re.sub(r'\D', '', numero)  # Remove caracteres não numéricos
    while len(numeros) < 11:  # Completa com "3" se o número tiver menos de 11 caracteres
        numeros += "3"
    telefone_corrigido = f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"  # Formata o número corrigido
    return telefone_corrigido

# Função para adicionar um contato ao calendário, com validação e correção de telefone
def adicionar(calendario_contatos):
    while True:
        nome = input("Adicione um Nome: ").strip()  # Solicita nome
        numero = input("Adicione um Telefone ((XX) XXXXX-XXXX): ").strip()  # Solicita telefone

        # Valida nome
        if not validar_nome(nome):
            print("Nome inválido! Use apenas letras e espaços.")
            continue

        # Verifica se o número já existe
        if numero not in calendario_contatos.values():
            if validar_telefone(numero):  # Se o número for válido
                calendario_contatos[nome] = numero
                registrar_log("Adicionado", f"{nome} ({numero})")  # Registra a ação no log
                print(f"Contato {nome} adicionado com sucesso!")
                break
            else:
                print("O telefone é inválido, corrigindo...")
                telefone_corrigido = corrige_telefone(numero)  # Corrige o telefone
                print(f"Telefone corrigido para: {telefone_corrigido}")
                calendario_contatos[nome] = telefone_corrigido
                registrar_log("Adicionado", f"{nome} ({telefone_corrigido})")  # Registra a ação no log
                print(f"Contato {nome} adicionado com sucesso!")
                break
        else:
            print("Esse telefone já existe na lista. Use outro número.")
            break

# Função para remover um contato do calendário, por nome ou número
def deletar(calendario_contatos):
    while True:
        try:
            user = int(input("Digite 1 para remover por nome ou 2 para remover pelo número: "))

            if user == 1:
                nome = input("Digite o nome a ser removido: ").strip()
                if nome in calendario_contatos:
                    numero = calendario_contatos.pop(nome)  # Remove o contato
                    registrar_log("Deletado", f"{nome} ({numero})")  # Registra a ação no log
                    print(f"Contato {nome} removido com sucesso!")
                    break
                else:
                    print("Contato não encontrado.")
            elif user == 2:
                numero = input("Digite o número a ser removido: ").strip()
                if numero in calendario_contatos.values():
                    nome_remover = [nome for nome, telefone in calendario_contatos.items() if telefone == numero][0]  # Busca o nome associado ao número
                    calendario_contatos.pop(nome_remover)  # Remove o contato
                    registrar_log("Deletado", f"{nome_remover} ({numero})")  # Registra a ação no log
                    print(f"Contato com número {numero} removido com sucesso!")
                    break
                else:
                    print("Número não encontrado.")
            else:
                print("Favor inserir SOMENTE 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

# Função para modificar um contato, permitindo alterar nome ou telefone
def modificar_contato(calendario_contatos):
    nome = input("Digite o nome do contato que deseja modificar: ").strip()
    if nome in calendario_contatos:
        print(f"1. Alterar nome ({nome})")
        print(f"2. Alterar telefone ({calendario_contatos[nome]})")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            novo_nome = input("Digite o novo nome: ").strip()
            if validar_nome(novo_nome):  # Valida o novo nome
                numero = calendario_contatos.pop(nome)  # Remove o contato antigo
                calendario_contatos[novo_nome] = numero  # Adiciona o contato com o novo nome
                print(f"Nome alterado de {nome} para {novo_nome}.")
                registrar_log("Alterado", f"Nome de {nome} para {novo_nome}")  # Registra a ação no log
            else:
                print("Nome inválido!")
        elif opcao == "2":
            novo_telefone = input("Digite o novo telefone ((XX) XXXXX-XXXX): ").strip()
            if validar_telefone(novo_telefone):  # Valida o novo telefone
                antigo_telefone = calendario_contatos[nome]
                calendario_contatos[nome] = novo_telefone  # Atualiza o telefone
                print(f"Telefone de {nome} atualizado de {antigo_telefone} para {novo_telefone}.")
                registrar_log("Alterado", f"Telefone de {nome} de {antigo_telefone} para {novo_telefone}")  # Registra a ação no log
            else:
                print("Telefone inválido!")
        else:
            print("Opção inválida!")
    else:
        print("Contato não encontrado.")

# Função para buscar um contato pelo nome ou número
def buscar(calendario_contatos):
    entrada = input("Digite o nome ou número que deseja buscar: ").strip()

    if entrada in calendario_contatos:  # Verifica se a entrada é um nome
        print(f"O telefone de {entrada} é {calendario_contatos[entrada]}")
    elif entrada in calendario_contatos.values():  # Verifica se a entrada é um número
        nome = [nome for nome, telefone in calendario_contatos.items() if telefone == entrada][0]
        print(f"O número {entrada} pertence a {nome}.")
    else:
        print("Contato não existente na lista.")

# Função para exibir todos os contatos cadastrados
def todos(calendario_contatos):
    if calendario_contatos:
        print("Os contatos cadastrados são:")
        for nome, numero in sorted(calendario_contatos.items()):  # Exibe contatos ordenados pelo nome
            print(f"O telefone de {nome} é {numero}")
    else:
        print("Nenhum contato existente na lista.")

# Função para carregar os contatos do arquivo JSON
def carregar_contatos():
    if os.path.exists("contatos.json"):  # Verifica se o arquivo existe
        with open("contatos.json", "r") as file:
            return json.load(file)  
    return {}

# Função para salvar os contatos no arquivo JSON
def salvar_contatos(calendario_contatos):
    with open("contatos.json", "w") as file:
        json.dump(calendario_contatos, file)  # Salva os contatos no arquivo JSON

# Função para registrar logs de ações (adicionar, deletar, alterar)
def registrar_log(acao, contato):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{acao}: {contato} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")  # Registra a ação com a data e hora

# Função para criar um backup dos contatos no arquivo JSON
def backup_contatos(calendario_contatos):
    with open("contatos_backup.json", "w") as backup_file:
        json.dump(calendario_contatos, backup_file)  # Cria o backup no arquivo
    print("Backup criado com sucesso!")

# Função para exportar os contatos para um arquivo CSV
def exportar_csv(calendario_contatos):
    with open("contatos_exportados.csv", "w") as file:
        file.write("Nome,Telefone\n")  # Escreve o cabeçalho
        for nome, telefone in calendario_contatos.items():
            file.write(f"{nome},{telefone}\n")  # Escreve cada contato
    print("Contatos exportados para 'contatos_exportados.csv'.")

# Função principal que exibe o menu e chama as funções conforme a escolha do usuário
def menu():
    calendario_contatos = carregar_contatos()  

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Exibir todos os contatos")
        print("5. Alterar contato")
        print("6. Sair e salvar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar(calendario_contatos)
        elif opcao == "2":
            deletar(calendario_contatos)
        elif opcao == "3":
            buscar(calendario_contatos)
        elif opcao == "4":
            todos(calendario_contatos)
        elif opcao == "5":
            modificar_contato(calendario_contatos)
        elif opcao == "6":
            backup_contatos(calendario_contatos)
            exportar_csv(calendario_contatos)
            salvar_contatos(calendario_contatos) 
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
