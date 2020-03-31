import heapq

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
pq = p[:x]+q[:y]
heapq.heapify(pq)

for e in r :
    heapq.heappushpop(pq, e)

print(sum(pq))
