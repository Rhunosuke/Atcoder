n = int(input())
h = list(map(int, input().split()))

cnt = 0
ans = -1

for i in range(n - 1) :
    if h[i] >= h[i+1] :
        cnt += 1
    else :
        ans = max(cnt, ans)
        cnt = 0
ans = max(cnt, ans)

#print(h)
print(ans)
