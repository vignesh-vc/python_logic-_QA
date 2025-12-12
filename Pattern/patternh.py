def patternH(n):
    for row in range(1,n+1):
        for col in range(1,n-row+2):  #formula n-row+2
            print("*",end=" ")
        print()
   
patternH(int(input("Enter a number:")))