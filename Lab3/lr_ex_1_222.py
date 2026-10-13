
n = int(input("Enter a number: "))
if n <= 1 or n > 1000:
    print("Please enter a number greater than 1 and less than or equal to 1000.")
else:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("*35*")
        elif i % 3 == 0:
            print("*3*")
        elif i % 5 == 0:
            print("*5*")
        else:
            print(i)