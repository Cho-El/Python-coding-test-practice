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
