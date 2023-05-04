from collections import Counter
import heapq
def solution(k, tangerine):
    answer = 0
    tangerineCounter = Counter(tangerine)
    q = []
    for key, value in tangerineCounter.items():
        heapq.heappush(q,[-value, key])
    
    temp = 0
    lenQ = len(q)
    while q:
        maxOrange = -heapq.heappop(q)[0]
        temp += maxOrange
        if temp < k:
            answer += 1
        elif temp == k:
            return answer + 1
        else:
            return answer
        
    return answer

# 기발한 풀이
def solution2(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))
# print(solution(6,[1,3,2,5]))
# print(solution(5,[1,1,1,1,1,2]))
# print(solution(1,[1,1,1,1,1,2]))
print(solution(5,[1,1,1,1,2,2]))



