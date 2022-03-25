'''
트리는 그래프의 일종으로, 사이클이 없는 것이 특징이다.

즉, 방문 체크를 하지 않고 DFS 혹은 BFS를 완전히 수행할 수 있다.
'''
# 1번 풀이----------------------------------
import sys
n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

def dfs(k, tree):
    tree[k] = -2
    for i in range(n):
        if k == tree[i]:
            dfs(i,tree)

dfs(k,tree)

cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)

# 2번 풀이----------------------------------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)
n = int(input())
graph = list(map(int,input().split()))
del_node = int(input())
cnt = 0
tree = [[] for _ in range(n+2)]

for i in range(n):
    if graph[i] == -1:
        tree[n+1].append(i)
    else:
        tree[graph[i]].append(i)

def dfs(x):
    global cnt
    if len(tree[x]) == 0:
        cnt += 1
        return cnt
    for in range 


# 3번 풀이----------------------------------
n = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = {}

for i in range(n):
    if i == del_node or parents[i] == del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)
    else:
        tree[parents[i]] = [i]

res = 0
if -1 in tree:
    q = [-1]
else:
    q = []

while q:
    node = q.pop()
    if node not in tree:
        res += 1
    else:
        q += tree[node]

print(res)