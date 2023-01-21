from random import randrange  # utilizado para gerar um número aleatório.
from time import sleep

def game():
    print("*" *32)
    print("****** JOGO DA ADVINHAÇÃO ******")
    print("*" *32)
    maquina = randrange(0, 100, 1)
    contador = 0

    while True:
        escolha = int(input("Informe um número de 0 a 100: "))

        if escolha != maquina:
            print("Incorreto, tente novamente!")
            contador += 1
            if escolha > maquina:
                print("O número é menor.\n")
            elif escolha < maquina:
                print("O número é maior.\n")
        elif escolha == maquina:
            print(f"Parabéns, você acertou! Seu número de tentativas foi {contador+1}")
            break
        
        if contador == 5:
            print(f"Você usou o número maximo de tentativas e o jogo acabou para você, o número correto é {maquina}")
            break
    sleep(2)
        
if __name__ == "__main__":
    game()