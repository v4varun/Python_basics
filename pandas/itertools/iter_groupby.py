from itertools import groupby

def encode(str):
    #return [(len(list(n)),m) for m,n in groupby(str)]
    return [(n,m) for m,n in groupby(str)]

str1 = "AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD" 

print(encode(str1))