def solution(cost, x):
    costRate = []
    result = 0
    
    for (idx,c) in enumerate(cost):
        costRate.append([2**idx/c, 2**idx, c])
    costRate.sort(reverse = True)
    for r in costRate:
        if x >= r[2]:
            x -= r[2]
            result += r[1]
        else:
            continue
        if x <= 0:
            break
        
    return result

print(solution([19,78,27,18,20],25))