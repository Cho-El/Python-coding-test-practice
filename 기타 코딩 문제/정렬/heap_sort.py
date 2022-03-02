# 힙 성질을 확인 후 재정렬
# unsorted : 배열, index : 인덱스, heap_size : 크기
def heapify(unsorted, index, heap_size):

    largest = index

    left_index = 2 * index
    right_index = 2 * index +1

    # 자식노드가 범위안에 드는지 확인, 자식노드가 부모노드보다 큰지 확인
    # 자식노드가 부모노드보다 크다면 인덱스 스위치

    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        ### [loop1]. largest = 6
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
   
    # 부모노드의 인덱스값이 바뀌었다면 자식노드의 값과 스위치

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        # 재귀 함수
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    # 리스트에 전체 길이를 받음
    n = len(unsorted)

    # // 연산자 : 몫 구하기
    # 이진트리를 구하기 때문에 전체 크기의 반만 반복
    # for문을 거꾸로 돌아감
    # 이진트리의 가장 아래서부터 heapify를 실행하여 힙 구조를 만듬

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    # 마지막 노드부터 루트노드를 기준으로 값을 스위치하면서 정렬
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted