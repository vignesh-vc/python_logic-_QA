# Sum of all odd numbers up to n
n=int(input("Enter a number:"))
odd=0
for i in range(1,n+1,2):
    odd +=i
print(odd)