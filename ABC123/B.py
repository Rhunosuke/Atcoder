num = []
m = 10
for _ in range(5) :
    n = int(input())
    if n % 10 == 0 :
        num.append(n)
        continue
    num.append(n + 10 - (n % 10))
    m = min(m, n % 10)

print(sum(num) - 10 + m)
