#Time Greeting
time=int(input("Enter time:"))
if time>=5 and time<=11:
    print("Morning")
elif time>=12 and time<=16:
    print("afternoon")
elif time>=17 and time<=20:
    print("Evening")
else:
    print("Night")