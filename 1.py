from numpy import *

#s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
s = "map.html"
ss = ""

abc = array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

for i in range(len(s)):
    p=s[i]
    if(p == " " or p == "." or p == "(" or p == ")" or p == "'" or p == "/" or p == ":"):
        ss+=p
    else:    
        ind = where(abc == p)[0][0]
        if(ind<24):
            ss += abc[ind+2]
        elif(ind==24):
            ss+='a'
        elif(ind==25):
            ss+='b'

print(ss)
