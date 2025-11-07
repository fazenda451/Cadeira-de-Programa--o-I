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