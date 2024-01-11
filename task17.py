arr = [1, 1, 2, 0, -1, 3, 4, 4]
print(arr)
count = 0
#---------------------Первое решение:

# flag = True
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if i != j:
#             if arr[i] == arr[j]:
#                 flag = False
#                 break
#         else:
#             break
#     if flag == True:
#         count += 1
#     elif flag == False:
#         flag = True
# print("!", count)

#----------------Второе решение:

# for i in range(len(arr)):
#     print(arr[i])
#     print(arr[:i])
#     if arr[i] not in arr[:i]:
#         count += 1
# print("!", count)


# ----------------------Третье решение:

print(len(set(arr))) # Функция преобразует список в множество