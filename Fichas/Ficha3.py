N = int(input('Qual o numero? '))

if N%2 == 0:
    print("É par")
else: 
    print('É Impar')


################################################
############### EX 2 ##########################
###############################################

n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))

if n2 == 0:
    print("Não é possivel dividir por zero")
else:
    if n1%n2 == 0:
        print("O primeiro numero é Divisivel pelo segundo numero")
    else: 
        print('O  primeiro numero não é Divisivel pelo segundo numero')


################################################
############### EX 3 ##########################
###############################################

n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))

if n2 == 0:
    print("ERRO:O divisor é 0.")
else:
    resto = n1%n2
    quociente = n1/n2
    print("O Resto é:", resto , "e o quociente é:", quociente)

# Exercicio 4 - PARA CASA: Ler quantos números a,b,c,d
# Verificar se as razões a/b e c/d são iguais.
# Exemplo: 2/4 e 3/6 --> são equivalentes

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))

if b == 0 or d == 0:
    print("Erro: Não é possível dividir por zero")
else:
    # Verificar se a/b == c/d usando equivalência: a*d == b*c
    if a * d == b * c:
        print("As razões são equivalentes")
    else:
        print("As razões não são equivalentes")