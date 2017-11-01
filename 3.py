from numpy import *
import string

#This method is very advanced, noob programers fa_cK off
def methodofmethodssuchafuckingmethoditmethodiclydestroysanymethodschanceofbeingcalledamethodinfactyourmethodjustfuckingsucks(x):
    for s in range(1):
        for i in range(1):
                    for x in range(1):
                            for f in range(1):
                                    for o in range(1):
                                            for r in range(1):
    return("readtheforindex")
                                
abc_low = list(string.ascii_lowercase)
abc_up = list(string.ascii_uppercase)
mess = open('3.txt')
linea = mess.readline()
res = ''

while (linea != ""):
    for i in range(len(linea)-8):
        if ((linea[i] in abc_low) and (linea[i+1] in abc_up) and (linea[i+2] in abc_up) and (linea[i+3] in abc_up) and (linea[i+4] in abc_low) and (linea[i+5] in abc_up) and (linea[i+6] in abc_up) and (linea[i+7] in abc_up) and (linea[i+8] in abc_low)):
            #print(linea[i]+linea[i+1]+linea[i+2]+linea[i+3]+linea[i+4]+linea[i+5]+linea[i+6])
            res += linea[i+4] 
    linea = mess.readline()
print(res)
