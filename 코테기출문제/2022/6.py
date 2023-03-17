def findMaxProfit(price):
 
    n = len(price)
 
    # 베이스 케이스
    if n == 0:
        return 0
 
    #는 `n` 크기의 보조 공간을 만듭니다.55
 
    # 보조 공간의 마지막 요소를 0으로 초기화
    profit[n - 1] = 0
 
    # 현재 주가 우측의 최고 주가를 추적
    max_so_far = price[n - 1]
 
    #는 목록을 오른쪽에서 왼쪽으로 순회합니다.
    for i in reversed(range(n - 1)):
 
        # profit[i]을 단일 주식이 벌어들인 최대 수익으로 업데이트
        # `i`일부터 `n-1`일까지 # 거래
        profit[i] = max(profit[i + 1], max_so_far - price[i])
 
        # 업데이트 지금까지 본 최대 주가
        max_so_far = max(max_so_far, price[i])
 
    #는 현재 주가의 왼쪽에 있는 최소 주가를 추적합니다.
    min_so_far = price[0]
 
    #는 목록을 왼쪽에서 오른쪽으로 순회합니다.
    for i in range(1, n):
 
        ''' Update profit[i] by taking a maximum of the following:
           1. profit[i-1], which represents the maximum profit calculated so far
           2. The total profit obtained by closing the first transaction on the day `i`
              and performing another transaction from the day `i` till day `n-1`. '''
 
        profit[i] = max(profit[i - 1], (price[i] - min_so_far) + profit[i])
 
        # 지금까지 본 최저 주가 업데이트
        min_so_far = min(min_so_far, price[i])
 
    # 이익의 마지막 요소는 결과를 저장합니다
    return profit[n - 1]
 
 
if __name__ == '__main__':
 
    price = [2, 4, 7, 5, 4, 3, 5]
 
    print('The maximum profit is', findMaxProfit(price))
 