
n = int(input())

total = n * (n + 1) // 2
for i in range(n - 1):
	card = int(input())
	total -= card

print(total)
