# Single / Double / Multi digit

n=int(input())

if n>=0 and  n<=9:
    print("single digit")
elif n>=10 and n<=99:
    print("Double digit")
else:
    print("multi digit")