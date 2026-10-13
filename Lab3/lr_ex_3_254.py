
d = float(input("Enter the distance covered on the first day (in km): "))
t = float(input("Enter the target total distance (in km): "))
days = 1
while d < t:
    d *= 1.1
    days += 1
print(f"Total distance covered after {days} days: {d:.2f} km")