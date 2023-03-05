
print("Bведите пожалуйста число М, максимальная масса одной лодки: ")
m = int(input())
print("Bведите пожалуйста число N, количество рыбаков: ")
n = int(input())
res = []
res1 = []
cnt = 0
if (m >= 1 and m <= 10000000) and (n >= 1 and n <= 100):
    for i in range(n):
        a = int(input("Введите вес рыбака: "))
        if a >= 1 and a <= m/2:
            res.append(a)
        else:
            res1.append(a)
else:
    print("Введено число, не соответствующее условиям!")

cnt = 0
l = len(res)
l1 = len(res1)
if l > l1:
    tmp = l - l1
    if tmp % 2 == 0:
        cnt = tmp//2 + l1
    else:
        cnt = tmp//2 + l1 + 1
else:
    cnt = l1
print("Количество необходимых лодок: ", cnt)