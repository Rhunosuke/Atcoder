N, A, B = map(int, input().split())
sum = 0

for i in range(1, N + 1) :
    bufSum = 0
    buf = i
    while buf / 10 != 0:
        bufSum += buf % 10
        buf = buf //10
    bufSum += buf
    if bufSum >= A and bufSum <= B :
        sum += i

print(sum)
