n = int(input())
b = list(map(int, input().split()))

ans = b[0] + b[n-2]

for i in range(n-2) :
    ans += min(b[i], b[i+1])

print(ans)
