n = int(input())
flag = False
for i in range(1, n+1):
    if i*i == n:
        flag = True
        break
print("Perfect Square" if flag else "Not Perfect")
