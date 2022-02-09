'''
거스름돈으로 사용할 500, 100, 50, 10원
N원을 거슬러줘야할 때 동전의 최소 개수를 구하세요
'''

N = int(input("거스름돈을 입력해주세요 : "))
def change1(N):
	total_cnt = 0

	cnt = 0
	cnt = N//500
	total_cnt += cnt
	N = N - cnt*500
	
	cnt = N//100
	total_cnt += cnt
	N = N - cnt*100

	
	cnt = N//50
	total_cnt += cnt
	N = N - cnt*50
	
	
	cnt = N//10
	total_cnt += cnt
	N = N - cnt*10
		

	return total_cnt


def change2(N):
	coin_list = [500,100,50,10]
	cnt = 0
	for coin in coin_list :
		cnt += N//coin
		N %= coin

	return cnt

print("동전의 갯수는 : ", change2(N))
