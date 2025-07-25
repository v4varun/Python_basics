def fibo(num):
    if num <=0:
        return print("Please enter postive number")
    if num == 1:
        return 1
    if num == 2:
        return[0,1]
    
    fibon = [0,1]
    if num > 2:
        for i in range(2,num):
            next_val = fibon[i-1] + fibon[i-2]
            fibon.append(next_val)
    return fibon

print(fibo(10))
