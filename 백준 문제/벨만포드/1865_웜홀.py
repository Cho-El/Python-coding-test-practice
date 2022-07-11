# 벨만포드
# INF와 float('inf')는 다르다?
# 초깃값을 무한대로 하면 무한대 값에서 음수 가중치를 더해주어도 그대로 무한대이기 때문에
# 현재값과 그 전의 값이 비교가 되지 않아서 가중치 값이 갱신되지 않은 것이었다..!

import sys
input = sys.stdin.readline
tc = int(input())
INF = sys.maxsize


def bford(start):
    INF = sys.maxsize
    distance = [INF] * (n + 1)
    
    for i in range(n): # 노드의 개수 원래는 n-1만큼이지만 음의 사이클 확인을 위해 
        for u,v,w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w 
                if i == n - 1: # 음의 사이클 확인
                    return True     
    return False

for _ in range(tc):
    n,m,w = map(int, input().rstrip().split())
    edges = []
    
    for _ in range(m):
        a,b,c = map(int, input().rstrip().split())
        edges.append((a,b,c))
        edges.append((b,a,c))
        
    for _ in range(w):
        a,b,c = map(int, input().rstrip().split())
        edges.append((a,b,-c))
    
    if bford(1): # 음의 사이클이 있는경우
        print('YES')
    else:
        print('NO')

    