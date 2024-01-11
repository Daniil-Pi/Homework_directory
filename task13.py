n = int(input("Введите общее количество дней: "))
count = 0
max = 0
arr = list(range(n))
for i in range(n):
    arr[i] = int(input(f"Введите температуру в {i+1} день: "))
    if arr[i] > 0:
        count += 1
        if count > max:
            max = count
    else:
        count = 0
print(max)