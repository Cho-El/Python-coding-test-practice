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

def solution(S):
    n = len(S)
    max_length = 0

    def search_symmetric(i, j):
        nonlocal max_length
        if i >= 0 and j < n:
            if S[i] in {'<', '?'} and S[j] in {'>', '?'}:
                max_length = max(max_length, j - i + 1)
                search_symmetric(i - 1, j + 1)

    for i in range(n):
        search_symmetric(i, i + 1)

    return max_length

print(solution("<><??>>")) # Should return 4
print(solution("??????"))  # Should return 6
print(solution("<<?"))     # Should return 2
print(solution("<<????"))  # Should return 6
print(solution("<<<?<??>><")) # Should return 8
print(solution("???<>>?<?")) # should return 6