# 그리디 DP
import sys
import copy
sys.setrecursionlimit(10**7)
result_problem = [] # 도달할 수 있는 경우들 시간
answer = sys.maxsize

def find_possible_solve(cur_alp, cur_cop, problems): # 풀 수 있는 문제 찾기
    temp = []
    for i in range(len(problems)):
        if problems[i][0] <= cur_alp and problems[i][1] <= cur_cop:
            temp.append(i)
    return temp

def find_next_level_problem(problems, cur_alp, cur_cop, possible_solve):
    alg = []
    cop = []
    result = []
    for i in range(len(problems)):
        if i not in possible_solve:
            if problems[i][0] <= cur_alp: # 알고리즘 능력만 충족하는경우
                dif = problems[i][1] - cur_cop # 코딩 능력의 차이값
                cop.append(dif)
            elif problems[i][1] <= cur_cop: # 코딩 능력만 충족하는 경우
                dif = problems[i][0] - cur_alp # 알고리즘 능력의 차이값
                alg.append(dif)
    
    

    if not alg and not cop:
        return result

    if alg:
        result.append(min(alg))
    else:
        result.append(-1)
    if cop:
        result.append(min(cop))
    else:
        result.append(-1)

    return result



def dfs(alg_goal, co_goal, problems, cur_alp, cur_cop, time): # 현재 algo 점수와 코딩 점수
    global answer
    possible_solve = find_possible_solve(cur_alp,cur_cop,problems)
    # possible_solve.append(101) # 그냥 문제 풀이 없이 코딩력을 기르는 경우를 추가
    # possible_solve.append(102) # 그냥 문제 풀이 없이 코딩력을 기르는 경우를 추가
    
    if alg_goal <= cur_alp and co_goal <= cur_cop: # 목표치에 도달하면 종료
        answer = min(answer, time)
        # 알고를 먼저 도달한 경우
        # 코딩을 먼저 도달한 경우
        return

    for ps in possible_solve: # 풀이가 가능한 문제들 모두 풀어보기
        cur_alp += problems[ps][2]
        cur_cop += problems[ps][3]
        time += problems[ps][4]
        
        dfs(alg_goal, co_goal, problems, cur_alp, cur_cop, time)
        cur_alp -= problems[ps][2]
        cur_cop -= problems[ps][3]
        time -= problems[ps][4]

                
            


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