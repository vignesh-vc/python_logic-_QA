def patternE(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(row,end=" ")
        print()
patternE(int(input("Enter a number:")))