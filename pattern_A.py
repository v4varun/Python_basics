# Write a program to print the following pattern.
# A
# B B
# C C C
# D D D D

def pattern_A(n):
    C='A'
    ascii_A=ord(C)   
    for i in range(n):
        C1 = chr(ascii_A)
        for j in range(i+1):
            print(C1, end=' ')
        ascii_A+=1
        print()

pattern_A(5)
    