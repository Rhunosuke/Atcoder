slist = []
plist = []

for _ in range(int(input())) :
    s, p = input().split()
    slist.append(s)
    plist.append(int(p))

print(slist[plist.index(max(plist))] if max(plist) > sum(plist) // 2 else 'atcoder')
