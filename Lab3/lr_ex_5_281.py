
n = int(input())

a = 0
b = 1
k = 0

while a < n:
    a, b = b, a + b
    k += 1

if a == n:
    print(k)
else:
    print(-1)
    