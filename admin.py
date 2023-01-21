import adiciona_palavra
import os
from time import sleep

def limpa_tela():
    return os.system("cls")

def auth(user : str, passwd : str) -> bool:
    return user == "admin" and passwd == "admin"

def admin():
    while True:
        limpa_tela()
        print("**********************")
        print("* MENU ADMINISTRADOR *")
        print("**********************")
        user = input("USUARIO: ") 
        passwd = input("SENHA: ")
        if auth(user, passwd):
            adiciona_palavra.nova()
            break
        else:
            print("Usuario e senha incorretos.")
            sleep(1)
            continue