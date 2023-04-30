import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    
    if k >= len(enemy):
        return len(enemy)
    
    for e in enemy:
        if len(heap) != k:
            heapq.heappush(heap, e)
        else:
            minE = heap[0]
            if minE >= e:
                if e > n:
                    return answer + k
                else:
                    n -= e
                    answer += 1
            else:
                if minE > n:
                    return answer + k
                else:
                    n -= minE
                    answer += 1
                    heapq.heappop(heap)
                    heapq.heappush(heap,e)
    
    return answer + k

print(solution(7,3,[4,2,4,5,3,3,1]))
print(solution(2,4,[3,3,3,3]))