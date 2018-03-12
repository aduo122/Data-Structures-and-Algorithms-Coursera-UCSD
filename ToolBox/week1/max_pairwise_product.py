# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

m1 = max(a)
a.remove(m1)
m2 = max(a)
result = m1*m2


print(result)
