N = int(input())
d = list(map(int, input().split()))

dic = {}

for e in d :
    if e not in dic :
        dic[e] = 1
    else :
        dic[e] += 1

dic = sorted(dic.items(), key=lambda x:x[0])

#print(dic)

sum = 0
ancker = 0
tmp = 0
ans = True

for i in range(len(dic)):
    sum += dic[i][1]
    if sum == N / 2 :
        ancker = i
        break;
    if sum > N / 2 :
        ans = False
        break
#print(ancker)

if not ans :
    print(0)
else :
    print(dic[ancker+1][0] - dic[ancker][0])
