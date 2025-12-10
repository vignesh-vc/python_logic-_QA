# Clock Angle
h, m = map(int,input().split())
hour_angle = 30*h + 0.5*m
min_angle = 6*m
diff = abs(hour_angle - min_angle)
print(min(diff, 360-diff))
