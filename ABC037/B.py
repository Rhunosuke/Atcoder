n, q = map(int, input().split())
a = [0] * n
for _ in range(q) :
    l, r, t = map(int, input().split())
    a[l-1:r] = [t for _ in range(r-l+1)]

print(*a,sep='\n')
