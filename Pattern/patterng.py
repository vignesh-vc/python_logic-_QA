def patterg(n):
    incrementvalue=1
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(incrementvalue,end=" ")
            incrementvalue +=1
        print()
    
  
patterg(int(input()))