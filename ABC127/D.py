N, M = map(int, input().split())
A = list(map(int, input().split()))

CList = []

for _ in range(M) :
    B, C = map(int, input().split())
    tuple = (B, C)
    CList.append(tuple)

for i in range(N) :
    CList.append((1, A[i]))

CList = sorted(CList, key=lambda t: t[1], reverse=True)

#print(CList)
ans = 0
sum = 0

for l in CList :
    ans += l[0] * l[1]
    sum += l[0]
    if sum >= N :
        ans -= l[1] * (sum - N)
        break

print(ans)
