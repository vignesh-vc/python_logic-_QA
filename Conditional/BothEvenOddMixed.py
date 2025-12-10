# Both Even / Odd / Mixed
a,b=map(int,input().split())

if a%2==0 and b%2==0:
    print("Both Even")
elif a%2!=0 and b%2!=0:
    print("Both Odd")
else:
    print("mixed")