def solution(t, p):
    answer = 0
    target = int(p)
    for i in range(len(t) - len(p) + 1):
        comp = t[i:i + len(p)]
        if int(comp) <= target:
            answer += 1
        
    return answer

print(solution("3141592","271"))
print(solution("500220839878","7"))
print(solution("10203","15"))
