'''
힙 라이브러리 사용 예제 : 최소 힙
'''
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,6,9,2,4,6,8,0])
print(result)

'''
힙 라이브러리 사용 예제 : 최대 힙
파이썬에서는 기본적으로 최소 힙을 제공
'''

# 내림차순 힙 정렬(Heap Sort)
def heapsort2(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value) # 부호를 바꾸어 삽입
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)) :
        result.append(-heapq.heappop(h))
    return result

result = heapsort2([1,3,5,6,9,2,4,6,8,0])
print(result)