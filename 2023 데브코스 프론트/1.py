def solution(record):
    answer = 0
    result = 0
    for r in record:
        result += r
        if result < 0:
            answer += 1
    return answer

print(solution([1100,-500,-800,200,400,57,-458,-1000,1001]))
print(solution([-100,100,-100,100]))