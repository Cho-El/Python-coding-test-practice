def solution(S):
    result = 0
    
    for i in range(len(S) - 1):
        start = i
        end = i + 1
        while 0 <= start < len(S) and 0 <= end < len(S):
            if S[start] in {'<','?'} and S[end] in {'>','?'}:
                result = max(result, end - start + 1)
                start -= 1
                end += 1
            else:
                break
        
    return result

print(solution("<><??>>"))
print(solution("<<?"))