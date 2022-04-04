import sys
sys.setrecursionlimit
n,m = map(int, input().split())
rs = []
check = [False] * (n + 1)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, n + 1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(num + 1)
            check[i] = False
            rs.pop()

recur(0)
