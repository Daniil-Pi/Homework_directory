def SS(num, ss):
    arr = []
    res =''
    slov = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F",}
    while num >= ss:
        ost = num%ss
        if ost > 9:
            arr.append(slov[ost])
        else:
            arr.append(ost)
        num = num // ss
    if num > 9:
            arr.append(slov[num])
    else: 
        arr.append(num)
    arr.reverse()
    arr = list(map(str, arr))
    for i in range(len(arr)):
         res += arr[i]
    return res

num = int(input('Введите число: '))
ss = int(input("Введите сс: "))
print(SS(num, ss))