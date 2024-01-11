# arr = [1, 2, 3, 5, 8, 15, 23, 38]
# arr2 = []
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         arr2.append((arr[i], arr[i]**2))
# print(arr2)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)