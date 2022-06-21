# 그리디 DP
import sys
import copy
sys.setrecursionlimit(10**7)

def solution(alp, cop, problems):
    global answer
    alg_goal = max(problems, key = lambda x:x[0])[0]
    co_goal = max(problems, key = lambda x:x[1])[1]
    start_alg = min(problems, key = lambda x:x[0])[0]
    start_co = min(problems, key = lambda x:x[1])[1]
    time = 0


    if alp < start_alg:
        time += start_alg - alp
    if cop < start_co:
        time += start_co -cop
    
    dfs(alg_goal, co_goal,problems, start_alg, start_co, time)
    return answer

if __name__ == '__main__':
    a = [(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])]
    for i in a:
        a, c, p = i
        print(solution(a,c,p))