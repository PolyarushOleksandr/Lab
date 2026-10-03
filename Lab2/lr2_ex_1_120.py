# Distance in kilometers
distance = float(input("Enter distance in kilometers: "))
minutes = float(input("Enter time in minutes: "))

if minutes <= 0:
	print("Time must be greater than zero.")
else:
	speed = distance * 60 / minutes
	print(f"Speed: {speed} km/h")

	if speed > 60:
		print("Traffic rules are not met.")
	else:
		print("Traffic rules are executed.")
