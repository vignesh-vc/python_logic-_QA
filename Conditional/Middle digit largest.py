# Middle digit largest?
n=int(input())
a=n//100
b=(n//10)%10
c=n%10

if b>a and b>c:
    print("Middle is largest")
elif b<a and b<c:
    print("Midle is smallest")
else:
    print("neither")