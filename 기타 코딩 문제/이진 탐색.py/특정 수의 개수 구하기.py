'''
N개의 원소를 포함하고 있느 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가
등장하는 횟수를 계산하세요. 예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면, 현재 수열에서
값이 2인 원소가 4개이므로 4를 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계해야 합니다.

ex)
7 2
1 1 2 2 2 2 3
출력 : 4
'''

N,M = list(map(int, input("두 수를 입력해주세요 : ").split()))
array = list(map(int, input().split()))

def count_x(N,M):
    start = 0
    end = N-1
    cnt = 0
    while start <= end:
        mid = (start + end)//2
        if array[mid] == M:
            cnt += 1
            for i in range(mid+1, N):
                if array[i] == M:
                    cnt += 1
                else:
                    break
            for i in range(mid-1,-1,-1):
                if array[i] == M:
                    cnt += 1
                else:
                    break
            break

        if array[mid] > M:
            end = mid - 1
        if array[mid] < M:
            start = mid + 1
    return cnt

from bisect import bisect_left, bisect_right
def count_x2(N,M):
    l = bisect_left(array, M)
    r = bisect_right(array,M)
    return r-l
print(count_x(N,M))
print(count_x2(N,M))