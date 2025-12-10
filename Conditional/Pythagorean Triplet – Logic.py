# Pythagorean Triplet – Logic
a,b,c=sorted(map(int,input().split()))

if a*a+b*b==c*c:
    print("valit triplet")
else:
    print("not valid")