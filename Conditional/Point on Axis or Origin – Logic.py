# Point on Axis or Origin – Logic
x,y=map(int,input().split())
if x==0 and y==0:
    print("origin")
elif x==0:
    print("y axis")
elif y==0:
    print("x Axis")
else:
    print("Inside a quadrant")