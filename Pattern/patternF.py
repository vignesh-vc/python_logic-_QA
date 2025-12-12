def patterF(n):
    for row in range(1,n+1):
        invert=0 if row%2==0 else 1
        for col in range(1,row+1):
            print(invert,end=" ")
            invert=0 if invert%2==1 else 1
        print()
    
patterF(int(input("enter a number:")))
            