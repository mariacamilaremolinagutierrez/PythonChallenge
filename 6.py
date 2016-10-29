from numpy import *
import os

path = 'channel/'
inicio = '90052'

directorio = os.listdir(path)
lista = []
lista.append(inicio)

for i in range(len(directorio) - 2):

    archivo = open(path + inicio + '.txt','r')
    inicio = archivo.readline().split(' ')[-1]
    archivo.close()

    lista.append(inicio)

print lista[-1]

import zipfile

zf = zipfile.ZipFile('channel.zip', 'r')
res = ''

for elemento in lista:
    res += zf.getinfo(elemento + '.txt').comment

print(res)
