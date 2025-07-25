# Write a program to print the following pattern.
#   1
#   2  3
#   4  5  6
#   7  8  9  10
#   11 12 13 14 15

def pattern_11(n):
    c = 1
    for i in range(n):
        for j in range(i+1):
            print(c, end=' ')
            c=c+1
        print()


pattern_11(5)