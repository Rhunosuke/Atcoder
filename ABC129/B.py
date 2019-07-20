N = int(input())
W = list(map(int, input().split()))

WSum = sum(W)

min = 99999
partSum = 0

for i in range(N) :
    partSum += W[i]
    if abs(2*partSum - WSum) < min :
        min = abs(2*partSum - WSum)

print(min)
