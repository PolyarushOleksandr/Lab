#n is distance car can drive per day
#m is total distance
n = int(input("Enter a number:"))
m = int(input("Enter second number:"))

print(f"Days needed: {m // n + (1 if m % n != 0 else 0)}")
