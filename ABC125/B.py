N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0

for i in range(len(V)) :
    if V[i] > C[i] :
        ans += V[i] - C[i]


print(ans)
