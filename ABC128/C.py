N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]
#for _ in range(M) :
#    l.append()
p = list(map(int, input().split()))

ans = 0

for a in range(2) :
    for b in range(2) :
        for c in range(2) :
            for d in range(2) :
                for e in range(2) :
                    for f in range(2) :
                        for g in range(2) :
                            for h in range(2) :
                                for i in range(2) :
                                    for j in range(2) :
                                        sl = [a, b, c, d, e, f, g, h, i, j]
                                        sl = sl[0:N]
                                        judge = [0] * M
                                        for m in range(M) :
                                            cnt = 0
                                            for ss in range(1, len(l[m])) :
                                                #cnt = 0
                                                if sl[l[m][ss] - 1] == 1 :
                                                    cnt += 1
                                                #print(cnt)
                                            if cnt % 2 == p[m] :
                                                #print(m, judge)
                                                judge[m] = 1
                                        #print(judge)
                                        if sum(judge) == M :
                                            #print(sl)
                                            ans += 1



ans /= (2 ** (10 - N))
ans = int(ans)

print(ans)

#for i in range(M) :
