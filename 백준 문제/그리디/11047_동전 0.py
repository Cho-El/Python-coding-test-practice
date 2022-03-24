import sys
n,k = map(int, sys.stdin.readline().split())
coins = []
result = 0

for i in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse = True)

for coin in coins:
    result += k//coin
    k %= coin

print(result)
        