x,y=input().split()
if x==y:
    print("NULL")
elif (x=='S' and y=='P') or (x=='R' and y=='S') or (x=='P' and y=='R'):
    print("Vignesh")
else:
    print("Charan")
