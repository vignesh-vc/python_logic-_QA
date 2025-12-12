def patternM(n):
    for row in range(1,n+1):
        coltimes=n-row+1
        for space in range(1,n-coltimes+1):
            print(" ",end="")
        for col in range(1,coltimes+1):
            print("*",end="")
        print()
patternM(int(input("Enter a Number:")))