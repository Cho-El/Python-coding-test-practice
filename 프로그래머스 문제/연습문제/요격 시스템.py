def solution(targets):
    answer = 1
    targets.sort(key = lambda x : [x[1],x[0]])
    start = targets[0][1]
    
    for i in range(1,len(targets)):
        if targets[i][0] < start:
            continue
        answer += 1
        start = targets[i][1]
        
    return answer