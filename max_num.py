
def max_num(arr):
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10,40,20,50,30]

print(max_num(arr))