from collections import deque

def solution1(elements):
    result = set()
    q = deque(elements)
    # 로직 : 해당 배열에서 연속 부분 수열의 합을 찾은 후 앞에 것을 빼서 뒤에 넣어준다.
    for i in range(len(elements)):
        prevNum = 0
        sumNum = 0
        for j in range(len(elements)):
            if prevNum <= q[j]:# 전 숫자보다 큰경우
                sumNum += q[j]
                result.add(sumNum)
                result.add(q[j])
                prevNum = q[j]
            else: 
                sumNum = q[j]
                prevNum = q[j]
                result.add(prevNum)
        front = q.popleft()
        q.append(front)
        prevNum = 0
        sumNum = 0
        for j in range(len(elements) - 1, -1, -1):
            if prevNum <= q[j]:# 전 숫자보다 큰경우
                sumNum += q[j]
                result.add(sumNum)
                result.add(q[j])
                prevNum = q[j]
            else: 
                sumNum = q[j]
                prevNum = q[j]
                result.add(prevNum)
        front = q.popleft()
        q.append(front)
    print(result)
    return len(result)



def solution(elements):
    answer = 0
    result = set()
    eleLen = len(elements)
    elements = elements * 2
    
    for i in range(eleLen):
        for j in range(eleLen):
            result.add(sum(elements[j:j+i+1]))
    return len(result)
print(solution([7,9,1,1,4]))