c = [list(map(int, input().split())) for i in range(3) ]

ans = False

for i in range(101) :
    for j in range(101) :
        for k in range(101) :
            b1 = c[0][0] - i
            b2 = c[1][0] - i
            b3 = c[2][0] - i
            if j + b1 != c[0][1] :
                continue
            elif j + b2 != c[1][1] :
                continue
            elif j + b3 != c[2][1] :
                continue
            elif k + b1 != c[0][2] :
                continue
            elif k + b2 != c[1][2] :
                continue
            elif k + b3 != c[2][2] :
                continue
            ans = True

if ans :
    print('Yes')
else :
    print('No')
