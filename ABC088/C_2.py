c = [list(map(int, input().split())) for i in range(3) ]

ans = True

X = 0
b = [c[i][0] - X for i in range(3)]
a = [c[0][i] - b[0] for i in range(3)]

for i in range(3) :
    for j in range(3) :
        if a[j] + b[i] != c[i][j] :
            ans = False

if ans :
    print('Yes')
else :
    print('No')
