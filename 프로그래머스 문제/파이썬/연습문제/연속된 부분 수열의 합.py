def solution(sequence, k):
    start = 0
    end  = 0
    lenS = len(sequence)
    sumS = 0
    resultTemp = []
    while start < lenS or end < lenS:
        if sumS < k and end == lenS:
            break
        if sumS == k: # 같은 경우 해당 인덱스를 저장
            resultTemp.append([start, end - 1])
            sumS -= sequence[start]
            start += 1
        elif sumS < k:
            sumS += sequence[end]
            end += 1
        else:
            sumS -= sequence[start]
            start += 1
        
    
    resultTemp.sort(key = lambda x : [x[1] - x[0], x[0]])
    return resultTemp[0]

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
