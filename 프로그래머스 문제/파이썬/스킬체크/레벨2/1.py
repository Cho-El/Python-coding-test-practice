def solution(n):
    arr = [i for i in range(1,n+1)]
    end = 0
    now_sum = 0
    cnt = 0
    for start in range(0,len(arr)):
        while now_sum < n and end < len(arr):
            now_sum += arr[end]
            end += 1
        if now_sum == n:
            cnt += 1
        now_sum -= arr[start]
    
    return cnt

print(solution(6))