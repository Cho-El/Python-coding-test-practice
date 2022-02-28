import time
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridgeweight = 0 # 다리 위에 트럭 무게
    wait = deque(truck_weights) # 대기 중인 트럭
    bridge = deque([0 for _ in range(bridge_length)]) # 다리 위 트럭 
    time = 0
    
    # 대기 트럭이 없어지거나 다리 위 트럭이 모두 없어질 때까지
    while bridgeweight > 0 or wait : # wait
        removed_Truck = bridge.popleft()
        bridgeweight -= removed_Truck

        if wait and bridgeweight + wait[0] <= weight: # 다리 무게 확인 후 
            new_truck = wait.popleft()
            bridgeweight += new_truck

            bridge.append(new_truck)
        else:
            bridge.append(0)
        
        time += 1

    return time

length = 2
weight = 10
weights = [7,4,5,6]

start = time.process_time()
print(solution(length, weight, weights))
end = time.process_time()
print("time : ", end - start)

start = time.process_time()
sum = 0
for i in range(1000000):
    sum += i
end = time.process_time()
print("time : ", end - start)

