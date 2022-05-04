from datetime import datetime as dp
def solution(lines):
	array = []
	result = 0
	for line in lines:
		temp = list(line.split(' '))
		second = int(temp[2][0])
		micro = 0
		if temp[2][1] != 's':
			micro = int(temp[2][2:-1]) * 1000
		dif = dp(2016,9,15,0,0,second,micro)
		end = dp.fromisoformat(temp[0] + ' ' + temp[1])
		print('end = ',end)
		start = end - dif + dp(2016,9,15,0,0,0,1000)
		print(type(start),type(end))
		array.append((start, end))
	print(array[0][0])
	print(dp(2016,9,15,0,0,0,1000))
	a = array[0][0] + dp(2016,9,15,0,0,0,1000)
	print(a)
	# for crit in array:
	# 	cnt = 0
	# 	crit_s = crit[1]
	# 	crit_e = dp(2016,9,15,0,0,0,1000) + crit_s
	# 	print(crit_s)
	# 	print(crit_e)
	# 	for a in array:
	# 		if crit_s >= a[0] and crit_e <= a[1]:
	# 			cnt += 1
		
	# 	result = max(result, cnt)

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
		solution(i)