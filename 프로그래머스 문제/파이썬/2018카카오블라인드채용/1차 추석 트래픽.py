def solution(lines):
	array = []
	result = 0
	for line in lines:
		year, time, throughput = line.split(' ')
		hour, minute, second = map(float, time.split(':'))
		end_second = hour * 3600 + minute * 60 + second
		
		print('t = ', float(throughput[:-1]))
		start_second = end_second - float(throughput[:-1]) + 0.001
		print(start_second, end_second)
		array.append((start_second, end_second))
	
	for crit in array:
		crit_start = crit[1]
		crit_end = crit_start + 0.999
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