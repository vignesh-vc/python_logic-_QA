# Password Rule – Logic
s = input()
has_digit = any(ch.isdigit() for ch in s)
if len(s) >= 8 and has_digit:
    print("Valid")
else:
    print("Invalid")
