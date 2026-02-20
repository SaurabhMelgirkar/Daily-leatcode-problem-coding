import math
def Unique(m,n):
    total=math.comb(m+n-2 , m-1)
    return total
res=Unique(3,2)
print(res)

# logic 2 
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def unique_paths(m, n):
    total = m + n - 2
    down = m - 1
    right = n - 1
    return factorial(total) // (factorial(down) * factorial(right))

print(unique_paths(3, 3))  # 6