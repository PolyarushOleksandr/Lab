digits = str(int(input("Enter a four-digit integer: ")))
first_sum = int(digits[0]) + int(digits[1])
last_sum = int(digits[2]) + int(digits[3])

print("True" if first_sum == last_sum else "False")
