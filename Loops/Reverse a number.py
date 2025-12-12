# Reverse a number
n=int(input("Enter a number"))
rev=0
while n>0:
    lastdigit=n%10
    rev=rev*10+lastdigit
    n //=10
print(rev)

# Number = 123

# Step 1:

# rev = 0
# digit = 3
# rev = 0 × 10 + 3 = 3

# Step 2:

# digit = 2
# rev = 3 × 10 + 2 = 32

# Step 3:

# digit = 1
# rev = 32 × 10 + 1 = 321

# 🎉 Final reverse = 321