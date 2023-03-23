def solution(S):
    lenS = len(S)
    answer = 1
    for i in range(len(S) - 1):
        start = i
        end = i + 1
        cntPalin = 0
        while 0 <= start < len(S) and 0 <= end < len(S):
            if S[start] == S[end]:
                cntPalin += 2
                start -= 1
                end += 1
            else:
                break
        answer = max(answer, cntPalin)
                
    for i in range(len(S) - 2):
        start = i
        end = i + 2
        cntPalin = 1
        while 0 <= start < len(S) and 0 <= end < len(S):
            if S[start] == S[end]:
                cntPalin += 2
                start -= 1
                end += 1
            else:
                break
        answer = max(answer, cntPalin)
        
    return answer

print(solution("abcdcba"))
print(solution("abacde"))
print(solution("a"))
print(solution("ab"))
print(solution("aba"))