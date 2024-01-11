from math import *
def f(n):
    
    k = 0
    for j in range(n):
        arr = []
        for i in range(n):
            if j<i:
                break
            else:
                k=int(factorial(j)/(factorial(i)*factorial(j-i)))
                arr.append(k)
        print(arr)
    
    
n = int(input())
f(n)