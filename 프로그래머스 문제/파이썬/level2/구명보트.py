from collections import deque

def solution1(people, limit): # 시간 초과
    people.sort()
    first= 0
    cnt = 0
    i = 0
    check = 0
    while people:
        first,i,check = 0,0,0

        if first == 0: # 구명보트에 한명 태움
            first += people.pop()
        # 한명 태운 몸무게를 기준으로 limit를 넘지 않는 몸무게의 사람을 태움
        while len(people) >= i + 1:
            if people[i] + first <= limit: # 조건에 맞아 구명보트 두명을 태움
                people.pop(i)
                check = 1
                cnt += 1
                break
            else:
                i += 1

        if check != 1: # 구명보트에 한명만 타는 경우
            cnt += 1

    return cnt

limit = 100
people = [40, 80, 20, 50]
print(solution1(people, limit))

def solution2(people,limit): # 시간 초과 개선됨
    cnt = 0
    while people:
        first,i = 0,0
        final_index = -1
        if first == 0: # 구명보트에 한명 태움
            first += people.pop()

        # 보트에 같이 탈 짝 구해주기
        for i in range(len(people)):
            if first + people[i] <= limit: # limit를 넘지 않는 사람을 발견
                if final_index != -1:
                    final_index = i if people[final_index] < people[i] else final_index
                else:
                    final_index = i
        
        if final_index != -1:
            people.pop(final_index)
            cnt += 1
        else:
            cnt += 1

    return cnt

limit = 100
people = [40, 80, 20, 50]
print(solution2(people, limit))


def solution(people, limit):
    boat = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한도 있음.
    q = deque(people)
    w = 0
    cnt = 0
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                boat += 1
        else:
            q.pop()
            boat += 1
    return boat