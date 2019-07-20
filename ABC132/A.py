S = input()

str = ""

dic = {}

for s in S :
    str = s
    if s not in dic :
        dic[s] = 1
    else :
        dic[s] += 1

if len(dic) == 2 and dic[str] == 2 :
    print('Yes')
else :
    print('No')
