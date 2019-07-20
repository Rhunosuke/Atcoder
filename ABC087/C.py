N = int(input())
A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

total = []

for i in range(N) :
    total.append(sum(A[0][0:i+1]) +sum(A[1][i:N]))

print(max(total))
