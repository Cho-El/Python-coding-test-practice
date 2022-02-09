'''
문제 어떠한 수 N이 1이될 떄까지 다음의 두 과정 중 하나를 반복적으로
선택하여 수행하려 한다. 단 두번째 연산은 N이 K로 나누어 떨어질 떄만 선택할 수 있다.
1. N에서 1을 뺸다.
2. N을 K로 나눈다.

N이 1이 될 떄까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.
'''

N,K = map(int, input("N과 K를 입력해주세요 : ").split())

def number_one(N,K):
	cnt = 0
	while(N != 1):
		if N%K != 0:
			N -= 1
			cnt += 1
			continue

		N /= K
		cnt += 1

	return cnt

def number_one2(N,K):
	cnt = 0
	while(True):
		# 안나눠질 떄까지 1을 한번에 빼기
		target = (N//K) * K # 가장 크게 나눌 수 있는 값
		cnt += N-target # 총 cnt에 더해주기
		N = target
		if N == 0: # N값이 0이 되는 순간  
			cnt -= 1
			break
		cnt += 1
		N /= K

	return cnt
print("최소 횟수는 : ", int(number_one2(N,K)))