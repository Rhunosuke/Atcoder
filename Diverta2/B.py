N = int(input())

l = []
for _ in range(N) :
    ll = list(map(int, input().split()))
    l.append(ll)

#print(l)

dic = {}

for i in range(N) :
    for j in range(N) :
        if i == j :
            continue

    #subl.append([l[i][0] - l[i-1][0], l[i][1] - l[i-1][1]])
    #k = 1000000001*(l[i][0] - l[i-1][0]) + l[i][1] - l[i-1][1]
    k = str(l[i][0] - l[i-1][0]) + '+' + str(l[i][1] - l[i-1][1])

    if l[i][0] - l[i-1][0] == 0 and l[i][1] - l[i-1][1] == 0:
        continue

    if k not in dic :
        dic[k] = 1
    else :
        dic[k] += 1

#print(dic)

if len(dic) == 0 :
    print(N)
else :
    print(N - max(dic.values()))
