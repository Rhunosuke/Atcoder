n, k = map(int, input().split())
s = list(input())

seqCnt = 0
seqTotal = 0
for i in range(n-1) :
    if s[i] == s[i+1] :
        seqCnt += 1
    if s[i] != s[i+1] or i == n - 2 :
        seqTotal += seqCnt
        seqCnt = 0

print(min(seqTotal + 2*k, n-1))
