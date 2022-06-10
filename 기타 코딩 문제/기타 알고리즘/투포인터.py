'''
투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘입니다.
시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현할 수 있습니다.
'''

'''
특정한 합을 가지는 부분 연속 수열 찾기
N개의 자연수로 구성된 수열이 있습니다.
합이 M인 부분 연속 수열의 개수를 구해보세요.
수행 시간 제한은 O(N)입니다.
'''
'''
투 포인터를 활용하여 문제 해결하기
1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스를 가리키도록 한다.
2. 현재 부분 합이 M과 같다면, 카운트한다.
3. 현재 부분 합이 M보다 작다면, end를 1증가시킨다.
4. 현재 부분 합이 M보다 크거나 같다면, start를 1증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.
'''
def seq(M, array):
    end = 0
    now_sum = 0
    cnt = 0
    for start in range(len(array)):
        while now_sum <M and end < len(array):
            now_sum += array[end]
            end += 1
        if now_sum == M:
            cnt +=1
        now_sum -= array[start]

    while start < len(array) and end < len(array):
        if now_sum < M:
            now_sum += array[end]
            end += 1
        else:
            if now_sum == M:
                cnt += 1
            now_sum -= array[start]
            start += 1

    print(start, end, cnt)
    return cnt

def seq2(M, array):
    start = 0
    end = 0
    now_sum = 0
    cnt = 0

    while start < len(array) and end < len(array):
        if now_sum < M: # end가 움직일 때
            now_sum += array[end]
            end += 1
        else: # start가 움직일 때
            if now_sum == M:
                cnt += 1
            now_sum -= array[start]
            start += 1

    print(start, end, cnt)
    return cnt

M = 5
array = [1,2,3,2,5]
print(seq(M, array), seq(M, array))

'''
구간 합문제
N개의 정수로 구성된 수열이 있습니다.
M개의 쿼리정보가 주어집니다.
 - 각 쿼리에 대하여 left, right구간에 포함된 데이터들의 합을 출력해야 합니다.
수행 시간 제한은 O(N + M)입니다.
'''

'''
접두사 합
'''

def part_sum(data,l,r):
    sum_value = 0
    prefix_sum = 0
    for i in data:
        sum_value += prefix_sum.append(sum_value)