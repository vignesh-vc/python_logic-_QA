def patterni(n):
    for row in range(1,n+1):
        for col in range(1,n-row+2):
            print(col,end=" ")
        print()

patterni(int(input("Enter a number:")))