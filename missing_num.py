"""find missing number in array"""

def missing_num(arr1):
    n = max(arr1)
    n1 = n*(n+1)//2
    a1 = sum(arr1)
    print(f"{n},{n1},{a1}")
    return n1 - a1

arr1 = [1,2,3,4,5,7,8]

print(missing_num(arr1))
