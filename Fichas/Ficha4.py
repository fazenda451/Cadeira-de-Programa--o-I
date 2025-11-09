#1) Faça um programa em Python para calcular a luminosidade de um quarto. O utilizador deve informar a
#intensidade da luz (de 0 a 1000). Se a intensidade for menor que 200, o programa deve indicar que o
#ambiente está escuro. Se estiver entre 200 e 700, deve indicar luminosidade moderada. Se for maior que
#700, deve indicar ambiente muito iluminado.

luz = int(input("Informe a intensidade da luz (0 a 1000): "))

if luz < 200:
    print("O quarto está escuro")
elif luz >= 200 and luz < 700:
    print("luminosidade moderada")
else:
    print("ambiente muito iluminado")


#2) Escreva um programa que pergunte ao utilizador se deseja converter uma temperatura para Celsius ou
#Fahrenheit. A resposta deve ser lida e convertida com .upper().
#Se for “C”, o programa deve ler um valor em Fahrenheit e converter para Celsius.
#Se for “F”, deve ler um valor em Celsius e converter para Fahrenheit.
#O resultado deve ser mostrado com uma casa decimal.

convert = input("Converter para C ou F: ").upper()
if convert == 'C':
    fah = float(input("Temperatura em Fahrenheit: "))
    celsius = (fah - 32) * 5 / 9
    print(f"Temperatura em Celsius: {celsius:.1f}°C")
elif convert == 'F':
    cel = float(input("Temperatura em Celsius: "))
    fahrenheit = (cel * 9 / 5) + 32
    print(f"Temperatura em Fahrenheit: {fahrenheit:.1f}°F")
else:
    print("Opção inválida. Escolha 'C' ou 'F'.")

#3) Crie um programa que leia três valores correspondentes aos lados de um triângulo. 
#O programa deve verificar se os valores formam um triângulo. 
#Se qualquer lado for maior ou igual à soma dos outros dois, a figura não é um triângulo. 
#Caso contrário, o programa deve identificar se o triângulo é equilátero (3 lados iguais), 
#isósceles (2 lados  iguais) ou escaleno (todos os lados diferentes). 

Lado1 = float(input("Lado 1: "))
Lado2 = float(input("Lado 2: "))
Lado3 = float(input("Lado 3: "))

if Lado1 + Lado2 > Lado3 and Lado1 + Lado3 > Lado2 and Lado2 + Lado3 > Lado1:
    print("Os valores formam um triângulo")

    if Lado1 == Lado2 == Lado3:
        print("O triângulo é equilátero")
    elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Os valores não formam um triângulo")


#4) Elabore um programa para classificar a velocidade do vento informada pelo utilizador (em km/h). Se for menor que 1, deve escrever “Calmo”. 
#Se estiver entre 1 e 19, deve escrever “Brisa leve”. 
#Se estiver entre 20 e 49, deve escrever “Vento moderado”. 
#Se for igual ou superior a 50, deve escrever “Vento forte”. 
#OBS.: Se o valor do vento for negativo, informar que não há vento negativo 

velocidade = float(input("Velocidade do vento (km/h): "))

if velocidade < 0:
    print("Não há vento negativo")
elif velocidade < 1:
    print("Calmo")
elif velocidade < 20:
    print("Brisa leve")
elif velocidade < 50:
    print("Vento moderado")
else:
    print("Vento forte")


#5) Faça um programa que leia o tempo de reação de uma pessoa (em segundos). 
#Se for inferior a 0.3 segundos, deve escrever “Reflexo excelente”. 
#Se estiver entre 0.3 e 0.6 segundos, deve escrever “Bom tempo de reação”. 
#Caso contrário, deve escrever “Tempo de reação lento”.


tempo = float(input("Tempo de reação (em segundos): "))

if tempo < 0.3:
    print("Reflexo excelente")
elif tempo <= 0.6:
    print("Bom tempo de reação")
else:
    print("Tempo de reação lento")


#6) Faça um programa que leia uma palavra e converta-a para minúsculas com .lower(). Se tiver menos de 4 letras, mostrar “Palavra curta”. 
#Se tiver entre 4 e 7 letras, mostrar “Palavra média”. 
#Caso contrário, mostrar “Palavra longa”. 
#OBS.: A função len() devolve o número de caracteres numa string

palavra = input("Digite uma palavra: ").lower()

if len(palavra) < 4:
    print("Palavra curta")
elif len(palavra) <= 7:
    print("Palavra média")
else:
    print("Palavra longa")


#7) Escreva um programa que leia um ângulo em graus. 
#Se o ângulo for menor que 90, o programa deve calcular e mostrar o seu ângulo complementar (90 - ângulo). 
#Se for exatamente 90, deve indicar “Ângulo reto”. 
#Se for maior que 90, deve indicar “Não possui complementar”. 

angulo = float(input("Digite o ângulo (em graus): "))

if angulo < 90:
    complementar = 90 - angulo
    print(f"O ângulo complementar é {complementar}°")
elif angulo == 90:
    print("Ângulo reto")
else:
    print("Não possui complementar")


#8) Crie um programa que leia a nota final de um aluno (entre 0 e 20). 
#Se a nota for inferior a 10, escreva “Reprovado”. 
#Se estiver entre 10 e 14, escreva “Suficiente”. 
#Se estiver entre 15 e 17, escreva “Bom”. 
#Se for igual ou superior a 18, escreva “Excelente”. 

nota = float(input("Digite a nota final (0 a 20): "))

if nota < 10:
    print("Reprovado")
elif nota <= 14:
    print("Suficiente")
elif nota <= 17:
    print("Bom")
else:
    print("Excelente")


#9) Elabore um programa que leia a altitude de uma cidade (em metros). 
#O programa deve classificar: 
#• Menor que 200 → Região litorânea 
#• De 200 a 700 → Baixa altitude 
#• De 700 a 1500 → Média altitude 
#• Acima de 1500 → Alta altitude 
#O resultado deve ser mostrado de forma textual e clara. 

altitude = float(input("Digite a altitude da cidade (em metros): "))

if altitude < 200:
    print("Região litorânea")
elif altitude <= 700:
    print("Baixa altitude")
elif altitude <= 1500:
    print("Média altitude")
else:
    print("Alta altitude")


#10) Escreva um programa que leia as coordenadas de dois pontos no plano: (x1, y1) e (x2, y2). Calcule a distância entre eles usando math.sqrt. 
#Se a distância for menor que 5, mostre “Pontos próximos”. 
#Caso contrário, mostre “Pontos distantes”. 
#OBS.: A fórmula da distância entre dois pontos é:

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Distância entre os pontos: {distancia:.2f}")

if distancia < 5:
    print("Pontos próximos")
else:
    print("Pontos distantes")
