from random import random, randint
from lista_opostos import lista_so_com_oposto
import os

def clear():
    os.system('clear')

clear()
while True:
    cmd = input('Comando: ')
    if cmd == 'sair': break
    clear()

    lista = []
    while len(lista) == 0:
        clear()
        lista = [randint(-1000,1000) for i in range(randint(0, 15))]
        print('lista inicial:')
        print(lista)
        retorno = lista_so_com_oposto(lista)
    print('Retorno:', retorno)
    print('Lista modificada:')
    print(lista)
