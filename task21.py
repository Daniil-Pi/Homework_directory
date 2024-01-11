arr = [{1: 1003}, {2: 1002}, {2: 1001}, {3: 1004}, {4: 1004}, {5: 1006}, {6: 1002}, {7: 1004}, {8: 1003}]
arr2 = []
arr3 = []
temp = 0
flag = True
for i in range(len(arr)):
    for k in arr[i].values():
        arr2.append(k)

for i in range(len(arr2)):
    for j in range(len(arr2)):
        if i == j:
            continue
        else:
            if arr2[i] == arr2[j]:
                flag = False
                break

    if flag == True:
        arr3.append(arr2[i])
    else:
        flag = True
print(arr2)
print(arr3)