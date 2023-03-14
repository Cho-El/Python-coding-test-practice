def solution(S, interval):
    for start, end in interval:
        startIdx = start - 1
        endIdx = end - 1
        temp = S[startIdx:endIdx + 1]
        S = S[:startIdx] + temp[::-1] + S[endIdx + 1:]
    return S

print(solution('abcde',[[1,3],[1,4],[4,5]]))