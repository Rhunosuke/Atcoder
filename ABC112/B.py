N, T = map(int, input().split())
M = 1001
for _ in range(N) :
    c, t = map(int, input().split())
    if t <= T :
        M = min(M, c)
print(M if M != 1001 else 'TLE')
