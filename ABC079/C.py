ABCD = input()

A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])

o1 = '+'
o2 = '+'
o3 = '+'
flag = False
for j in range(2) :
    if j % 2 == 0 :
        B2 = -B
        o2 = '-'
    else :
        B2 = B
        o2 = '+'
    for k in range(2) :
        if k % 2 == 0 :
            C2 = -C
            o3 = '-'
        else :
            C2 = C
            o3 = '+'
        for l in range(2) :
            if l % 2 == 0 :
                D2 = -D
                o4 = '-'
            else :
                D2 = D
                o4 = '+'
            if A+B2+C2+D2 == 7 :
                #print(B2, C2, D2 , o2, o3 ,o4)
                flag = True
                break
        if flag :
            break
    if flag :
        break
ans = str(A) + o2 + str(B) + o3 + str(C) + o4 + str(D) + '=7'
print(ans)
