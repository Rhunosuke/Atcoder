from heapq import heappush, heappop

N, M = map(int, input().split())
AB = [[] for _ in range(M)]

for i in range(N) :
    A, B = map(int, input().split())
    if A <= M :
        AB[A-1].append(B)

queue = []
ans = 0
for i in range(M) :
    for j in range(len(AB[i])) :
        heappush(queue, -AB[i][j])

    if len(queue) != 0 :
        ans += -heappop(queue)

print(ans)
