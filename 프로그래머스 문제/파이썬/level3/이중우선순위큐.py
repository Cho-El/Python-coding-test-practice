import heapq

# 힙에서 원소 뺐으면 다른 힙 초기화하고 다시 넣어줌
def changeHeap(heap):
    h = []
    for num in heap:
        heapq.heappush(h, -num)
    return h

def solution(operations):
    answer = []  # [최댓값, 최솟값]
    minheap = []
    maxheap = []

    for o in operations:
        command, num = o.split(' ')
        num = int(num)
        if command == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        elif command == 'D':
            try:
                if num == 1:  # 최댓값 삭제
                    heapq.heappop(maxheap)
                    minheap = changeHeap(maxheap)
                else:  # 최솟값 삭제
                    heapq.heappop(minheap)
                    maxheap = changeHeap(minheap)
            except:
                continue

    if len(maxheap) != 0:
        answer.append(-maxheap[0])
    else:
        answer.append(0)
    if len(minheap) != 0:
        answer.append(minheap[0])
    else:
        answer.append(0)
    return answer