# arr = [0, -1, 5, 2, 3]
# count = 0
# for i in range(len(arr)-1):
#     if arr[i+1] > arr[i]:
#         count += 1
# print(count)

list_1 = [1, 2, 3, 4, 5]
k = 6

# Введите ваше решение ниже
arr = []
flag = False
for i in range(len(list_1)):
    if list_1 == k:
        flag = True
        break
    else:
        arr.append(abs(list_1[i] - k))
print(arr)
min = arr[0]
ind = 0
for j in range(len(arr)):
    if min > arr[j]:
        min = arr[j]
        ind = j
print(list_1[ind])