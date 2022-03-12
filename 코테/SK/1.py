# money = 4578
# costs = [1,4,99,35,50,1000]
money = 1999
costs = [2,11,20,100,200,600]

def solution(money, costs):
    coins = [[1,0],[5,0],[10,0],[50,0],[100,0],[500,0]]
    result = 0
    stack = []

    N = money
    for index, coin in enumerate(coins):
        coin[1] = costs[index]
    
    stack.append(coins[0])
    for i in range(1,len(coins)):
        quo = coins[i][0] // stack[-1][0]
        if stack[-1][1] * quo > coins[i][1]:
            stack.append(coins[i])
    
    print(stack)
    while money != 0:
        temp = stack.pop()
        result += (money//temp[0]) * temp[1]
        money %= temp[0]
    
    return result


print(solution(money, costs))