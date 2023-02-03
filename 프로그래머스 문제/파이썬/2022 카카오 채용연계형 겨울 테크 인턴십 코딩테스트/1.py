def solution(x,y,z):
    max_result = max(x,y)
    distance = abs(x-y)
    if distance > z:
        return -1
    else:
        leftMove = z - distance
        if leftMove % 2 == 0:
            max_result += leftMove // 2
        else:
            max_result += (leftMove - 1) // 2
    return max_result

# x = int(input().strip())
# y = int(input().strip())
# z = int(input().strip())

print(solution(100000000,99999998,12))