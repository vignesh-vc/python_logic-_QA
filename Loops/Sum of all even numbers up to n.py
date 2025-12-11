# Sum of all even numbers up to n
n=int(input("Enter a number:"))
even=0
for i in range(2,n+1,2):
    even +=i
print(even)