#import random
#ex 1
#Como simular 10 lançamentos de um dado de 6 faces

#import random
#for i in range(10):
#    d=random.randint(1,6)
#    print(d)

#ex 2
#sortear nº
#se meu palpite for igual = ok
# se meu palpite for > nº = informar que tem que ser menor
#se meu palpite for < nº = informar que tem que ser mais
#quantos palpites

#numero_sorteado = random.randint(1, 10)
#tentativas = 0

#while True:
#    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
#    tentativas += 1
#    if palpite == numero_sorteado:
#        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
#        break
#    elif palpite > numero_sorteado:
#        print("O número é menor. Tente novamente.")
#    else:
#        print("O número é maior. Tente novamente.")



#ex3 - Função com condição e retorno
#A partir dos codigos
#10 lançamentos de um dado de 6 faces
#adivinhar um numero entre 1 e 20
#criar 2 funções, uma para cada uma destes jogos
#chamar as 2 funções se escolher:
# 1 . chamar dados
#2 - chamar adivinhar numero
# 0 - sair
# qualquer outro valor opção incorreta

import random
def lancar_dados():
    print("Lançando o dado 10 vezes:")
    for i in range(10):
        d = random.randint(1, 6)
        print(d)
    print("Fim dos lançamentos.\n")

def adivinhar_numero():
    numero_sorteado = random.randint(1, 20)
    tentativas = 0
    while True:
        try:
            palpite = int(input("Adivinhe o número (entre 1 e 20): "))
        except ValueError:
            print("Digite um número válido!")
            continue
        tentativas += 1
        if palpite == numero_sorteado:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        elif palpite > numero_sorteado:
            print("O número é menor. Tente novamente.")
        else:
            print("O número é maior. Tente novamente.")
    print("Fim do jogo.\n")

while True:
    print("Escolha uma opção:")
    print("1 - Lançar dados")
    print("2 - Adivinhar número")
    print("0 - Sair")
    opcao = input("Digite sua opção: ")
    if opcao == '1':
        lancar_dados()
    elif opcao == '2':
        adivinhar_numero()
    elif opcao == '0':
        print("Saindo do programa.")
        break
    else:
        print("Opção incorreta. Tente novamente.\n")

#ex3 - Função com condição e retorno
#A partir dos codigos
#10 lançamentos de um dado de 6 faces
#adivinhar um numero entre 1 e 20
#criar 2 funções, uma para cada uma destes jogos
#chamar as 2 funções se escolher:
# 1 . chamar dados
#2 - chamar adivinhar numero
# 0 - sair
# qualquer outro valor opção incorreta

