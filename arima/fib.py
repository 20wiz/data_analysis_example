

m = {}

def fib(x):
    if x <= 0:
        return 0
    if x == 1 or x == 2:
        ret =1
    else: 
        ret = fib(x-2) + fib(x-1)
    m[x] = ret
    print(x, ret)  # recursive call,  cannot keep order, can be duplicated 
    return ret

n = 5

print('result =', fib(n))

for k,v in sorted(m.items()):
    print(k, v)



# fib(0, 1)


# 1 1 2 3 5



