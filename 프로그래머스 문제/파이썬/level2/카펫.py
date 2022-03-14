import math
def solution(brown, yellow):
	answer = []
	width = brown + yellow
	# for i in range(int(math.sqrt(width))+1, 0, -1):
	for i in range(int(math.sqrt(width))+1, 0, -1):
		if width % i == 0 and (i - 2) * (width//i - 2) == yellow:
			answer.append(i)
			answer.append(width//i)
			break
	answer.sort(reverse = True)
	
	return answer

brown = 18
yellow = 6
print(solution1(brown,yellow))