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
        # 금 가격이 내일 오를 것으로 예상되면 오늘 금을 구매
        if gold_prices[i] < gold_prices[i + 1] and not havingGold:
            havingGold = 1
            profit -= gold_prices[i]
            continue
        
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
            
    
print(solution([2,5,1,3,4]))
print(solution([7,2,5,6,1,4,2,8]))
print(solution([7,6,5,4,3,2,1]))
print(solution([7,2,3,4,5,6,99,101]))