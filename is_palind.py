def is_palind(str):
    if(str == str[::-1]):
        return True
    else:
        return False


print(is_palind("madam"))