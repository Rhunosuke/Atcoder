H, W = map(int, input().split())

S = []
for i in range(H) :
    S.append(list(input()))

for i in range(H) :
    for j in range(W) :
        cnt = 0
        if S[i][j] == "." :
            for a in range(-1, 2) :
                for b in range(-1, 2) :
                    if i + a >= 0 and i + a < H and j + b >= 0 and j + b < W :
                        if S[i + a][j + b] == "#" :
                            cnt += 1
            S[i][j] = str(cnt)

for i in range(H) :
    print(''.join(S[i]))
