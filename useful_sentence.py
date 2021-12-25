import math
# 빈 리스트 확인, 빈 배열 확인
A = []
if not A : 
	print('빈 배열입니다.')

a = []
if len(a) == 0 : 
	print("빈 배열입니다.")

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

list = [int(i) for i in str(1234)]
print(*list)
print(sum(list))
print(str(1234))

def solution2(n):
	return sum([int(i) for i in str(n)])

class Counter:
	def __init__(self, stop):
		self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
		self.stop = stop    # 반복을 끝낼 숫자
	
	def __iter__(self):
		return self         # 현재 인스턴스를 반환
	
	def __next__(self):
		if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
			r = self.current            # 반환할 숫자를 변수에 저장
			self.current += 1           # 현재 숫자를 1 증가시킴
			return r                    # 숫자를 반환
		else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
			raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')