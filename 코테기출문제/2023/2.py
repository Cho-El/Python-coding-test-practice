# def solution(dots, lines):
#     global min_segments
#     min_segments = 11
#     cover_dots(0, 0, dots, lines)

#     return -1 if min_segments == 11 else min_segments

# def cover_dots(start_index, used_segments, dots, lines):
#     global min_segments
    
#     if start_index == len(dots):
#         min_segments = min(min_segments, used_segments)
#         return

#     for line in lines:
#         end_point = dots[start_index] + line
#         next_index = start_index

#         while next_index < len(dots) and dots[next_index] <= end_point:
#             next_index += 1

#         if next_index > start_index:
#             cover_dots(next_index, used_segments + 1, dots, lines)

# import sys
def solution(dots, lines):
    global minLine
    minLine = 11
    lines.sort(reverse = True)
    dfs(0, [], 0, dots, lines)
    
    if minLine == 11:
        return -1
    else:
        return minLine

def dfs(startDotIdx, usedLineIdxList, countUsed, dots, lines):
    global minLine
    if startDotIdx == len(dots):
        minLine = min(minLine, countUsed)
        return
    
    for lIdx in range(len(lines)):
        # 선분 하나를 사용
        if lIdx not in usedLineIdxList:
            usedLineIdxList.append(lIdx)
        else:
            continue
            
        addLine = dots[startDotIdx] + lines[lIdx]
        nextDotIdx = startDotIdx
        
        while nextDotIdx < len(dots) and dots[nextDotIdx] <= addLine:
            nextDotIdx += 1
        
        # 선분이 한개 이상 포함할 수 있는 경우
        if nextDotIdx > startDotIdx:
            dfs(nextDotIdx, usedLineIdxList, countUsed + 1, dots, lines)
            usedLineIdxList.pop()

import sys
def solution(dots, lines):
    global minLine
    INF = sys.maxsize
    minLine = INF
    lines.sort(reverse = True)
    usedLine = 0
    start = 0
    
    for line in lines:
        addLine = dots[start] + line
        usedLine += 1
        
        while start < len(dots) and dots[start] <= addLine:
            start += 1
        
        if start == len(dots):
            break
    
    minLine = min(usedLine, minLine)
    
    if minLine == INF:
        return -1
    else:
        return minLine

print(solution([1,5,8], [1,3,4,6]))
print(solution([1,3,4,6,7,10],[2,2,2,2]))