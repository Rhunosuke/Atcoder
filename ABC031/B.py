L, H = map(int, input().split())
A = [int(input()) for _ in range(int(input()))]
for i in range(len(A)) :
    print(-1 if A[i] > H else max(L - A[i], 0))
