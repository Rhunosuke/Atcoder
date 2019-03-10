A, B = map(int, input().split())

ans = 0
buf = A
ans = A
print(bin(A))
print(len(bin(A)) - 2)

while buf < B :
    ans = ans ^ (buf + 1)
    buf += 1

print(ans)

map(int, input().split())
