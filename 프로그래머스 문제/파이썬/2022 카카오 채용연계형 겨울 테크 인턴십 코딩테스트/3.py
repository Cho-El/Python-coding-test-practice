def solution(box):
    maxBox = max(box)
    if maxBox == box[0]:
        return box[0]
    start, end = 0, maxBox
    answer = maxBox
    while start <= end:
        mid = (start + end) // 2
        
        crit = 0
        for b in box:
            crit += b - mid
            if crit > 0:
                start = mid + 1
                break
            
        if crit <= 0: #
            end = mid - 1
            answer = min(answer, mid)

        else:
            start = mid + 1
    
    return answer

print(solution([500, 999, 400]))     