# Finding the largest n such that n^3 < 12000

n = 1
while n ** 3 in range(12000):
    n += 1
print(n-1)
