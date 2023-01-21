from random import choice
from time import sleep


def escolha_palavra(palavras : str) -> str:
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    return choice(palavras)

def forca(palavra: str, letras: str) -> str:
    erros = 0
    acertou = False
    enforcou = False

    while not enforcou and not acertou:
        
        chute = str(input("\nInforme uma letra: "))
        chute = chute.strip().upper()

        if chute in palavra:
            index = 0
            for letra in palavra:
                if chute == letra:
                    letras[index] = letra
                index += 1

        else:
            erros += 1

        print(erros)
        print(letras)

        if erros == 5:
            print("Você Perdeu!!")
            print(f"A palavra correta é {palavra}")
            enforcou = True
        elif "_" not in letras:
            print("Parabens!! Você acertou.")
            acertou = True

def game():
    print("*" *27)
    print("****** JOGO DA FORCA ******")
    print("*" *27)

    palavra = escolha_palavra(palavras=str).upper()
    letras = ["_" for letra in palavra]

    forca(palavra, letras)

    sleep(1)        
