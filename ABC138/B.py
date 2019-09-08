def calc_reverse(n):
    return n ** (-1)

n = int(input())
a = [int(inp) for inp in input().split()]
*a, = map(calc_reverse, a)
print(sum(a) ** (-1))
