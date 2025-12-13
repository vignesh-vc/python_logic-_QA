ch=input("Enter a char:")
freq=[0]*52

for s in ch:
    freq[ord(s)-ord('A')]+=1
for i in range(26):
    print(chr(i+ord('A')),"=",freq[i])