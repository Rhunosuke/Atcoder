import re

N, Q = map(int, input().split())
S = input()
L = [list(map(int, input().split())) for i in range(Q)]

array = [0 for i in range(N + 1)]
for i in range(N) :
    array[i + 1] = array[i] + (1 if S[i: i + 2] == 'AC' else 0)

for i in range(Q) :
    print(array[L[i][1] - 1] - array[L[i][0] - 1])
