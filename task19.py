arr = [1, 2, 3, 4, 5]
k = int(input("Введите k: "))

# Первое решение:

# for i in range(k):
#     for j in range(len(arr)-1, 0, -1):
#         if j > 0:
#             arr[j],arr[j-1] = arr[j-1], arr[j]
#             print("test!!!!: ", arr)
#         else:
#             arr[-1],arr[j] = arr[j], arr[-1]
#     print("test: ", arr)
# print(arr)

# Второе решение:

temp = 0
for i in range(k):
    temp = arr.pop(0)
    arr.append(temp)
    print(arr)