import copy
MAX_SCORE_DIFF = 0
answers = []
# 라이언과 어피치의 점수 차이를 계산하는 함수
def calcScoreDiff(info, myshots):
    enemyScore, myScore = 0, 0
    for i in range(11):
        if (info[i], myshots[i]) == (0, 0):
            continue
        if info[i] >= myshots[i]:
            enemyScore += (10 - i)
        else:
            myScore += (10 - i)
    return myScore - enemyScore
    
def dfs(info, myshots, n, i): # 어피치, 라이언, 화살의 갯수 ,depth
    global MAX_SCORE_DIFF, answers
    if i == 11:
        if n != 0: # 0점까지 왔는데 화살이 남아있을 때
            myshots[10] = n
        scoreDiff = calcScoreDiff(info, myshots)
        if scoreDiff <= 0: # 
            return
        result = copy.deepcopy(myshots)
        if scoreDiff > MAX_SCORE_DIFF:
            MAX_SCORE_DIFF = scoreDiff
            answers = [result]
            return
        if scoreDiff == MAX_SCORE_DIFF:
            answers.append(result)
        return

    # 점수 먹는 경우
    if info[i] < n:
        myshots.append(info[i] + 1)
        dfs(info, myshots, n - info[i] - 1, i + 1)
        myshots.pop()

    # 점수 안먹는 경우
    myshots.append(0)
    dfs(info, myshots, n, i + 1)
    myshots.pop()

def solution(n, info):
    global MAX_SCORE_DIFF, answers
    dfs(info, [], n, 0)
    if answers == []:
        return [-1]
    answers.sort(key = lambda x : x[::-1], reverse=True)
    return answers[0]

if __name__ == '__main__':
    a = [(5, [2,1,1,1,0,0,0,0,0,0,0]), (1,[1,0,0,0,0,0,0,0,0,0,0]),(9,[0,0,1,2,0,1,1,1,1,1,1]),(10,	[0,0,0,0,0,0,0,0,3,4,3])]
    for i in a:
        n, info = i
        print(solution(n, info))