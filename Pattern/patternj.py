def patternj(n):
    for row in range(1,n+1):
        for col in range(1,n-row+2):
            print(n-row+1,end=" ")
        print()
    

patternj(int(input("Enter a number:")))