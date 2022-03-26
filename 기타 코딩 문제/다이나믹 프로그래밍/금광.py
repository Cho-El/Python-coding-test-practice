'''
n X m 크기의 금광이 있습니다. 금광은 1 X 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의
금이 들어 있습니다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수
있습니다. 이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.
1<= T <= 1000
1<= n, m<=20

ex)
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
출력 19
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
출력 16
'''
test_num = int(input("테스트 케이스 갯수 : "))

dn = [0,-1,1] # 오른쪽, 오른쪽 위, 오른쪽 아래

for i in range(test_num):
	n,m = list(map(int, input("입력해주세요 : ").split()))
	array = list(map(int,input().split()))
	array2 = []
	index = 0
	for i in range(n):
		array2.append(array[index:index+m])
		index += m

	dp = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(n): # 첫 dp 테이블 초기값 선언
		dp[i][0] = array2[i][0]
	
	# print(array2)
	# print(dp)

	# dp테이블 채우기 m-1번이동하므로
	for i in range(1,m): # y값 1부터 m-1까지 이동
		for j in range(n): # x값 0부터 n-1까지 이동
			if j == 0: # 첫 번째 줄일때
				dp[j][i] = array2[j][i] + max(dp[0][i-1],dp[1][i-1])
			elif j == n-1: # 마지막 줄일때
				dp[j][i] = array2[j][i] + max(dp[n-1][i-1],dp[n-2][i-1])
			else: # 중간 줄일때
				dp[j][i] = array2[j][i] + max(dp[j-1][i-1],dp[j][i-1],dp[j+1][i-1])
	
	for i in array2:
		print(i)

	for i in dp:
		print(i)

	result = max([dp[i][m-1] for i in range(n)])
	print(result)