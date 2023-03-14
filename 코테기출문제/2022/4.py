def solution(estimates,k):
    result = 0
    for i in range(len(estimates) - k + 1):
        sumEstimates = 0
        for j in range(k):
            sumEstimates += estimates[i + j]
        if sumEstimates > result:
            result = sumEstimates
    return result

print(solution([5,1,9,8,10,5],3))
print(solution([10,1,10,1,1,4,3,10],6))