x=int(input())
for i in range(x):
    y,z=map(int,input().split())
    print(max(0,y-z))
