def merge_list():
    a = [1,2,3]
    b = [3,4,5]
    c = [a+b for a,b in zip(a,b)]
    d = dict(zip(a,b))
    e = [[a+b for a in a] for b in b]
    print(c)
    print(d)
    print(e)

merge_list()