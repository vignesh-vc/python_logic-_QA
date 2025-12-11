# Print all even numbers from 1 to 100
n=100
for i in range(1,100+1):
    if i%2==0:
        print(i,end=" ")
        
for i in range(2,n,2):
    print(i,end=" ")