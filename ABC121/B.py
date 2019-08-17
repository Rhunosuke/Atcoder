n, m, c = map(int, input().split())
b = [int(inp) for inp in input().split()]
cnt = 0

for i in range(n) :
    sum = 0
    a = [int(inp) for inp in input().split()]
    for j in range(m) :
        sum += a[j] * b[j]
    if sum + c > 0 :
        cnt += 1

print(cnt)
