N = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

for i in range((len(a) + 1 )// 2) :
    alice += max(a)
    a.remove(max(a))
    if len(a) != 0 :
        bob += max(a)
        a.remove(max(a))
print(alice - bob)
