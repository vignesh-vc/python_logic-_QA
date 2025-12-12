def patternk(n):
    for row in range(1,n*2):
        coltimes=(n*2-row) if row>n else row
        for col in range(1,coltimes+1):
            print(col,end=" ")
        print()
  
    
patternk(int(input()))