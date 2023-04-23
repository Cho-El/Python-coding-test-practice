def solution(scores):
    answer = 0
    wonHo = scores[0]
    scores.sort(key = lambda x : [-x[0], x[1]])
    leavePerson = []
    while scores:
        score = scores.pop()
        if not leavePerson:
            leavePerson.append(score)
        else:
            if leavePerson[-1][0] != score[0]:
                while leavePerson and leavePerson[-1][1] < score[1]:
                    leavePerson.pop()
            leavePerson.append(score)
    
    if wonHo not in leavePerson:
        return -1
    
    leavePerson.sort(key = lambda x : sum(x), reverse = True)
    rank = 1
    end = leavePerson.index(wonHo)
    for p in leavePerson[:end]:
        if sum(wonHo) < sum(p):
            rank += 1
    return rank

print(solution([[1,2],[2,3]]))
print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
print(solution([[2,2],[2,3],[2,2]]))
print(solution([[4,3],[2,3],[4,4],[5,5],[6,2]]))