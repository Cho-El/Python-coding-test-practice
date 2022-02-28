def solution2(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer

answer = 0
def dfs(idx, v, numbers, target):
    global answer
    n = len(numbers)
    if n == idx and target == v:
        answer += 1
        return
    if n == idx:
        return
    
    dfs(idx + 1, v - numbers[idx], numbers, target)
    dfs(idx + 1, v + numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    dfs(0,0,numbers,target)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))