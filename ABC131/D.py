N = int(input())
AB = []
for _ in range(N) :
    AB.append(list(map(int, input().split())))

AB = sorted(AB, key=lambda x: x[1])

time = 0
ans = True

for i in range(N) :
    time += AB[i][0]
    if time > AB[i][1] :
        ans = False
        break

if ans :
    print('Yes')
else :
    print('No')
