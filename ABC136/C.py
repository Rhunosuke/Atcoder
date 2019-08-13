N = int(input())
H = list(map(int, input().split()))

ans = True

for i in range(1, N) :
    if H[i - 1] <= H[i] :
        continue
    if H[i - 1] <= H[i] + 1 :
        H[i] += 1
        continue
    ans = False

if ans :
    print('Yes')
else :
    print('No')
