import sys
sys.setrecursionlimit(10 ** 6)
# def solution(gold_prices):
#     n = len(gold_prices)
#     buy = 0  # 구매한 금의 양
#     profit = 0  # 총 이익
#     for i in range(n):
#         # 금 가격이 내일 오를 것으로 예상되면 오늘 금을 구매
#         if i < n - 1 and gold_prices[i] < gold_prices[i+1]:
#             # 최대 1 돈만 구매 가능
#             can_buy = 1 - buy
#             if can_buy > 0:
#                 buy += can_buy
#                 profit -= gold_prices[i]  # 금을 구매하면 돈을 지불
#         # 금 가격이 내일 떨어질 것으로 예상되면 오늘 금을 판매
#         elif i < n - 1 and gold_prices[i] > gold_prices[i+1]:
#             # 최대 1 돈만 판매 가능
#             can_sell = buy
#             if can_sell > 0:
#                 buy -= can_sell
#                 profit += gold_prices[i]  # 금을 판매하면 돈을 수입
#         # 금 가격이 떨어지지 않을 경우, 금을 팔아 이익을 실현
#         elif i == n - 1 and buy > 0:
#             profit += gold_prices[i] * buy
#     return profit

def solution(gold_prices):
    global result
    result = []
    dfs(gold_prices, 0, 0, 0, len(gold_prices))
    return max(result)

def dfs(gold_prices, havingGold, profit, start, totalLen):
    global result
    for i in range(start,totalLen - 1):
        # 금 가격이 내일 오를 것으로 예상되면 살 수도 있고 안 살수도 있다.
        if gold_prices[i] < gold_prices[i + 1] and not havingGold:
            # 사는 경우
            dfs(gold_prices, 1, profit - gold_prices[i], i + 1, totalLen)
            # 안 사는 경우
            dfs(gold_prices, 0, profit, i + 1, totalLen)
        
        # 금을 가지고 있는 경우
        elif havingGold:
            # 그냥 파는 경우
            dfs(gold_prices, 0, profit + gold_prices[i], i + 2, totalLen)
            # 팔지 않는 경우
            dfs(gold_prices, 1, profit, i + 1, totalLen)
    
    if havingGold:
        result.append(profit + gold_prices[totalLen - 1])
        return
    
    result.append(profit)
    return

def solution2(gold_prices):
    havingGold = 0
    profit = 0
    i = 0
    while i < len(gold_prices) - 2: 
        # 살 수 있는 경우
        if not havingGold:
            # 현재 무조건 사야 하는 경우 : 3개가 상승곡선
            if gold_prices[i] <= gold_prices[i + 1] <= gold_prices[i + 2]:
                havingGold = 1
                profit -= gold_prices[i]
            # 위로 꺾이는 곡선인 경우
            elif gold_prices[i] < gold_prices[i + 1] and gold_prices[i + 1] > gold_prices[i + 2]:
                havingGold = 1
                # 3번째 것이 마지막인 경우 1번째것을 산다.
                if i + 2 == len(gold_prices) - 1:
                    profit -= gold_prices[i]
                # 4번째거와 3번째거의 차이와 1번째거와 두번째거의 차이를 비교하여 산다.
                elif gold_prices[i + 1] - gold_prices[i] >= gold_prices[i + 3] - gold_prices[i + 2]:
                    profit -= gold_prices[i]
                elif gold_prices[i + 1] - gold_prices[i] < gold_prices[i + 3] - gold_prices[i + 2]:
                    profit -= gold_prices[i + 2]
                    i += 2
        # 팔 수 있는 경우 : gold를 가지고 있음
        else:
            # 현재 무조건 팔아야하는 경우
            # 현재 비교하고 있는 i 인덱스의 값보다 i + 1, i + 2가 하락곡선일 때 5 4 3인 경우 5에서 팔아야 함
            if gold_prices[i] > gold_prices[i + 1] and gold_prices[i + 1] > gold_prices[i + 2]:
                havingGold = 0
                profit += gold_prices[i]
                i += 1
            # 위로 꺾이는 곡선인 경우 ex) 5 9 3
            elif gold_prices[i] < gold_prices[i + 1] and gold_prices[i + 1] > gold_prices[i + 2]:
                havingGold = 1
                # i + 2가 마지막인 경우 i + 1을 판다.
                if i + 2 == len(gold_prices) - 1:
                    profit += gold_prices[i + 1]
                    
            # (i 인덱스와 i + 1 인덱스의 값의 차이)와 (i + 2 i + 3 인덱스의 값의 차이를 비교)
                # 앞의 것이 더 크다면 i + 1 인덱스에 판다
                # 뒤에 것이 더 크다면 i 인덱스를 판다.
        i += 1
    return
    
    # 45351 100
print(solution([2,5,1,3,4]))
print(solution([7,6,5,4,3,2,1]))
print(solution([7,2,3,4,5,6,99,101]))
print(solution([3,5,1,100]))