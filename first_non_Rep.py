"""first not repeating chracter within String"""

def fnrpt(str):
    for i in str:
        if str.count(i) == 1:
            return i
        

str="NETSETOSNETM"
print(fnrpt(str))
