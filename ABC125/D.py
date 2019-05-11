N = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A :
    if a < 0 :
        cnt += 1

A = list(map(abs, A))

if cnt % 2 == 0 :
    print(sum(A))
else : 
    print(sum(A) - min(A) * 2)
