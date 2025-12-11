# Sum of digitsn-
n=567
s=0
while n>0:
    s +=n%10   
    n //=10 
print(s)

#n % 10 → last digit எடுக்க

#n // 10 → அந்த digit-ஐ number-ல இருந்து remove பண்றதுக்கு 
      