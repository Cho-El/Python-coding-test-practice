# 트리 만들기 1
n = int(input())
parents = list(map(int, input().split()))
tree = {}

for i in range(n):
    if parents[i] in tree:
        tree[parents[i]].append(i)
    else:
        tree[parents[i]] = [i]

# 트리 만들기 2
