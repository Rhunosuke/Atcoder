import queue

'''
TLE code

'''

def put_property(q, cost, v, d) :
    if cost[v] != float('INF') :
        return
    q.put(v)
    cost[v] = d


n, x, y = map(int, input().split())
x -= 1
y -= 1

ans = [0] * n

for i in range(n) :
    q = queue.Queue()
    cost = [float('INF') for _ in range(n)]
    put_property(q, cost,  i, 0)
    while not q.empty() :
        v = q.get()
        d = cost[v]
        #print(i, v, d, cost, 'IN')
        #print(v, d)
        if v+1 < n :
            put_property(q, cost, v+1, d+1)
        if v-1 >= 0 :
            put_property(q, cost, v-1, d+1)
        if v == x :
            put_property(q, cost, y, d+1)
        if v == y:
            put_property(q, cost, x, d+1)
        #print(i, v, d, cost)
    for j in range(n) :
        ans[cost[j]] += 1

for i in range(1, n) :
    print(ans[i] // 2)
