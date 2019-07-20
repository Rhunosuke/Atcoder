N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

sumList = [0] * (N+2)
sumList[0] = 0
sumList[1] = 1
sumList[2] = 2
for i in range(3, N+1) :
    sumList[i] = sumList[i-1] + sumList[i-2]
    sumList[i] %= 1000000007
if M == 0 :
    print(sumList[N])
    exit()

ans = 0
if a[0] == 1 :
    ans = 1
else :
    ans = sumList[a[0] - 1]
for i in range(1, M) :
    if a[i] - a[i-1] != 0 :
        if a[i] - a[i-1] == 1 :
            ans = 0
        else :
            ans *= sumList[a[i] - 2 - a[i-1]]
            ans = ans % 1000000007
if N - a[M-1] != 1 :
    ans *= sumList[N - 1 - a[M-1]]
print(ans % 1000000007)
