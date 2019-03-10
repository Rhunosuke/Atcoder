N, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

rest = x
i = 0
cnt = 0

while rest > 0 :
    if rest < a[i] :
        break
    rest -= a[i]
    i += 1
    if (i == N) :
        if (rest == 0) :
            cnt += 1
        break
    cnt += 1

print(cnt)
