#Quadrant
x,y=map(int,input().split())

if x>0 and y>0:
    print("q1")
elif x<0 and y>0:
    print("q2")
elif x<0 and y<0:
    print("q3")
elif x>0 and y<0:
    print("q4")
else:
    print("on axis")