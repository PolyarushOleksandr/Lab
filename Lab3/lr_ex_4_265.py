
n = int(input("Enter the number of cars (1-30): "))
if n < 1 or n > 30:
    print("Invalid number of cars. Please enter a value between 1 and 30.")
else:
    speeds = []
    for i in range(n):
        speed = int(input(f"Enter the speed of car {i + 1} (1-300): "))
        if speed < 1 or speed > 300:
            print("Invalid speed. Please enter a value between 1 and 300.")
            break
        speeds.append(speed)
    else:
        average_speed = sum(speeds) / n
        print(f"Average speed: {average_speed:.1f} km/h")
        if any(speed > 60 for speed in speeds):
            print("Yes")
        else:
            print("No")