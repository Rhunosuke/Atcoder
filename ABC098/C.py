N = int(input())
S = input()

cntE = [0] * N
cntW = [0] * N

if S[0] == 'E' :
    cntE[0] = 1
if S[N-1] == 'W' :
    cntW[N-1] = 1

for i in range(1, N) :
    cntE[i] = cntE[i-1]
    if S[i] == 'E' :
        cntE[i] += 1

for i in range(N-1)[::-1] :
    cntW[i] = cntW[i+1]
    if S[i] == 'W' :
        cntW[i] += 1

cntSum = list(map(sum, zip(cntE, cntW)))
print(N - max(cntSum))
