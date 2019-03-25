words = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(len(words)) :
    words[i] = words[i][::-1]

S = input()[::-1]

ans = True

i = 0

while True :
    flag = False
    for w in words :
        if S[i:i + len(w)] == w :
            i += len(w)
            flag = True
            break
    if flag == False:
        ans = False
        break
    if i == len(S) :
        break

if ans :
    print('YES')
else :
    print('NO')
