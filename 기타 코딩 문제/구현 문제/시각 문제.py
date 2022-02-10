'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는
시각입니다.

00시 00분 03초
00시 13분 30초

반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각입니다.

00시 02분 55초
01시 27분 45초

ex)
5
출력
11475
'''

N = int(input("숫자 입력하세요 : "))
def count_time(N):
	total = 0
	# 1 ~ 60초까지 3이 포함되어 있는 수 세기
	cnt_second = 0
	for i in range(59):
		for j in str(i):
			if j == '3':
				cnt_second += 1
				break
	#1 ~ 59분까지 3이 포함되어 있는 수 세기
	cnt_min = cnt_second
	
	cnt_min_no = 60 - cnt_min
	cnt_min_no *= cnt_second
	cnt_min *= 60
	cnt_min += cnt_min_no # 00시 00분 00초부터 00시 59분 59초까지 3들어있는 갯수

	# 1~24시까지 3이 포함되어 있는 수 세기
	for i in range(N+1):
		for j in str(i):
			if j == '3':
				total += 3600
				break
			else:
				total += cnt_min
				break
	
	return total

print(count_time(N))

def count_time1(N):
	cnt = 0
	for i in range(N+1):
		for j in range(60):
			for k in range(60):
				if '3' in str(i) + str(j) + str(k) :
					cnt += 1
	return cnt

print(count_time1(N))