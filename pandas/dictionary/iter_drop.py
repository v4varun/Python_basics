import itertools as it

def drop_while(num):
    return it.takewhile(lambda x : x < 0,num)

nums = [-1,-2,-3,4,-10,2,0,5,12]
print(nums)
print(list(drop_while(nums)))