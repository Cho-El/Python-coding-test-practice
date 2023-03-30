def solution(keymap, targets):
    answer = []
    keyboard = {}
    for k in keymap:
        for idx, s in enumerate(list(k)):
            if s not in keyboard:
                keyboard[s] = idx + 1
            else:
                keyboard[s] = min(keyboard[s], idx + 1)
    
    for t in targets:
        result = 0
        for s in t:
            if s in keyboard:
                result += keyboard[s]
            else:
                result = -1
                break
        answer.append(result)
    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))
