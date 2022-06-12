import sys
from bisect import bisect_left
from copy import deepcopy
def solution(n, plans, clients):
    answer = []
    plan_data = []
    plan_service = []
    client_info = []
    temp = []
    # 요금제 분석
    for plan in plans:
        plan_info = list(map(int, plan.split()))
        plan_data.append(plan_info[0])

        temp += plan_info[1:]
        temp2 = deepcopy(temp)
        plan_service.append(temp2)

    # 고객의 서비스 이용정보
    for client in clients:
        client_info.append(list(map(int, client.split())))
    

    for c_info in client_info:

        if not (set(plan_service[len(plan_service)-1]) >= set(c_info[1:])):
            answer.append(0)
            continue

        if plan_data[len(plan_data)-1] <= c_info[0]: # 고객이 요구하는 이용 데이터 제공이 없는 경우
            answer.append(0)
            continue

        else:
            data_accept_ix = bisect_left(plan_data, c_info[0])
            for i in range(data_accept_ix, len(plan_data)):
                if set(plan_service[i]) >= set(c_info[1:]):
                    answer.append(i + 1)
                    break

    return answer
    
if __name__ == '__main__':
    n = [5,4]
    plans = [['100 1 3', ' 500 4', '2000 5'], ['38 2 3', '394 1 4']]
    clients = [['300 3 5', '1500 1', '100 1 3', '50 1 2'], ['10 2 3', '300 1 2 3 4', '500 1']]
    for n, plans, clients in zip(n, plans, clients):
        print(solution(n, plans, clients))