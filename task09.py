# n = int(input("Введите факториал: "))
# f = 1
# if n > 0:
#     while n > 0:
#         f *= n
#         n -= 1
#     print(f"Ответ: {f}")
# else:
#     print(f"Ответ: {f}")

n = int(input("Введите факториал: "))
def f(n):
    if n > 0:
        return n * f(n-1)
    else:
        return 1
print(f(n))