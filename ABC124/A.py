A, B = map(int, input().split())

ans = 0

for i in range(2) :
    if max(A, B) == A :
        ans += A
        A -= 1
    else :
        ans += B
        B -= 1

print(ans)
