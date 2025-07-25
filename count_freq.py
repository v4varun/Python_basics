def count_freq(str1):
    str2 = str1.split()
    freq = {}
    for i in str2:
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i]=1
            
    return freq



str1 = "my name is varun and varun is my name"
print(count_freq(str1))