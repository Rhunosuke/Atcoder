N = int(input())
A = []
for i in range(N) :
    A.append(int(input()))

Amax = -1
Amax2 = -1
index = -1
index2 = -1

for i in range(N) :
    if Amax < A[i] :
        Amax = A[i]
        index = i

if A.count(Amax) > 1 :
    for i in range(N) :
        print(Amax)
    exit()

for i in range(N) :
    if i == index :
        continue
    if Amax2 < A[i] :
        Amax2 = A[i]
        index2 = i

for i in range(N) :
    if i == index :
        print(Amax2)
    else :
        print(Amax)
