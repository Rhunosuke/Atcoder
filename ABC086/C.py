N = int(input())

T = [0]
X = [0]
Y = [0]


for i in range(N) :
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)
#print(T, X, Y)

judge = True

for i in range(1, N + 1) :
    if T[i] - T[i-1] >= abs(X[i] - X[i-1]) + abs(Y[i] - Y[i-1]) :
        if (T[i] - T[i-1] - (abs(X[i] - X[i-1]) + abs(Y[i] - Y[i-1]))) % 2 == 0 :
            #print('test')
            continue
    judge = False
    break

if judge :
    print('Yes')
else :
    print('No')
