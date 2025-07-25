"""find common letter between two string"""
def cmn_ltr(str1,str2):
    return set(str1) & set(str2)

str1="HIMADRI"
str2="SHILA"
print(cmn_ltr(str1,str2))

