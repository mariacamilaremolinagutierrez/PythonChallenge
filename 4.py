from numpy import *
import urllib

base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

inicio = '63579'

res = 'and the next nothing is'

f = urllib.urlopen(base + inicio)
linea = f.read()
arr = linea.split(' ')

while(arr[0] == 'and'):

    inicio = arr[-1]

    print(inicio)

    f = urllib.urlopen(base + inicio)
    linea = f.read()
    arr = linea.split(' ')
