import random
def jogo():
    opcoes = ['pedra', 'papel', 'tesoura']
    while True: 
        jogador = input("escolha entre pedra, papel e tesoura:  ")
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")
        if jogador == computador:
         print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or ( jogador == "papel" and computador == "pedra") or ( jogador == "tesoura" and computador == "papel"):
         print("Ganhou!!!")
        else:
         print("Perdeu!")
jogo()