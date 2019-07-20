N, X = map(int, input().split())
l = list(map(int, input().split()))

cnt = 1
nowL = 0

for i in range(N) :
    nowL += l[i]
    if nowL <= X :
        cnt += 1
    else :
        break

print(cnt)
