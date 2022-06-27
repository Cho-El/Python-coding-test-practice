# 분리집합 
# 실수 조심
# 진실만을 아는 set을 만들 때 find함수를 안쓰고 그냥 parent의 값으로 하였는데 이 경우 부모가 갱신되지 않는 경우가 있으니 주의해야한다.

import sys
input = sys.stdin.readline
n,m = map(int, input().split())

parent = []
for i in range(n + 1):
    parent.append(i)

# 아는 사람 체크
temp = list(map(int, input().split()))
for t in temp[1:]:
    parent[t] = 0

def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    x = find_parent(x)
    y = find_parent(y) 
    if x < y :
        parent[y] = x
    else:
        parent[x] = y

graph = []
for _ in range(m):
    temp = list(map(int, input().split()))
    graph.append(temp[1:])
    if len(temp) == 2:
        continue
    else:
        start = temp[1]
        for t in temp[2:]:
            union(start, t)

# 진실만을 들어야하는 set
true_team = []
for i in range(len(parent)):
    if find_parent(i) == 0:
        true_team.append(i)

result = 0
for g in graph:
    for v in g:
        if v in true_team:
            break
    else:
        result += 1

print(result)