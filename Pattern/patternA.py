def patternA(n):
 for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=" ")
    print()
        
patternA(int(input("Enter a number:")))