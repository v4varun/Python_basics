

def puzzle(lst):
    j = 19
    k = 5
    cnt = cnt1 = 0
    for i in lst:
        if i == j: 
            cnt+=1
        elif i == k:
            cnt1+=1
        else:
            pass
    if cnt == 2 and cnt1 >= 3:
        return True
    else:
        return False

a = [19, 19, 15, 5, 3, 5, 5, 2]
b = [19, 15, 15, 5, 3, 3, 5, 2]
c = [19, 19, 5, 5, 5, 5, 5]
print(puzzle(a))
print(puzzle(b))
print(puzzle(c))

def puzzle1(lst):
    return lst.count(19) ==2 and lst.count(5) >= 3

print(puzzle1(a))
print(puzzle1(b))
print(puzzle1(c))