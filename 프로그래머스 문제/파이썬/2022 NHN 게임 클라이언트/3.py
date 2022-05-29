from collections import deque
def bfs(start, possible):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([start])
    n = len(visited[0])
    m = len(visited)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0<= ny < n and graph[nx][ny] in possible and visited[nx][ny] == 1:
                visited[nx][ny] = visited[nx][ny] + visited[x][y]
                q.append((nx,ny))
            

def solution(maze, queries):
    global visited, graph
    answer = []
    graph = []
    for m in maze:
        graph.append(list(m))
    
    
    for q in queries:
        visited = [[1 for _ in range(len(graph[0]))] for _ in range(len(graph))]
        A, B, C, D, E = q.split(' ')
        visited[int(A) - 1][int(B) - 1] = 1
        bfs((int(A) - 1,int(B) - 1), list(E))
        if visited[int(C) - 1][int(D) - 1] != 1:
            answer.append(visited[int(C) - 1][int(D) - 1])
        else:
            answer.append(-1)
    
    return answer
        
        

if __name__ == '__main__':
    maze = [["AAAAA", "AABBB", "CAEFG", "AAEFF"], ["AAA", "ABB", "ABA"]]
    queries = [["1 1 1 5 AF", "1 1 4 5 AF", "2 1 4 5 FAE", "1 5 4 5 ABF", "1 1 4 1 A"], ["1 1 1 3 A", "1 3 3 1 A", "1 1 3 3 A", "1 1 3 3 AB"]]
    for maze, queries in zip(maze, queries):
        print(solution(maze, queries))