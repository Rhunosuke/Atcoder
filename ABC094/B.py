n, m, x = map(int, input().split())
a = [int(inp) for inp in input().split()]

cnt = sum(a[i] < x for i in range(m))

print(min(cnt, m - cnt))
