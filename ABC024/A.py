a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
print(a*s + b*t - c*(s+t)*(s+t >= k))
