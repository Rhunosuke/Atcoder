N = int(input())

nList = [i + 1 for i in range(N)]
res = -1
counter = -1
for n in nList :
    count = 0
    buf = n
    while buf % 2 == 0 :
        count += 1
        buf = buf / 2
    if counter < count :
        counter  = count
        res = n
print(res)
