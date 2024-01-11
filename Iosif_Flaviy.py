from math import *
def f(n,k):
    arr = []
    arr = [i for i in range(1,n+1)]
    count = 0
    while len(arr) >= 1:
        count += 1
        print(arr)
        print(f'count = {count}')
        if count < k and len(arr)>1:
            save = arr.pop(0)
            arr.append(save)
        elif len(arr) > 1:
            del arr[0]
            count = 0
        else:
            return arr
        
n= int(input())
k = int(input())
print(*f(n,k))