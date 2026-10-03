#Дано трицифрове ціле число. Визначити кількість однакових цифр у
#записі числа і вивести значення цієї кількості.
#155, 111, 478

digits = str(abs(int(input("Enter a three digit integer: "))))
count = max(digits.count(digit) for digit in set(digits))
print(count if count > 1 else 0)