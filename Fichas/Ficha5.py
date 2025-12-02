#1) Escrever um programa com a função sem parâmetros def contar_intervalo(): que lê dois inteiros
#inicio e fim (podem ser lidos em qualquer ordem) e mostra todos os números entre eles (incluindo os
#limites) que não terminem em zero.
#A função deve reorganizar os valores se o utilizador introduzir primeiro o maior e depois o menor.
#No programa principal, chamar contar_intervalo().
#2) Escrever um programa com a função sem parâmetros def estatisticas_valores(): que lê valores
#inteiros positivos até ser introduzido um valor menor ou igual a 0 e apresenta as estatísticas pedidas.

import random

LEDS_POR_DIGITO = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
}

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Introduza um número inteiro.\n")


def contar_intervalo():
    inicio = ler_inteiro("Introduza o primeiro inteiro: ")
    fim = ler_inteiro("Introduza o segundo inteiro: ")

    if inicio > fim:
        inicio, fim = fim, inicio

    for numero in range(inicio, fim + 1):
        if numero % 10 != 0:
            print(numero)


#2) Escrever um programa com a função sem parâmetros def estatisticas_valores(): que lê
#valores inteiros positivos enquanto o utilizador não introduzir um valor menor ou igual a 0. A função deve
#usar um ciclo while e, no final, mostrar:
#quantos valores foram lidos
#quantos são ímpares
#a média dos valores positivos
#Se nenhum valor positivo for introduzido, deve ser mostrada uma mensagem.

def estatisticas_valores():
    total_valores = 0
    impares = 0
    soma = 0

    while True:
        valor = ler_inteiro("Introduza um inteiro positivo (<= 0 para terminar): ")
        if valor <= 0:
            break

        total_valores += 1
        soma += valor
        if valor % 2 != 0:
            impares += 1

    if total_valores == 0:
        print("Nenhum valor positivo foi introduzido.")
    else:
        media = soma / total_valores
        print(f"Foram lidos {total_valores} valores positivos.")
        print(f"{impares} são ímpares.")
        print(f"Média dos valores positivos: {media:.2f}")

#6) Escrever um programa com a função def maior_de_tres(a, b, c): que recebe três inteiros e
#devolve o maior deles, usando apenas if / elif / else (sem usar funções prontas da linguagem para
#máximo). No programa principal, ler três números inteiros, chamar maior_de_tres(a, b, c) e mostrar
#o valor devolvido.

def maior_de_tres():
    a = ler_inteiro("Introduza o primeiro inteiro: ")
    b = ler_inteiro("Introduza o segundo inteiro: ")
    c = ler_inteiro("Introduza o terceiro inteiro: ")
    
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    
    print(f"O maior valor é {maior}")


#7) Escrever um programa com a função def lancamentos_moeda(n): que recebe um inteiro n maior
#que 0 e devolve o número de vezes que saiu “cara” ao lançar uma moeda virtual n vezes.
#Em cada lançamento, a função deve usar random.randint(0, 1), onde 0 representa “cara” e 1
#representa “coroa”.
#A função deve usar um ciclo for e devolver apenas a quantidade de “caras”. No programa principal, ler o
#valor de n, chamar lancamentos_moeda(n) e mostrar quantas vezes saiu “cara” e quantas vezes saiu
#“coroa” (o valor de “coroa” é calculado a partir de n).

def lancamentos_moeda(n):
    caras = 0
    for _ in range(n):
        if random.randint(0, 1) == 0:
            caras += 1
    return caras


def executar_lancamentos():
    while True:
        n = ler_inteiro("Quantos lançamentos pretende simular (> 0): ")
        if n > 0:
            break
        print("O número de lançamentos tem de ser maior do que zero.\n")

    caras = lancamentos_moeda(n)
    coroas = n - caras
    print(f"Resultados dos {n} lançamentos:")
    print(f"Cara: {caras}")
    print(f"Coroa: {coroas}")


#9o) João quer montar um painel de LEDs contendo diversos números. Entretanto o João não possui muitos
#LEDs, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos LEDs dos
#números, faça um algoritmo que ajude João a descobrir a quantidade de LEDs necessário para montar o valor.
#3 Exemplos de entrada e saída:
#115380 → 27
#2819311 → 29
#23456 → 25
#000 → 18
#Dica: Utilize pelo menos uma função para calcular o número de LEDs necessários para um número dado.


def leds_para_numero(numero_str):
    leds = 0
    for digito in numero_str:
        leds += LEDS_POR_DIGITO[digito]
    return leds


def executar_calculo_leds():
    while True:
        numero = input("Introduza o número (apenas dígitos): ").strip()
        if numero and numero.isdigit():
            break
        print("Entrada inválida. Introduza somente dígitos (0-9).\n")

    total_leds = leds_para_numero(numero)
    print(f"São necessários {total_leds} LEDs para mostrar o número {numero}.")


def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Contar intervalo")
        print("2 - Estatísticas de valores")
        print("3 - O Maior dos 3 numeros")
        print("4 - Lançamentos de moeda")
        print("5 - Número de LEDs")
        print("0 - Sair")
        opcao = input("Digite a sua opção: ")
        if opcao == "1":
            contar_intervalo()
        elif opcao == "2":
            estatisticas_valores()
        elif opcao == "3":
            maior_de_tres()
        elif opcao == "4":
            executar_lancamentos()
        elif opcao == "5":
            executar_calculo_leds()
        elif opcao == "0":
            print("A sair do programa.")
            break
        else:
            print("Opção incorreta. Tente novamente.\n")


menu()