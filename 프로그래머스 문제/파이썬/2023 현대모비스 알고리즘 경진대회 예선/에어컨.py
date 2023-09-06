def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    k = 1000 * 100
    t1 += 10
    t2 += 10
    temperature += 10
    # 전략 : 바텀업
    # dp[i][j]는 i분 상태의 j 온도를 만드는 에어컨의 최소 소비 전력
    dp = [[k] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0 # 첫번째 온도
    
    flag = 1
    if temperature > t2:
        flag = -1
        
    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [k]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 에어컨을 키지 않고 실외온도와 달라 -flag 되는경우
                if 0 <= j + flag <= 50:
                    arr.append(dp[i - 1][j + flag])
                # 에어컨을 키지 않고 현재온도와 실외온도가 같아서 변하지 않느 경우
                if j == temperature:
                    arr.append(dp[i - 1][j])
                # 에어컨을 키고 현재온도가 변하는 경우
                if 0 <= j - flag <= 50:
                    arr.append(dp[i - 1][j - flag] + a)
                # 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는 경우
                if t1 <= j <= t2:
                    arr.append(dp[i - 1][j] + b)
                dp[i][j] = min(arr)
    
    answer = min(dp[len(onboard) - 1])
    return answer

print(solution(28,18,26,10,8,[0, 0, 1, 1, 1, 1, 1]))
print(solution(-10,-5,5,5,1,[0, 0, 0, 0, 0, 1, 0]))
print(solution(11,8,10,10,1,[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))
print(solution(11,8,10,10,100,[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))