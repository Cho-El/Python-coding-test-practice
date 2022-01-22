# 자릿수 더하기
def solution(n):
    answer = 0
    while n>=1 :
        answer += n%10
        n //= 10 # 몫 연산자 //
    return answer

print(solution(123))

def solution1(n):
	if n < 10 :
		return n
	return (n%10) + solution1(n//10)

print(solution1(123))

def solution2(n):
	return sum([int(i) for i in str(n)])

print(solution2(123))
