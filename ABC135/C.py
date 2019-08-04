N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
next = A[0]

for i in range(N) :
    buf = B[i] - next
    if buf <= 0 :
        cnt += B[i]
        next = A[i+1]
        continue
    cnt += next
    buf2 = buf - A[i+1]
    if buf2 <= 0 :
        cnt += buf
        next = A[i+1] - buf
        continue
    else :
        cnt += A[i+1]
        next = 0

print(cnt)
