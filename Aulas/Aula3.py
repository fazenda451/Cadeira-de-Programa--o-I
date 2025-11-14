#Exercicio 1
#O piloto de Formula 1 Lando Norris lidera o campeonato com 390  pontos. O segundo colocado, Max Verstappen, tem 341 pontos.
#Sabendo que o lider nao podera mais correr e que o vencedor de cada prova some 12 pontos,construa um programa em Python utilizando
#um ciclo while para calcular quantas provas Max verstappen precisa de vencer para ultrapassar Lando Norris e se tornar o novo lider do campeonato.

#pontos_lando = 390
#pontos_verstappen = 341
#provas_restantes = 0

#while pontos_verstappen < pontos_lando:
#    pontos_verstappen += 12
#    provas_restantes += 1

#print(f"Max Verstappen precisa de vencer {provas_restantes} provas para ultrapassar Lando Norris e se tornar o novo lider do campeonato.")

#exercicio 2
#Escreva um programa que leia vários números positivos introduzidos pelo utilizador e calcule a média deles.
#O programa deve terminar quando o utilizador digitar um número negativo

#soma = 0
#contador = 0
#numero = float(input("Digite um numero positivo: "))

#while numero >= 0:
#    if numero >= 0:
#        soma += numero
#    contador += 1

#if contador > 0:
#    print(f"A média dos números é: {soma / contador}")
#else:
#    print("Nenhum número positivo foi introduzido.")

#exercicio 3
#Construa um programa que peça um número inteiro positivo e faça uma contagem regressiva até O, mostrando todos os números no ecrã~

#numero = int(input("Digite um numero inteiro positivo: "))
#while numero >= 0:
#    print(numero)
#    numero -= 1
#print("Fim da contagem")

#exercicio 4
#Faça um algoritmo que leia números inteiros e some-os ate que a soma ultrapasse 100. No final, mostre o total somado e quantos números foram lidos.

#soma = 0
#contador = 0

#while soma <= 100:
#    numero = int(input("Digite um numero inteiro: "))
#    soma += numero
#    contador += 1

#print(f"O total somado é: {soma}")
#print(f"Foram lidos {contador} números.")


#exercicio 5
#Escreva um programa que leia vários números positivos introduzidos pelo utilizador e calcule a média deles.
#O programa deve terminar quando o utilizador digitar um número negativo, com while true

#while True:
#    numero = float(input("Digite um numero positivo: "))
#    if numero < 0:
#        break
#    soma += numero
#    contador += 1

#if contador != 0:
#    print(f"A média dos números é: {soma / contador}")
#else:
#    print("Nenhum número positivo foi introduzido.")


#
# exercicio 6

#import time

#print("Contagem regressiva para o lançamento do foguete:")

#for i in range(5, 0, -1):
#    print("Motor Ligado",)

#    time.sleep(1)

#print("Lançamento!")

#exercicio 7

#n = 0
#total = 0

#while n <= 10:
#    n+=1
#    total += n
#print(total)

#Crie um programa em py que mostre apenas os numeros pares entre 2 e 20 (inclusive)

for i in range(2, 21, 2):
    print(i)

#Peça um numero ao utilizador e mostre uma cpntagem regressiva até 0, com um for descrescente
#nota:assegure que funcione sempre

numero = int(input("Digite um numero: "))
for i in range(numero, -1, -1):
    print(i)


#Faça um programa que peça um numero inteiro e mostre a sua tabuada de 1 a 10 usando um for.
numero = int(input("Digite um numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")