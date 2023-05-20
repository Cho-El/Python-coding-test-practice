def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    box = []
    for s in score:
        box.append(s)
        if len(box) == m:
            answer += min(box) * m
            box = []
    
    return answer