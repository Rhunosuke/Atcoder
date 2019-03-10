A, B, C = map(int, input().split())

n = min(A, B)
count = 0
for i in range(n) :
    if A % (n - i) == 0 and B % (n - i) == 0 :
        count += 1
        if count == C :
            print(n - i)
