import sys
from itertools import combinations as com
t = int(input())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())

    list_m = [i for i in range(m)]
    result = len(list(com(list_m, n)))
    print(result)
