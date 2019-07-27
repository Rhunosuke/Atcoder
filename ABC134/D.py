N = int(input())
a = list(map(int, input().split()))

b = [0] * N

for i in range(N//2, N) :
    b[i] = a[i]

for i in range(0, N//2)[::-1] :
    buf = 0
    for j in range(1, N//(i+1)) :
        buf += b[(i+1)*(j+1) - 1]
    buf += a[i]
#    if i == 0 :
#        print(i, buf, a[i])
    if buf % 2 == a[i] :
        b[i] = a[i]
    else :
        if a[i] == 1 :
            b[i] = 0
        if a[i] == 0 :
            b[i] = 1
#        if i == 0 :
#            print(a[i], b[i])
#print(b)
ans = []
cnt = 0

for i in range(N) :
    if b[i] == 1 :
        ans.append(i+1)
        cnt += 1

print(cnt)
for i in range(len(ans)) :
    print(ans[i], end=" ")
if len(ans) > 0 :
    print()
