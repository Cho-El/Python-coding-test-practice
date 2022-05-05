'''
파이썬에서 소수의 연산의 경우
소수가 실수와 무리수를 둘다 표현해야하므로 일반연산을 하면

이상한 값이 나온다.
ex) 0.1 + 0.3 == 0.400000000000000000000004

'''

def solution(lines):
	array = []
	result = 0
	for line in lines:
		year, time, throughput = line.split(' ')
		hour, minute, second = time.split(':')
		end_second = int((int(hour) * 3600 + int(minute) * 60 + float(second)) * 1000)
		start_second = end_second - int(float(throughput[:-1]) * 1000) + 1
		array.append((start_second, end_second))
	
	for crit in array:
		crit_start = crit[1]
		crit_end = crit_start + 1000 - 1
		cnt = 0
		for a in array:
			if not(a[1] < crit_start or a[0] > crit_end):
				cnt += 1
	
		result = max(cnt, result)

	return result

if __name__ == '__main__':
	a =  [[
			"2016-09-15 01:00:04.001 2.0s",
			"2016-09-15 01:00:07.000 2s"
			],[
			"2016-09-15 01:00:04.002 2.0s",
			"2016-09-15 01:00:07.000 2s"
			],[
			"2016-09-15 20:59:57.421 0.351s",
			"2016-09-15 20:59:58.233 1.181s",
			"2016-09-15 20:59:58.299 0.8s",
			"2016-09-15 20:59:58.688 1.041s",
			"2016-09-15 20:59:59.591 1.412s",
			"2016-09-15 21:00:00.464 1.466s",
			"2016-09-15 21:00:00.741 1.581s",
			"2016-09-15 21:00:00.748 2.31s",
			"2016-09-15 21:00:00.966 0.381s",
			"2016-09-15 21:00:02.066 2.62s"
			]]
	for i in a:
		print(solution(i))