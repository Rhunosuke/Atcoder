import heapq
import queue

'''
TLE code

'''

def push_property(h, cost, v, d) :
    if cost[v] != float('INF') :
        return
    heapq.heappush(h, [d, v])
    cost[v] = d


n, x, y = map(int, input().split())
x -= 1
y -= 1

ans = [0] * n

for i in range(n) :
    h = []
    heapq.heapify(h)
    heapq.heappush(h, [0, i])
    cost = [float('INF') for _ in range(n)]
    push_property(h, cost,  i, 0)
    while len(h) != 0 :
        v = heapq.heappop(h)[1]
        d = cost[v]

        #print(i, v, d, cost, 'IN')
        #print(v, d)
        if v+1 < n :
            push_property(h, cost, v+1, d+1)
        if v-1 >= 0 :
            push_property(h, cost, v-1, d+1)
        if v == x :
            push_property(h, cost, y, d+1)
        if v == y:
            push_property(h, cost, x, d+1)
        #print(i, v, d, cost)
    for j in range(n) :
        ans[cost[j]] += 1

for i in range(1, n) :
    print(ans[i] // 2)
