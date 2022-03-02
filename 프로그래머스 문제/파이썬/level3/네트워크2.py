def dfs(start,computers):
    computers[start][start] = 2 # 방문
    for i in range(len(computers[start])): # 돌면서 체크
        if computers[i][i] != 2 and computers[start][i] == 1:
            dfs(i, computers)



def solution(n, computers):
    answer = 0
    for i in range(n):
        if computers[i][i] == 1:
            dfs(i,computers)
            answer += 1
    return answer

n = 3
computers =	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]


from collections import deque
def bfs(start,computers):
    q = deque([start])

    while q:
        s = q.popleft()
        computers[s][s] = 2
        for i in range(len(computers[s])):
            if computers[i][i] != 2 and computers[s][i] == 1:
                q.append(i)

def solution2(n, computers):
    answer = 0
    for i in range(n):
        if computers[i][i] == 1:
            bfs(i,computers)
            answer += 1
    return answer

print(solution2(n,computers))