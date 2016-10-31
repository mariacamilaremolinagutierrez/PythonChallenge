from numpy import *
import string

abc=list(string.ascii_lowercase)
mess=open('mess.txt')
linea=mess.readline()

while (linea != ""):

    for car in linea:
        if (car in abc):
            print(linea)

    linea = mess.readline()
        

