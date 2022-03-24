# import sys
# n = int(sys.stdin.readline())
# tree = list(map(int, sys.stdin.readline().split()))
# k = int(sys.stdin.readline())

# def dfs(k, tree):
#     tree[k] = -2
#     for i in range(n):
#         if k == tree[i]:
#             dfs(i,tree)

# dfs(k,tree)

# cnt = 0
# for i in range(n):
#     if tree[i] != -2 and i not in tree:
#         cnt += 1

# print(cnt)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)
n = int(input())
graph = list(map(int,input().split()))
del_node = int(input())

tree = [[] for _ in range(n+2)]
for i in range(n):
    if graph[i] == -1:
        tree[n+1].append(i)
    else:
        tree[graph[i]].append(i)

print(tree)
