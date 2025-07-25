def first_char_occur(str):
    s = str[0]
    str = str.replace(s,'$')
    str1 = s + str[1:]
    return str1

print(first_char_occur('restart'))

      
      
