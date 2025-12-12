def patternl(n):
    for row in range(1,n+1):
        
        for space in range(1,n-row+1):
            print("_",end="")
        for col in range(1,row+1):
            print("*",end="")
        print()
            
patternl(int(input("ENter a number:")))

# def patternK(n):
#     for row in range(1, n + 1):
#         colTimes = row
#         for space in range(1, n - colTimes + 1):
#             print(" ", end="")
#         for col in range(1, colTimes + 1):
#             print("*", end="")
#         print()
# patternK(int(input("ENter a number:")))
        