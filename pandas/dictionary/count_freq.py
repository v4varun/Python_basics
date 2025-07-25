def cnt_freq(str):
    d1 = {}
    for i in str:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    return d1

print(cnt_freq('w3resource'))            