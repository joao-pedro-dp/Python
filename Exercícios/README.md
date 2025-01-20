# Exercícios de Python - Básico ao Avançado
Este repositório contém uma série de exercícios de programação em Python que foram criados com o objetivo de treinamento pessoal. Eles cobrem uma gama de níveis de dificuldade, desde o básico até o avançado, e foram desenvolvidos para aprimorar minhas habilidades de programação e compreensão de conceitos fundamentais da linguagem Python.

# Sobre os Códigos
Autorais: Todos os códigos são de minha autoria e foram feitos de forma independente. O objetivo principal é a prática e o aprendizado contínuo.
Os exercícios não seguem exatamente os padrões ou objetivos de problemas típicos encontrados em plataformas de desafios, mas sim focam em aprender e explorar a linguagem de maneira pessoal e prática. Além disso, a documentação dos códigos também é parte desse processo de treinamento, garantindo que eu compreenda a importância de documentar adequadamente minhas soluções e ajude no aprimoramento das minhas habilidades de escrita técnica.

# Exemplo de Exercício - Conversão de Temperatura
Aqui está um exemplo de um exercício simples que converte uma temperatura de Celsius para Fahrenheit. Note que, como parte do meu aprendizado, eu busquei explorar e lidar com entradas inválidas e apresentar resultados de forma clara.

    def cel_para_fah():
        """
        Função que converte uma temperatura fornecida em Celsius para Fahrenheit.
        Lida com entradas inválidas e solicita novamente até receber um número válido.
        
        Retorna:
        tuple: Temperatura em Fahrenheit (precisa e arredondada).
        """
        while True:
            try:
                # Solicita a temperatura em Celsius
                cel = float(input("Informe a temperatura em Celsius: "))
    
            except ValueError: 
                # Trata entradas inválidas
                print("Entrada inválida, favor digitar um número")
    
            # Converte para Fahrenheit
            f = (((9/5) * cel) + 32)
            f_arredondado = round(f, 2)  # Arredonda o valor para 2 casas decimais
    
            # Exibe os resultados
            print("A temperatura em graus Fahrenheit será:", f)
            print("A temperatura em graus Fahrenheit arredondado será:", f_arredondado)
            
            return f, f_arredondado
    
    # Chamada da função
    cel_para_fah()

# Estrutura
Exercícios Básicos: Abarcam conceitos como variáveis, tipos de dados, condicionais, laços de repetição e funções simples.
Exercícios Intermediários: Envolvem manipulação de listas, dicionários, funções mais complexas, e integração entre módulos.
Exercícios Avançados: Englobam conceitos como manipulação de arquivos, orientações a objetos, e algoritmos mais sofisticados.

# Como Usar
Sinta-se à vontade para explorar os códigos.
Execute e modifique conforme necessário.

