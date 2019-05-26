N, M = map(int, input().split())
L = []
R = []
for _ in range(M) :
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


borderL = L[0]
borderR = R[0]
for i in range(1, M) :
    if L[i] > borderL :
        borderL = L[i]
    if R[i] < borderR :
        borderR = R[i]

if borderR < borderL :
    print(0)
else :
    print(borderR - borderL + 1)
