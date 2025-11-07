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

