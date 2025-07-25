# Write a program to print the following pattern.
# A
# B C
# D E F
# G H I J

def pattern_AB(n):
    C = 'A'
    ascii_A = ord(C)
    for i in range(n):
        for j in range(i+1):
            c1 =chr(ascii_A)
            print(c1, end=' ')
            ascii_A+=1
        print()    

pattern_AB(5)
