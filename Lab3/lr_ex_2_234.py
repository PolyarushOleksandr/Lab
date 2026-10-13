
n = int(input("Введіть кількість днів: "))

total = 0

for i in range(n):
    m = int(input("Введіть кількість помилок за день: "))
    total += m

print("Загальна кількість помилок:", total)