"""
===========================================
FORMULÁRIO DE REVISÃO - PROGRAMAÇÃO I
Teste de Amanhã - Todos os Tópicos
===========================================
"""

# Importar módulos necessários
import math  # Para operações matemáticas (sqrt, pi, etc.)
import random  # Para gerar números aleatórios

# ===========================================
# PARTE 1: VARIÁVEIS E OPERAÇÕES BÁSICAS
# ===========================================

def exercicio_1_variaveis():
    """
    Exercício 1: Variáveis e Input/Output
    Cria um programa que pede o nome, idade e cidade do utilizador
    e mostra uma mensagem personalizada.
    """
    print("\n=== EXERCÍCIO 1: Variáveis ===")
    
    # Pedir dados ao utilizador usando input()
    # input() sempre devolve uma string (texto)
    nome = input("Qual o teu nome? ")
    idade = input("Qual a tua idade? ")
    cidade = input("De que cidade és? ")
    
    # Usar f-string para formatar a mensagem
    # f"texto {variavel}" permite inserir variáveis no texto
    print(f"Olá {nome}! Tens {idade} anos e és de {cidade}.")


# ===========================================
# PARTE 2: ESTRUTURAS CONDICIONAIS
# ===========================================

def exercicio_2_condicionais_simples():
    """
    Exercício 2: If/Else Básico
    Verifica se um número é par ou ímpar.
    """
    print("\n=== EXERCÍCIO 2: Condicionais Simples ===")
    
    # int() converte a string do input para número inteiro
    numero = int(input("Introduza um número: "))
    
    # % é o operador módulo (resto da divisão)
    # numero % 2 == 0 significa "o resto da divisão por 2 é zero" (número par)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:  # Se não for par, então é ímpar
        print(f"O número {numero} é ímpar.")


def exercicio_3_condicionais_multiplas():
    """
    Exercício 3: If/Elif/Else
    Classifica a nota de um aluno.
    """
    print("\n=== EXERCÍCIO 3: Condicionais Múltiplas ===")
    
    # float() converte para número decimal (com vírgula)
    nota = float(input("Introduza a nota (0-20): "))
    
    # Estrutura if/elif/else permite múltiplas condições
    # As condições são verificadas de cima para baixo
    # Quando uma condição é verdadeira, executa o código e sai
    if nota < 10:  # Se nota for menor que 10
        print("Reprovado")
    elif nota <= 14:  # Senão, se nota for menor ou igual a 14
        print("Suficiente")
    elif nota <= 17:  # Senão, se nota for menor ou igual a 17
        print("Bom")
    else:  # Senão (nota >= 18)
        print("Excelente")


def exercicio_4_operadores_logicos():
    """
    Exercício 4: Operadores Lógicos (and, or)
    Verifica se um triângulo é válido e classifica-o.
    """
    print("\n=== EXERCÍCIO 4: Operadores Lógicos ===")
    
    # Ler os três lados do triângulo
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    
    # Verificar se forma triângulo: cada lado deve ser menor que a soma dos outros dois
    # 'and' significa "E" - todas as condições devem ser verdadeiras
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print("Os valores formam um triângulo")
        
        # Classificar o tipo de triângulo
        # == verifica se os valores são iguais
        if lado1 == lado2 == lado3:  # Todos os lados iguais
            print("O triângulo é equilátero")
        # 'or' significa "OU" - pelo menos uma condição deve ser verdadeira
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:  # Dois lados iguais
            print("O triângulo é isósceles")
        else:  # Todos os lados diferentes
            print("O triângulo é escaleno")
    else:
        print("Os valores não formam um triângulo")


# ===========================================
# PARTE 3: CICLOS (LOOPS)
# ===========================================

def exercicio_5_ciclo_for():
    """
    Exercício 5: Ciclo For
    Mostra todos os números pares entre 1 e 20.
    """
    print("\n=== EXERCÍCIO 5: Ciclo For ===")
    print("Números pares entre 1 e 20:")
    
    # range(1, 21) cria uma sequência de 1 até 20 (21 não incluído)
    # for repete o código para cada valor na sequência
    for i in range(1, 21):
        # Verificar se o número é par
        if i % 2 == 0:
            # end=" " faz com que não mude de linha, apenas adicione um espaço
            print(i, end=" ")
    
    # print() sem argumentos apenas muda de linha
    print()


def exercicio_6_ciclo_while():
    """
    Exercício 6: Ciclo While
    Lê números até ser introduzido um valor negativo.
    """
    print("\n=== EXERCÍCIO 6: Ciclo While ===")
    
    # Inicializar variáveis para acumular valores
    soma = 0  # Guarda a soma de todos os números
    contador = 0  # Conta quantos números foram introduzidos
    
    # while True cria um ciclo infinito
    # break dentro do ciclo permite sair quando necessário
    while True:
        numero = int(input("Introduza um número (negativo para terminar): "))
        
        # Se o número for negativo, sair do ciclo
        if numero < 0:
            break  # break interrompe o ciclo e continua após o while
        
        # Acumular o número na soma
        soma += numero  # Equivale a: soma = soma + numero
        contador += 1  # Incrementar o contador
    
    # Verificar se foram introduzidos números
    if contador > 0:
        # Calcular a média
        media = soma / contador
        print(f"Foram introduzidos {contador} números.")
        print(f"Soma: {soma}")
        # :.2f formata o número com 2 casas decimais
        print(f"Média: {media:.2f}")
    else:
        print("Nenhum número foi introduzido.")


# ===========================================
# PARTE 4: FUNÇÕES
# ===========================================

def exercicio_7_funcao_sem_parametros():
    """
    Exercício 7: Função sem Parâmetros
    Função que calcula e mostra a área de um círculo.
    """
    print("\n=== EXERCÍCIO 7: Função sem Parâmetros ===")
    
    # Definir uma função (def) sem parâmetros
    # Funções agrupam código que pode ser reutilizado
    def calcular_area_circulo():
        # Pedir o raio ao utilizador
        raio = float(input("Introduza o raio do círculo: "))
        
        # Calcular a área: π * r²
        # math.pi é o valor de π (pi)
        # ** é o operador de potência (raio ** 2 = raio²)
        area = math.pi * raio ** 2
        
        # Mostrar o resultado
        print(f"A área do círculo é {area:.2f}")
    
    # Chamar a função (executar o código dentro dela)
    calcular_area_circulo()


def exercicio_8_funcao_com_parametros():
    """
    Exercício 8: Função com Parâmetros
    Função que recebe dois números e devolve o maior.
    """
    print("\n=== EXERCÍCIO 8: Função com Parâmetros ===")
    
    # Definir função com parâmetros (a e b)
    # Parâmetros são valores que a função recebe quando é chamada
    def maior_numero(a, b):
        # Comparar os dois números
        if a > b:
            # return devolve um valor e termina a função
            return a
        else:
            return b
    
    # Ler dois números do utilizador
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    
    # Chamar a função passando os valores como argumentos
    # O valor devolvido (return) é guardado em resultado
    resultado = maior_numero(num1, num2)
    print(f"O maior número é {resultado}")


def exercicio_9_funcao_com_return():
    """
    Exercício 9: Função com Return
    Função que calcula a distância entre dois pontos.
    """
    print("\n=== EXERCÍCIO 9: Função com Return ===")
    
    # Função com 4 parâmetros que devolve um valor
    def distancia_pontos(x1, y1, x2, y2):
        # Fórmula da distância: √[(x2-x1)² + (y2-y1)²]
        # math.sqrt() calcula a raiz quadrada
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Ler as coordenadas dos dois pontos
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    # Chamar a função e guardar o resultado
    dist = distancia_pontos(x1, y1, x2, y2)
    print(f"Distância entre os pontos: {dist:.2f}")


# ===========================================
# PARTE 5: STRINGS E MÉTODOS
# ===========================================

def exercicio_10_metodos_string():
    """
    Exercício 10: Métodos de String
    Converte uma palavra e analisa o seu comprimento.
    """
    print("\n=== EXERCÍCIO 10: Métodos de String ===")
    
    # .lower() converte a string para minúsculas
    # Pode ser usado diretamente após input()
    palavra = input("Introduza uma palavra: ").lower()
    
    # len() devolve o número de caracteres na string
    comprimento = len(palavra)
    
    print(f"Palavra em minúsculas: {palavra}")
    # .upper() converte para maiúsculas
    print(f"Palavra em maiúsculas: {palavra.upper()}")
    print(f"Comprimento: {comprimento} caracteres")
    
    # Classificar a palavra pelo comprimento
    if comprimento < 4:
        print("Palavra curta")
    elif comprimento <= 7:
        print("Palavra média")
    else:
        print("Palavra longa")


# ===========================================
# PARTE 6: RANDOM E DICIONÁRIOS
# ===========================================

def exercicio_11_random():
    """
    Exercício 11: Módulo Random
    Simula lançamentos de um dado.
    """
    print("\n=== EXERCÍCIO 11: Módulo Random ===")
    
    # Pedir quantos lançamentos fazer
    n_lancamentos = int(input("Quantos lançamentos? "))
    
    # Criar um dicionário para guardar os resultados
    # Chave: número da face (1-6), Valor: quantidade de vezes que saiu
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    # _ significa que não usamos a variável do ciclo
    for _ in range(n_lancamentos):
        # random.randint(1, 6) gera um número aleatório entre 1 e 6 (inclusive)
        resultado = random.randint(1, 6)
        
        # Incrementar o contador dessa face
        resultados[resultado] += 1
    
    # Mostrar os resultados
    print("\nResultados:")
    # .items() devolve pares (chave, valor) do dicionário
    for face, quantidade in resultados.items():
        print(f"Face {face}: {quantidade} vezes")


def exercicio_12_dicionarios():
    """
    Exercício 12: Dicionários
    Sistema simples de notas de alunos.
    """
    print("\n=== EXERCÍCIO 12: Dicionários ===")
    
    # Criar um dicionário vazio
    # Dicionários guardam pares chave:valor
    alunos = {}
    
    # Pedir dados de 3 alunos
    for i in range(3):
        nome = input(f"Nome do aluno {i+1}: ")
        nota = float(input(f"Nota do aluno {i+1}: "))
        
        # Adicionar ao dicionário: alunos[nome] = nota
        # A chave é o nome, o valor é a nota
        alunos[nome] = nota
    
    # Mostrar todas as notas
    print("\nNotas dos alunos:")
    # Percorrer o dicionário e mostrar cada par
    for nome, nota in alunos.items():
        print(f"{nome}: {nota}")


# ===========================================
# PARTE 7: TRATAMENTO DE ERROS
# ===========================================

def exercicio_13_try_except():
    """
    Exercício 13: Try/Except
    Lê um número inteiro com validação.
    """
    print("\n=== EXERCÍCIO 13: Try/Except ===")
    
    # Função que valida a entrada do utilizador
    def ler_inteiro(mensagem):
        # Ciclo infinito até receber um valor válido
        while True:
            try:
                # Tentar converter o input para inteiro
                # Se funcionar, devolve o valor e sai do ciclo
                return int(input(mensagem))
            except ValueError:
                # Se der erro (ex: utilizador escreveu texto), captura o erro
                # ValueError ocorre quando int() não consegue converter
                print("Valor inválido. Introduza um número inteiro.")
                # O ciclo continua e pede novamente
    
    # Usar a função para ler um número válido
    numero = ler_inteiro("Introduza um número inteiro: ")
    print(f"O número introduzido foi: {numero}")


# ===========================================
# PARTE 8: EXERCÍCIOS COMPOSTOS
# ===========================================

def exercicio_14_composto():
    """
    Exercício 14: Exercício Composto
    Calcula estatísticas de valores introduzidos.
    """
    print("\n=== EXERCÍCIO 14: Exercício Composto ===")
    
    # Criar uma lista vazia para guardar os valores
    valores = []
    
    # Ciclo para ler valores até o utilizador pressionar Enter (string vazia)
    while True:
        valor = input("Introduza um número (Enter para terminar): ")
        
        # Se a string estiver vazia, sair do ciclo
        if valor == "":
            break
        
        # Tentar converter para número
        try:
            # .append() adiciona um elemento à lista
            valores.append(float(valor))
        except ValueError:
            # Se der erro, mostrar mensagem mas continuar o ciclo
            print("Valor inválido. Tente novamente.")
    
    # Verificar se foram introduzidos valores
    if valores:  # Se a lista não estiver vazia
        print(f"\nEstatísticas:")
        # len() devolve o número de elementos na lista
        print(f"Quantidade de valores: {len(valores)}")
        # sum() soma todos os elementos da lista
        print(f"Soma: {sum(valores)}")
        print(f"Média: {sum(valores)/len(valores):.2f}")
        # max() e min() devolvem o maior e menor valor
        print(f"Máximo: {max(valores)}")
        print(f"Mínimo: {min(valores)}")
    else:
        print("Nenhum valor foi introduzido.")


def exercicio_15_menu():
    """
    Exercício 15: Menu Interativo
    Menu com várias opções de exercícios.
    """
    print("\n=== EXERCÍCIO 15: Menu Interativo ===")
    
    def menu():
        # Ciclo do menu - continua até o utilizador escolher sair
        while True:
            print("\n--- MENU DE EXERCÍCIOS ---")
            print("1 - Calcular área de retângulo")
            print("2 - Verificar se número é primo")
            print("3 - Calcular fatorial")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            # Opção 1: Calcular área
            if opcao == "1":
                largura = float(input("Largura: "))
                altura = float(input("Altura: "))
                area = largura * altura
                print(f"Área: {area}")
            
            # Opção 2: Verificar número primo
            elif opcao == "2":
                num = int(input("Número: "))
                primo = True  # Assumir que é primo
                
                # Números menores que 2 não são primos
                if num < 2:
                    primo = False
                else:
                    # Verificar divisores de 2 até √num
                    # num**0.5 calcula a raiz quadrada
                    for i in range(2, int(num**0.5) + 1):
                        # Se encontrar um divisor, não é primo
                        if num % i == 0:
                            primo = False
                            break  # Sair do ciclo quando encontrar divisor
                
                # Operador ternário: valor_se_verdadeiro if condição else valor_se_falso
                print(f"{num} é primo" if primo else f"{num} não é primo")
            
            # Opção 3: Calcular fatorial
            elif opcao == "3":
                num = int(input("Número: "))
                fatorial = 1  # Inicializar com 1
                
                # Fatorial: n! = 1 * 2 * 3 * ... * n
                for i in range(1, num + 1):
                    fatorial *= i  # Multiplicar por cada número
                
                print(f"Fatorial de {num}: {fatorial}")
            
            # Opção 0: Sair
            elif opcao == "0":
                print("A sair...")
                break  # Sair do ciclo while
            
            # Opção inválida
            else:
                print("Opção inválida!")
    
    # Chamar a função do menu
    menu()


# ===========================================
# MENU PRINCIPAL
# ===========================================

def menu_principal():
    """
    Menu principal com todos os exercícios de revisão.
    """
    # Dicionário que mapeia opções para (descrição, função)
    # As funções são guardadas sem parênteses (sem executar)
    exercicios = {
        "1": ("Variáveis e Input/Output", exercicio_1_variaveis),
        "2": ("Condicionais Simples (if/else)", exercicio_2_condicionais_simples),
        "3": ("Condicionais Múltiplas (if/elif/else)", exercicio_3_condicionais_multiplas),
        "4": ("Operadores Lógicos (and/or)", exercicio_4_operadores_logicos),
        "5": ("Ciclo For", exercicio_5_ciclo_for),
        "6": ("Ciclo While", exercicio_6_ciclo_while),
        "7": ("Função sem Parâmetros", exercicio_7_funcao_sem_parametros),
        "8": ("Função com Parâmetros", exercicio_8_funcao_com_parametros),
        "9": ("Função com Return", exercicio_9_funcao_com_return),
        "10": ("Métodos de String", exercicio_10_metodos_string),
        "11": ("Módulo Random", exercicio_11_random),
        "12": ("Dicionários", exercicio_12_dicionarios),
        "13": ("Try/Except", exercicio_13_try_except),
        "14": ("Exercício Composto", exercicio_14_composto),
        "15": ("Menu Interativo", exercicio_15_menu),
    }
    
    # Ciclo principal do menu
    while True:
        # Mostrar cabeçalho
        print("\n" + "="*50)  # "="*50 cria uma string com 50 sinais de igual
        print("FORMULÁRIO DE REVISÃO - PROGRAMAÇÃO I")
        print("="*50)
        print("\nEscolha um exercício para praticar:")
        print()
        
        # Mostrar todas as opções disponíveis
        # .items() devolve (chave, valor) do dicionário
        # _ ignora o segundo elemento da tupla (a função)
        for num, (descricao, _) in exercicios.items():
            # :>2 alinha o número à direita com 2 espaços
            print(f"{num:>2}. {descricao}")
        print(" 0. Sair")
        
        # Pedir escolha ao utilizador
        # .strip() remove espaços no início e fim
        escolha = input("\nOpção: ").strip()
        
        # Verificar a escolha
        if escolha == "0":
            print("\nBoa sorte no teste amanhã! 🍀")
            break  # Sair do ciclo
        elif escolha in exercicios:
            # Verificar se a opção existe no dicionário
            try:
                # exercicios[escolha][1] acede à função (segundo elemento da tupla)
                # () no final executa a função
                exercicios[escolha][1]()
            except Exception as e:
                # Se ocorrer algum erro, mostrar mensagem
                print(f"\nErro ao executar exercício: {e}")
        else:
            print("\nOpção inválida! Tente novamente.")


# ===========================================
# EXECUÇÃO
# ===========================================

# __name__ == "__main__" verifica se o ficheiro está a ser executado diretamente
# (não importado como módulo)
# Isto permite que o código só execute quando correres o ficheiro
if __name__ == "__main__":
    # Iniciar o menu principal
    menu_principal()
