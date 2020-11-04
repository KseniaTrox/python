#n = list(input("Введите целое положительное число "))
#print(max (n))
n = int(input("Введите целое положительное число "))
list = []
a = 0
while n != 0:
    a = n % 10
    list.append(a)
    n = n // 10
print(max(list))
