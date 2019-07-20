N = int(input())
a = []
for i in range(N) :
    a.append(int(input()))

index = 1
cnt = 0

for i in range(N):
    index = a[index - 1]
    cnt += 1
    if index == 2 :
        break
    if index == 1 :
        cnt = -1
        break
    if i == N - 1 :
        cnt = -1

print(cnt)
