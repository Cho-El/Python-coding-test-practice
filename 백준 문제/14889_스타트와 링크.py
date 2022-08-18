#
import sys
input = sys.stdin.readline
MAX = sys.maxsize
n = int(input())
score = []
visited = [False for _ in range(n)]
team = [i for i in range(n)]
result = MAX

for i in range(n):
    score.append(list(map(int, input().split())))

# def cal_score(t1):
#     t2 = []
#     score1 = 0
#     score2 = 0
#     for i in team:
#         if not visited[i]:
#             t2.append(i)
            
#     for i in range(0, len(t1) - 1):
#         for j in range(i + 1, len(t1)):
#             score1 += score[t1[i]][t1[j]]
#             score1 += score[t1[j]][t1[i]]
    
#     for i in range(0, len(t2) - 1):
#         for j in range(i + 1, len(t2)):
#             score2 += score[t2[i]][t2[j]]
#             score2 += score[t2[j]][t2[i]]
    
#     return abs(score1 - score2)
    
    
    
    
def dfs(depth,idx):
    global n, result
    if depth == n//2:
        score1, score2 = 0, 0
        for i in range(n-1):
            for j in range(i + 1,n):
                if visited[i] and visited[j]:
                    score1 += score[i][j]
                    score1 += score[j][i]
                elif not visited[i] and not visited[j]:
                    score2 += score[i][j]
                    score2 += score[j][i]
                
        result = min(result, abs(score1 - score2))
        
    
    for i in range(idx, len(visited)):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False
         
dfs(0,0)
print(result)