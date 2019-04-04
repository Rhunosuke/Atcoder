N = int(input())

dic = {}

for i in range(N) :
    str = input()
    if str in dic :
        dic[str] += 1
    else :
        dic[str] = 1

cnt = 0

for e in dic.values() :
    if e % 2 != 0 :
        cnt += 1

print(cnt)
