import admin

def nova():
    admin.limpa_tela()
    arquivo = open("palavras.txt","a")
    while True:
        nova = str(input("Informe uma nova palavra: ")).lower()
        arquivo.write(nova + "\n")
        continua = str(input("Deseja continuar? [S/N] ")).upper()
        if continua == "N": break
    arquivo.close()