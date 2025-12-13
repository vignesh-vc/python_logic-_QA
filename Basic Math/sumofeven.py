# def sum_of_evens(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             total += i
#     return total

# n = int(input("Enter a number: "))
# print(sum_of_evens(n))


def sum_of_evens(n):
    k=n//2
    return k*(k+1)
    
 
n = int(input("Enter a number: "))
print(sum_of_evens(n))
