num = []

for _ in range(5) :
    num.append(int(input()))

k = int(input())
ans = True

for i in range(5) :
    for l in range(i + 1, 5) :
        if num[l] - num[i] > k :
            ans = False

if ans :
    print('Yay!')
else :
    print(':(')
