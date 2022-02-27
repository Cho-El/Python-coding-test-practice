def solution2(n, lost, reserve):
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    for reserve_person in reserve_set: 
        if reserve_person-1 in lost_set: 
            lost_set.remove(reserve_person-1) 
        elif reserve_person+1 in lost_set: 
            lost_set.remove(reserve_person+1) 
    
    return n-len(lost_set)

n = 5
lost = [1,2,3,4,5]
reserve = [1]
def solution(n, lost, reserve):
    result = 0
    shirt = [1] * (n+1)
    for l in lost:
        shirt[l] -= 1
    for r in reserve:
        shirt[r] += 1
    
    for i in range(1,n+1):
        if shirt[i] == 0:
            if i >= 2 and shirt[i-1] == 2:
                shirt[i] += 1
                shirt[i-1] -= 1
            elif i+1 <= n and shirt[i + 1] == 2:
                shirt[i] += 1
                shirt[i+1] -= 1

    for i in shirt:
        if i != 0:
            result += 1
    return result - 1

print(solution(n, lost, reserve))