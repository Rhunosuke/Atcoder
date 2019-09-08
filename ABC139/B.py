a, b = map(int, input().split())

if b == 1 :
    print(0)
elif b <= a :
    print(1)
else :
    cnt = b
    ans = 0
    cnt -= a
    ans = 1
    while cnt > 0 :
        cnt -= (a-1)
        ans += 1
    print(ans)
