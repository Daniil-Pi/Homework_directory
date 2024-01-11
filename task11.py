# 0 1 1 2 3 5 8 13 ..
# 0 1 2 3 4 5 6 7..

A = int(input("Введите число: "))
count = 1
list = [0, 1]
temp = list[0]
while A > temp:
    count += 1
    list.append(list[count-1] + list[count-2])
    temp = list[count]
    
print("!!", count)

