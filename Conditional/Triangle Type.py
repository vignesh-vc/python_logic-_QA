#Triangle Type
a,b,c=map(int,input().split())
if a==b==c:
    print("Equilateral")
elif a==b or b==c:
    print("Isosceles")
else:
    print("scalene")