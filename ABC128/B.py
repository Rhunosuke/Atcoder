N = int(input())

l = []

for i in range(N) :
    a, b = map(str, input().split())
    b = int(b)
    l.append([a, b, i+1])

l = sorted(l, key=lambda x:(x[0],-x[1]))

for i in range(len(l)) :
    print(l[i][2])
