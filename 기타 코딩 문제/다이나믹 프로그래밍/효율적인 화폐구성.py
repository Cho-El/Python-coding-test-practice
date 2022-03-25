'''
N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다.
이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수입니다.
M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

ex) 1<=N<=100 1<=M<=10000
2 15 # 첫째 줄에 최소 화폐 개수를 출력, 이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 불가능할 때는 -1을 출력한다.
2
3
출력 5

3 4
3
5
7
출력 -1
'''

n,m = list(map(int, input("입력해주세요 : ").split()))
# coin = list(map(int, input().split('\n')))
coin = []
for i in range(n):
    coin.append(int(input()))

d = [0]*10001
def how_many(n,m):
    min_coin = min(coin)
    if min_coin > m: # 가장 작은 화폐보다 m값이 작은 경우
        d[m] = -1
    else:
        for i in coin:  # 초기 동전 갯수
            d[i] = 1
        for i in range(min_coin, m+1): # i값이 i값을 만들기 위한 최소한의 동전수
            for j in coin: # 주어진 화폐 돌아보기
                min_list = [] # 뺄 수 있는 화폐들 모두 모음
                if i >= j and d[i-j] != 0 and d[i-j] != -1 : # 화폐 값보다 구하려는 값이 작지 않은 경우
                    min_list.append(d[i-j] + 1)
            if not min_list: # i값에서 뺄수 있는 동전이 하나도 없으면 해당 값은 -1
                d[i] = -1
            else:
                d[i] = min(min_list)
                min_list = []

    print(d[m])


d = [10001] * (m+1)
d[0] = 0

def how_many2(n,m):
    for i in range(n): # 화폐 단위
        for j in range(coin[i], m+1): # 금액 
            if d[j-coin[i]] != 10001:
                d[j] = min(d[j], d[j-coin[i]]+1)

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])

how_many2(n,m)