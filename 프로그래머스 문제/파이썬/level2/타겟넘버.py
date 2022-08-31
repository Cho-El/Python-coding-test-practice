# def solution2(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == n:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx+1, result+numbers[idx])
#             dfs(idx+1, result-numbers[idx])
#     dfs(0,0)
#     return answer

# answer = 0
# def dfs(idx, v, numbers, target):
#     global answer
#     n = len(numbers)
#     if n == idx and target == v:
#         answer += 1
#         return
#     if n == idx:
#         return
    
#     dfs(idx + 1, v - numbers[idx], numbers, target)
#     dfs(idx + 1, v + numbers[idx], numbers, target)

# def solution(numbers, target):
#     global answer
#     dfs(0,0,numbers,target)
#     return answer
def dfs(numbers, target,idx, l_num, sum_n):
    global answer
    if idx == l_num and target == sum_n:
        answer += 1
        return
    if idx == l_num:
        return
    
    sum_n += numbers[idx]
    dfs(numbers, target, idx + 1, l_num, sum_n)
    sum_n -= 2 * numbers[idx]
    dfs(numbers, target, idx + 1, l_num, sum_n)
def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers,target,0,len(numbers),0)
    return answer
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))