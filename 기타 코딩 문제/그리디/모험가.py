'''
한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로
'공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서
제대로 대처할 능력이 떨어집니다.

모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는
반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.

동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는 지 궁금합니다. N명의 모험가에 대한
정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요

ex) N = 5, 공포도 : 2 3 1 2 2
출력 : 2
'''
'''
문제 전략
가장 작은 공포도를 가진 사람부터 팀을 꾸린다.

'''
N = int(input("총원은? : "))
scary_stat = list(map(int, input("공포도 : ").split()))
def team(N, scary_stat):
	team_num = 0
	scary_stat.sort()
	i = 0
	# for i in range(N):
	while(N>i):
		current_size = scary_stat[i]# 그룹의 크기
		start_index = i# 아직 그룹에 포함되지 않은 index
		while(True):
			j = start_index # 시작 인덱스
			cnt = 0
			if j+current_size > N: # N의 크기보다 넘어갈경우
				return team_num

			for k in range(j,j+current_size): # 해당 사이즈의 그룹중에 현재 사이즈보다 큰 숫자가 있으면 current_size를 변경하고 다시 그룹화
				if current_size < scary_stat[k]:
					current_size = scary_stat[k]
					cnt += 1
					break

			if cnt != 0: # 그룹내에 current_size보다 큰 값이 존재했음
				continue
			else: # 그룹형성
				team_num += 1
				i = k+1
				break
	return team_num

def team2(N, scary_stat):
	scary_stat.sort()

	team_num = 0
	cnt = 0
	for i in scary_stat:
		cnt += 1
		if cnt >= i:
			team_num += 1
			cnt = 0
	return team_num

print(team(N,scary_stat))
print(team2(N,scary_stat))
