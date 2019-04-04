H, W = map(int, input().split())

l = [['P' for _ in range(W + 2)] for _ in range(H + 2)]

for i in range(H) :
    s = list(input())
    for j in range(W) :
        l[i+1][j+1] = s[j]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = True

for i in range(1, H + 1) :
    for j in range(1, W + 1) :
        if l[i][j] != "#" :
            continue
        flag = False
        for k in range(len(dx)) :
            if l[i + dx[k]][j + dy[k]] == "#" :
                flag = True
                break
        if flag == False :
            ans = False

if ans :
    print('Yes')
else :
    print('No')
