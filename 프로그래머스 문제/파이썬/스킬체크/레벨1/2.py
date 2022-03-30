def solution(arr):
    if len(arr) == 1:
        return -1
    else:
        arr.pop(arr.index(min(arr)))
        return arr
arr = [2,4,6,1]
print(solution(arr))