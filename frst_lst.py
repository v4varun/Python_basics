def frst_lst(str):
    if len(str) < 2:
        return ""
    else:
        return str[0:2] + str[-2:]


print(frst_lst('w3resource'))
