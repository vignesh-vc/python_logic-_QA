# Product of digits of a number
# n = 334
# p = 1
# while n > 0:
#     p *= (n % 10)
#     n //= 10
# print(p)
n=334
p=1

while n>0:
   lastdigit=n%10
   p=p*lastdigit
   n //=10
print(p)
   