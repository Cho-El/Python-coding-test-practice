'''
www.acmicpc.net/problem/11657
벨만포드 알고리즘
특징
- 음수 간선의 순환을 감지
- 벨만 포드의 기본 시간 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느리다.

음수 간선 최단 경로 문제
1) 모든 간선이 양수인 경우
2) 음수 간선이 있는 경우
    1) 음수 간선 순환은 없는 경우
    2) 음수 간선 순환이 있는 경우

벨만포드 알고리즘의 동작과정
1. 출발 노드 설정
2. 최단 거리 테이블을 초기화
3. 다음의 과정을 N-1번 반복
    1) 간선 E개를 하나씩 확인
    2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신

여기서 왜 N-1번 반복해야될까?
a에서 c에 이르는 최단경로는 a에서 b까지의 최단경로에 b에서 c 사이의 가중치를 더한 값이다.
D(a,c) = D(a,b) + cost(b,c)
근데 여기서 a, b 사이의 최단 경로는 a에서 바로 b로 가는 것으로 끝날 수도 있지만, b를 제외한 그래프
의 모든 노드들이 a,b 사이의 최단경로를 구성할 수 도 있다. 그러하기에 b를 제외한 총 노드의 갯수 - 1회
수행하여야 한다.

만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행합니다.
 - 이 때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것입니다.
'''
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input())
edges = [] # 간선 정보
dist = [INF] * (n + 1) # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node == edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:
                    return True

    return False
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
