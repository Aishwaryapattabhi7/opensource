x=int(input())
arr=list(map(int,input().split()))
y=[]
for num in arr:
    if num not in y:
        y.append(num)
print(*y)
