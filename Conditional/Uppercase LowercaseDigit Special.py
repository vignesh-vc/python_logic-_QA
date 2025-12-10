# Uppercase / Lowercase / Digit / Special
char=input()

if char.isupper():
    print("Uppercase")
elif char.islower():
    print("lower")
elif char.isdigit():
    print("Digit")
else:
    print("Special char")