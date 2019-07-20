N, L = map(int, input().split())

taste = [0] * N
minimum = 10000
minAbs = 10000

for i in range(N) :
    taste[i] = L + i
    if abs(taste[i]) < minAbs :
        minimum = taste[i]
        minAbs = abs(taste[i])

print(sum(taste) - minimum)
