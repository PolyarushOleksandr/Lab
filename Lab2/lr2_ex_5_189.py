number = int(input("Enter an number: "))
last_two_digits = (number) % 100
last_digit = (number) % 10

if 11 <= last_two_digits <= 14:
	currency_word = "Hryven"
elif last_digit == 1:
	currency_word = "Hryvnia"
elif 2 <= last_digit <= 4:
	currency_word = "Hryvni"
else:
	currency_word = "Hryven"

print(number, currency_word)
