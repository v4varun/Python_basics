def cnt_chr(str):
    s = {}
    for i in str:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    return s

print(cnt_chr('google.com'))            



