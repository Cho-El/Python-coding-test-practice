def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = []
    for i in range(len(numbers)):
        if not stack or numbers[i] <= stack[-1][1]:
            stack.append([i, numbers[i]])
        else:
            while stack and numbers[i] > stack[-1][1]:
                a, b = stack.pop()
                answer[a] = numbers[i]
            stack.append([i, numbers[i]])
        
    return answer

print(solution([2,3,3,5]))
print(solution([9, 1, 5, 3, 6, 2]))
print(solution([2,2,2,2,2]))
print(solution([9,8,4,3,2]))
print(solution([5,4,4,7,8,9,9,3,10,11,8]))
print(solution([9,9,9,1,1,1,7,7,7,4,4,4,10]))