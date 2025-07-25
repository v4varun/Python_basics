import numpy as np

def arrays(arr):
    arr1 = np.array(arr, dtype = int)
    arr2 = arr1.reshape(3, 3)
    return arr2

def arrays1(arr):
    arr1 = np.array(arr, dtype = int)
    arr2 = np.array(arr[::-1], dtype = float)
    return arr2
arr = input().strip().split(' ')

def arrays2(arr):
    arr1 = np.array(arr, dtype = int)
    arr2 = np.zeros(arr1, dtype = int)
    return arr2

arr = input().strip().split(' ')

print(arrays2(arr))