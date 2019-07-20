S = input()
count = 0

for s in S :
    if s == "o" :
        count += 1



if count >= len(S) - 7 :
    print('YES')
else :
    print('NO')
