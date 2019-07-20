N = int(input())
p = list(map(int, input().split()))

cnt = 0

for i in range(1, N - 1) :
    #print(p[i], max(p[i-1:i+2]), min(p[i-1:i+2]))
    if p[i] != max(p[i-1:i+2]) and p[i] != min(p[i-1:i+2]) :
        cnt += 1


print(cnt)
