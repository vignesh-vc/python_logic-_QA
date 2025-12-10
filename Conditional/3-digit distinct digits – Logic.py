# 3-digit distinct digits – Logic

n=int(input())
a=n//100
b=(n//10)%10
c=n%10

if a!=b and b!=c and a!=c:
    print("Distinct")
else:
    print("Not distinct")