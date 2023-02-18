import sys
def solution(n,v):
	start = v[0]
	result = v[0] - v[1]
	for i in range(1,len(v)):
		# start와 현재 인덱스의 값의 차가 comp보다 크다면 comp 최신화, 차가 양수라면 start 최신화 및 comp 비교
		dif = start - v[i]
		if dif < 0 :
			start = v[i]
			if result < dif:
				result = dif
		else:
			if result < dif:
				result = dif
	return result
			
if __name__ == "__main__":
	n = [10,10]
	v = [[3,1,4,1,5,9,2,6,5,3],[1,2,3,4,5,6,7,8,9,10]]
	for a,b in zip(n,v):
		print(solution(a,b))