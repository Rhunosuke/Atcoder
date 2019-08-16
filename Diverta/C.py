N = int(input())
S = [input() for _ in range(N)]

cnt = 0
cntA = 0
cntB = 0
cntAB = 0

for s in S :
    for i in range(1, len(s)) :
        if s[i - 1] =='A' and s[i] == 'B':
            cnt += 1
    if s[0] == 'B' and s[len(s) - 1] == 'A':
        cntAB += 1
    elif s[0] == 'B' :
        cntB += 1
    elif s[len(s) - 1] == 'A' :
        cntA += 1

ans = min(cntA, cntB)
if cntAB >= 2 :
    ans += (cntAB - 1)
if cntAB >= 1 and max(cntA, cntB) != 0:
    ans += 1

'''
if max(cntA, cntB) == 0:
    ans = cntAB - 1
else :
    ans += cntAB
'''
if ans == len(S) :
    ans -= 1

print(cnt + ans)
