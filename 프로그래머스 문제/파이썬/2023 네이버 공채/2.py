from collections import deque
def solution(n,k):
    answer = 0\
    
    return answer

def dfs(array,k):
    array.sort(reverse = True)
    tempArray = []
    while array:
        num = array.pop()
        if num > k:
            addArray = [num - k, k]
            dfs(array + addArray ,k)
    
print(solution(7,3))