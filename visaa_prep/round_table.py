x=int(input())
ways=1
for i in range(1,x+1):
    ways*=i
print(ways)
