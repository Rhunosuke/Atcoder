N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
tmp = 0

for i in range(N) :
    #print(tmp)
    if i % 2 == 0 :
        tmp += A[i]
    else :
        tmp -= A[i]

ans[0] = tmp

for i in range(1, N) :
    ans[i] = 2 * A[i - 1] - ans[i - 1]

for i in range(N-1) :
    print(ans[i], end=" ")
print(ans[N-1])
