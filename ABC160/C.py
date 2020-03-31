k, n = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n-1) :
    b[i] = a[i+1] - a[i]

b[n-1] = k + a[0] - a[n-1]

print(sum(b) - max(b))
