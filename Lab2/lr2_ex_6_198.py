a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

a, b, c = sorted((a, b, c))

if a <= 0 or a + b <= c:
	print("impossible")
elif a**2 + b**2 == c**2:
	print("rectangular")
elif a**2 + b**2 > c**2:
	print("acute")
else:
	print("obtuse")
