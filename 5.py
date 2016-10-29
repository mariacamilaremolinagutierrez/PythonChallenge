from numpy import *
import pickle

# we open the file for reading
fileObject = open('banner.p','r')
# load the object from the file into variable b
b = pickle.load(fileObject)

for bb in b:
    linea = ''
    for bb8 in bb:
        car = bb8[0]
        num = bb8[1]
        parte = ''
        for i in range(num):
            parte += car

        linea += parte
    print(linea)
