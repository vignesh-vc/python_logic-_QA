# Letter / Digit / Other
ch=input()

if ch.isalpha():
    print("letter")
elif ch.isdigit():
    print("digit")
else:
    print("Other")