'''
패밀리 레스토랑에 가서, 여러 개의 테이블에 사람을 나누어 앉게 하려고 한다.
이때, 한 사람만 앉는 테이블이 없게 그룹을 지어야 한다.
인원수를 나누는 패턴만 구하면 되며, 누가 어디에 앉는지는 고려하지 않아도 된다.
예를 들어 6명이면
2,2,2
2,4
3,3
6 이렇게 4가지가 된다.
한 개의 테이블에 앉을 수 있는 최대 10명이며, 100명이 하나 이상의 테이블에
나누어 앉는 패턴을 구하라.
'''
# 전체 탐색 문제에 대한 접근
'''
1. 탐색한다 -> 반복 -> 재귀함수나 반복문으로 푼다. -> 주로 재귀함수로 푸는 게 쉬움
2. 시작 조건과 종료 조건 확실히 정의
3. 트리 그려서 생각하기 -> 노드와 엣지 구조
'''

min_people = 2
max_people = 10
cnt = 0

def problem1(leave, sit):
    global cnt
    if leave < 0: # 종료조건1
        return
    if leave == 0: # 종료조건2 유효
        cnt += 1
        return
    # 재귀 호출
    # 이전 앉힐 사람 수 ~ 남은 사람 수
    for i in range(sit, 11):
        problem1(leave-i,i)

problem1(100, 2)
print(cnt)

# 메모화 적용

memo = {}
def problem2(leave, sit):
    key = str((leave,sit)) # 
    if key in memo: # 추가된 종료조건 memo에 있는지 확인
        return memo[key]
    if leave < 0: # 종료조건1
        return 0
    if leave == 0: # 종료조건2 유효
        return 1
    
    # 재귀 호출
    cnt = 0
    # 이전 앉힐 사람 수 ~ 남은 사람 수
    for i in range(sit, 11):
        cnt += problem2(leave-i,i)
    # 메모화 처리
    memo[key] = cnt
    return cnt

print(problem2(100, 2))