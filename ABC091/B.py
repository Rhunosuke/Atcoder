s = [input() for _ in range(int(input()))]
t = [input() for _ in range(int(input()))]

print(max(0, max(s.count(s[i]) - t.count(s[i]) for i in range(len(s)))))
