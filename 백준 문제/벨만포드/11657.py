'''
음수 간선이 포함된 상황에서의 최단 거리 문제
벨만 포드 필요한 것들
최단거리 테이블, edge 저장
'''
import sys
INF = sys.maxsize
input = sys.stdin.readline
edges = []
def bf(start,n,m):
    global dist
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            start, end, cost = edges[j][0], edges[j][1], edges[j][2]
            if dist[start] != INF and dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost
                # 음수 간선 순회 확인
                if i == n - 1:
                    return False
    
    return True

def solution(edges,n,m):
    global dist
    dist = [INF] * (n + 1)
    if bf(1,n,m):
        for i in range(2,n+1):
            if dist[i] == INF:
                print(-1)
            else:
                print(dist[i])

    else:
        print(-1)

if __name__ == '__main__':
    n,m = map(int, input().split())
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a,b,c))
    solution(edges,n,m)