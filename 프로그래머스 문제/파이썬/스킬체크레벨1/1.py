def solution(n):
    temp = list(str(n))
    result = []
    while temp:
        a = temp.pop()
        result.append(int(a))
    return result

print(solution(23678))