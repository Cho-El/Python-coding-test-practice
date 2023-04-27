def solution(storey):
    answer = 0
    while storey > 0:
        firstNum = storey % 10
        if firstNum > 5:
            storey //= 10
            storey += 1
            answer += 10 - firstNum
        elif firstNum == 5:
            nextNum = storey // 10
            answer += firstNum
            if nextNum % 10 >= 5:
                storey //= 10
                storey += 1
            else:
                storey //= 10
        else:
            storey //= 10
            answer += firstNum
            
    return answer

def solution1(storey):
    answer = 0
    while storey > 0:
        firstNum = storey % 10
        if firstNum > 5:
            storey //= 10
            storey += 1
            answer += 10 - firstNum
        elif firstNum == 5:
            nextNum = storey // 10
            nextNum += 1
            answer += firstNum
            if nextNum % 10 > 5:
                storey //= 10
                storey += 1
            else:
                storey //= 10
        else:
            storey //= 10
            answer += firstNum
            
    return answer

def solution2(storey):
    answer = 0
    while storey > 0:
        storey, moves = divmod(storey, 10)
        if moves > 5 or (moves == 5 and storey % 10 >= 5):
            moves = 10 - moves
            storey += 1
        answer += moves
    return answer

print(solution(75))
print(solution(965))
print(solution(45))
