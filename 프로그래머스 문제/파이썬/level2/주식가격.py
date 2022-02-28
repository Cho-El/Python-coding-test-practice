from collections import deque
prices = [1,2,3,2,3,2,2,1,4]
def solution(prices):
    result = []
    price = deque(prices)
    while price:
        second = 0
        p = price.popleft()
        for i in price:
            if p <= i:
                second += 1
            else:
                second += 1
                break
        result.append(second)
    
    return result

print(solution(prices))