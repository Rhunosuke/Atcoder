import re

N, Q = map(int, input().split())
S = input()
L = [list(map(int, input().split())) for i in range(Q)]

array = []

for m in re.finditer(r'AC', S):
    array.append(m.start())


for i in range(Q) :
    count = 0
    for j in range(len(array)) :
        if L[i][0] - 1 <= array[j] and L[i][1] - 2 >= array[j] :
            count += 1
    print(count)
