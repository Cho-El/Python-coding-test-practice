import math
# 빈 리스트 확인, 빈 배열 확인
A = []
if not A : 
	print('빈 배열입니다.')
a = []
if len(a) == 0 : 
	print("빈 배열입니다.")

# for문이나 조건문 옆으로 쓰기
#1 for문 if나 for문 전 줄이 실행됨
list = [int(i) for i in str(1234)]
print(list)
print(*list)
print(sum(list))
print(str(1234))
#2 if 문
start = 1
B = [1,2,3,4]
s = start + 1 if A else 0
print(s)
s = start + 1 if B else 0
print(s)

# 전역 변수 쓰는 법
counter = 0
def f(n):
	global counter # 전역 변수 선언
	for i in range(1, n+1):
		counter += 1
	
	return counter
print(f(5))

# 리스트를 문자열로 합치기
# 원본 리스트
a = ['BlockDMask', 'python', 'join', 'example']
print(a)
print()
 
# 리스트를 문자열로 합치기
result1 = "_".join(a)
print(result1)
 
# 리스트를 문자열로 합치기
result2 = ".".join(a)
print(result2)