# Функция enumerate() применяется к итерируемому объекту и
# возвращает новый итератор с кортежами из индекса и элементов входных
# данных. 

# users = ["user1", "user2", "user3"]
# data = list(enumerate(users))
# print(data)


def is_pangram(text):
    k = "q w e r t y u i o p l k j h g f d s a z x c v b n m"
    k = k.split()
    if len(text) < 26:
        return False
    else:
        text = text.lower()
        text = text.split()
        temp = []
        for j in range(len(text)):
            temp.extend(text[j])
        for i in temp:
            print(f'i = {i}')
            if i in k:
                k.remove(i)
    if k == []:
        return True
    else:
        return False

# считываем данные
text = input("введи: ")

# вызываем функцию
print(is_pangram(text))