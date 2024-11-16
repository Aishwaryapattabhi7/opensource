x=int(input())
num=1
for i in range(x):
    print(*range(num, num + i + 1))
    num += i + 1
