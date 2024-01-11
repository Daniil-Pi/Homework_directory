# Функция zip() применяется к набору итерируемых объектов и
# возвращает итератор с кортежами из элементов входных данных

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)


# Функция zip () пробегает по минимальному входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)