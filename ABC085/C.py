N, Y = map(int, input().split())

flag = False

for i in range(N + 1) :
    for j in range(N + 1 - i) :
        k = N - i - j
        if 10000 * i + 5000 * j + 1000 * k == Y :
            print(i, j, k)
            flag = True
            break
    if flag == True :
        break

if flag == False :
    print(-1, -1, -1)
