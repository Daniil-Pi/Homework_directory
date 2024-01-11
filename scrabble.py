# # Русский алфавит:

# och1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
# och2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
# och3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
# och4 = ['Й', 'Ы']
# och5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
# och8 = ['Ш', 'Э', 'Ю']
# och10 = ['Ф', 'Щ', 'Ъ']

# # Английский алфавит

# och10 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
# och20 = ['D', 'G']
# och30 = ['B', 'C', 'M', 'P']
# och40 = ['F', 'H', 'V', 'W', 'Y']
# och50 = ['K']
# och80 = ['J', 'X']
# och100 = ['Q', 'Z']

# k = input('Введите слово: ')
# k = k.upper()
# print(k)
# count = 0


# for i in range(len(k)):
#     if k[i] == "Щ":
#         count += 10
#         continue
#     if k[i] in och1 or k[i] in och10:
#         count += 1
#         continue
#     if k[i] in och2 or k[i] in och20:
#         count += 2
#         continue
#     if k[i] in och3 or k[i] in och30:
#         count += 3
#         continue
#     if k[i] in och4 or k[i] in och40:
#         count += 4
#         continue
#     if k[i] in och5 or k[i] in och50:
#         count += 5
#         continue
#     if k[i] in och8 or k[i] in och80:
#         count += 8
#         continue
#     if k[i] in och10 or k[i] in och100:
#         count += 10
#         continue

# print(count)

# Второе решение:

k = input("Введите слово: ")

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j
print(count)
