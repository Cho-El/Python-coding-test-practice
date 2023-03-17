from collections import deque
def solution(N, coffee_times):
    answer = []
    makingCoffee = []
    howManyCoffee = len(coffee_times)
    coffee_times = deque(coffee_times)
    orderNum = 1
    # coffee_times 순회
    while True:
        # 커피 추출구에 배정
        while coffee_times:
            # 커피 추출구를 다쓰면 break
            if len(makingCoffee) == N:
                break
            time = coffee_times.popleft()
            makingCoffee.append([time,orderNum])
            orderNum += 1
            
        makingCoffee.sort()
        endTime, endNum = makingCoffee.pop(0)
        answer.append(endNum)
        
        leaveCoffeeNum = len(makingCoffee)
        i = 0
        # 완료까지 남은 커피들 계산
        while i < leaveCoffeeNum:
            leaveTime, leaveNum = makingCoffee.pop(0)
            leaveTime -= endTime
            if leaveTime == 0:
                answer.append(leaveNum)
            else:
                makingCoffee.append([leaveTime, leaveNum])
            i += 1
        
        if len(answer) == howManyCoffee:
            break
        
    return answer

def solution(N, coffee_times):
    extractors = [0] * N
    order_numbers = [0] * N
    completed_orders = []

    current_order = 0

    while len(completed_orders) < len(coffee_times):
        for j in range(len(extractors)):
            if extractors[j] > 0:
                extractors[j] -= 1

            if extractors[j] == 0 and order_numbers[j] != 0:
                completed_orders.append(order_numbers[j])
                order_numbers[j] = 0

        for j in range(len(extractors)):
            if extractors[j] == 0 and current_order < len(coffee_times):
                extractors[j] = coffee_times[current_order]
                order_numbers[j] = current_order + 1
                current_order += 1

    return completed_orders

print(solution(3, [4, 2, 2, 5, 3]))
print(solution(3,[4,2,2,5,3]))
print(solution(1,[100,1,50,1,1]))