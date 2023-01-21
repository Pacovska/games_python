import advinha
import forca
import admin

def menu(escolha : int) -> int:
    admin.limpa_tela()
    print("*" * 40)
    print("*" *11, "ESCOLHA UM JOGO", "*" * 12)
    print("*" * 40)


    while True:
        admin.limpa_tela()
        print("(1) Forca - (2) Advinha - (3)Voltar")
        
        try:
            escolha = int(input("Digite sua escolha: "))
            break
        except Exception as e:
            print(e)

    return escolha

def main():
    while True:
        admin.limpa_tela()
        print("Com o modo jogador, você poderá escolher qual jogo deseja jogar.")
        print("Já no modo administrador, você irá conseguir inserir novas palabras ao jogo forca.")
        
        while True:
            print("(1) Administrador - (2) Jogador")

            try:
                escolhe = int(input("Você deseja escolher entre admin ou jogador: "))
                break
            except:
                print("\nEntrada Invalida!!")
        

        if escolhe == 1:
            admin.admin()
        elif escolhe == 2:
            opcao_jogo = menu(escolha=int)
            if opcao_jogo == 1:
                admin.limpa_tela()
                forca.game()
            elif opcao_jogo == 2:
                admin.limpa_tela()
                advinha.game()
            elif opcao_jogo == 3:
                admin.limpa_tela()

if __name__ == "__main__":
    main()