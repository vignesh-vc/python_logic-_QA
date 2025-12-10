# Largest of 3 numbers
a=int(input("Ente  Number A:"))
b=int(input("Ente  Number b:"))
c=int(input("Ente  Number c:"))

if a>=b and a>=c:
    print(a,"a is a largest")
elif b>=c:
    print(b,"b is a Largest")
else:
    print(c,"c is a largest")