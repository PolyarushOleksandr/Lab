V = float(input("Enter the speed: "))

if V < 0:
    print("Speed cannot be negative.")
else:
    print(f"Distance after 6 hours: {V * 6} km")
    print(f"Distance after 10 hours: {V * 10} km")
    print(f"Distance after 15 hours: {V * 15} km")
