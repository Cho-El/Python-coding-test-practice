import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
S = 0

while a:
    min_a = min(a)
    max_b = max(b)
    S += min_a * max_b
    a.pop(a.index(min_a))
    b.pop(b.index(max_b))

print(S)