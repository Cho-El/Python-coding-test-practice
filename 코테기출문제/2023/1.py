from collections import defaultdict
from copy import deepcopy
def solution(K, user_scores):
    result = 0
    # 정렬 조건
    # 점수가 높은 순
    # 점수가 같다면 점수를 먼저 달성한 유저의 랭킹
    
    ranking = [] # ranking 표 이름만
    scoreList = {}
    for pk, u in enumerate(user_scores):
        nickname, score = u.split()
        score = int(score)
        # 유저 점수표에 넣는다.
        # 해당 유저가 딕셔너리 안에 있는지 체크
        # 없는 경우
        if nickname not in scoreList:
            scoreList[nickname] = [score,pk]
        # 있는 경우
        else:
            # 기존에 있던 점수와 비교
            # 기존 것보다 큰경우
            if scoreList[nickname][0] < score:
                scoreList[nickname] = [score, pk]
            # 작은 경우는 무시
        
        # 정렬하기
        sortedScoreList = sorted(scoreList.items(), key = lambda x : [-x[1][0],x[1][1]])
        temp = []
        for i in sortedScoreList[:K]:
            temp.append(i[0])
        
        # 랭킹등수가 업데이트가 된다면 result 한 개 올리기
        if ranking != temp:
            result += 1
        ranking = deepcopy(temp)
        
        
    return result

print(solution(3, ["al 100", "ch 200", "co 150", "lu 100", "al 120", "co 300", "ch 110"]))
print(solution(3, ["al 100", "ch 200", "al 200", "ch 150", "co 50", "co 200"]))
print(solution(2, ["ch 200", "al 100", "co 150", "pu 120"]))
