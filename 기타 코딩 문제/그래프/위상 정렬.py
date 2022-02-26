'''
위상 정렬
사이클이 없는 방향 그래프(DAG)의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미합니다.

진입 차수(Indegree) : 특정한 노드로 들어오는 간선의 개수
진출 차수(Outdegree) : 특정한 노드에서 나가는 간선의 개수

위상 정렬 알고리즘 -> dfs나 큐를 이용해 구현 가능

큐를 이용하는 위상 정렬 알고리즘의 동작 과정은 다음과 같습니다.
1. 진입차수가 0인 모든 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다읨의 과정을 반보한다.
 1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
 2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
 -> 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같습니다.

성능 분석
위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거해야 합니다.
 - 위상 정렬 알고리즘의 시간 복잡도는 O(V + E)입니다.
'''
from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1 # 진입 차수 1 증가

def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end = ' ')

# topology_sort()/

visited = [False] * (v + 1)

def dfs(result, start):
    if not visited[start]:
        visited[start] = True
        for i in graph[start]:
            dfs(result,i)
        result.append(start)
    else:
        return

def topology_sort_dfs():
    result = []
    for i in range(1, v + 1):
        dfs(result, i)
    result.reverse()
    
    for i in result:
        print(i, end = ' ')
topology_sort_dfs()