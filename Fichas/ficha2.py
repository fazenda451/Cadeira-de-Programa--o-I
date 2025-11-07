
################################################
############### EX 1 ##########################
###############################################


Compras = int(input('Quanto foi o valor Total das compras? '))
Desconto = Compras* 0.1


if Compras >= 100:
    compras_com_Desconto = Compras - Desconto
    print(f"O Valor final foi de: {compras_com_Desconto}")
else: 
    print('Sem Desconto')


################################################
############### EX 2 ##########################
###############################################


Idd = int(input('Que idade o jogador tem? '))

if Idd < 18:
    print("O jogador joga na categoria Juvenil")
else: 
    print('O jogador joga no Sub18')


################################################
############### EX 3 ##########################
###############################################


N = int(input('Qual o numero? '))

if N%5 == 0:
    print("O numero é multiplo de 5")
else: 
    print('O numero não é multiplo de 5')


################################################
############### EX 4 ##########################
###############################################

Velocidade = int(input('Qual a velocidade do Carro? '))

if Velocidade > 120:
    print("Excesso de velocidade")
elif Velocidade == 20: 
    print('No limite Máximo')
else:
    print("A velocidade é:", Velocidade)
