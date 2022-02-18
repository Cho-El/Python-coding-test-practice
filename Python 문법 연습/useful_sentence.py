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
list1 = [int(i) for i in str(1234)]
print(list1)
print(*list1) 
print(sum(list1))
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

# 리스트를 문자열로 합치기------------------------------------------------
# 원본 리스트
a = ['BlockDMask', 'python', 'join', 'example']
print(a)
print()

# 리스트를 문자열로 합치기------------------------------------------------
result1 = "_".join(a)
print(result1)

# 리스트를 문자열로 합치기------------------------------------------------
result2 = ".".join(a)
print(result2)

#zip 함수
for number, upper, lower in zip('12345','ABCDE','abcde') :
	print(number, upper, lower)

#swap
a, b = 1, 2
a, b = b, a
print("swap : ", a,b)

# 아스키 코드 값을 이용한 'a'로 얼마나 떨어져 있는지 구하는 법------------------------------------------------
data = 'b'
col = int(ord(data[0])) - int(ord('a')) # 아스키코드
print(col)

# 람다 표현식 -> 내장 함수에서 자주 사용된다.------------------------------------------------
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
	return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key = lambda x: x[1]))
#출력값이 둘이 같다.

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
a = (1,2)
# 같은 인덱스끼리 더하여 list로 반환하기
result = list(map(lambda a, b: a+b, list1, list2))
print(list1 + list2)
print(list(result))

# sorted 함수------------------------------------------------
'''
sorted함수의 key값으로는 함수가 들어가야 한다.
sorted(정렬할 iterable 객체, key = 함수)
https://blockdmask.tistory.com/466
'''
student_tuples = [('dave','B', 20), ('jane', 'B', 11), ('john', 'A', 13)]
print(sorted(student_tuples, key = lambda student: student[-1]))

student_tuples1 = [[('dave','B', 20), ('jane', 'B', 11), ('john', 'A', 13)], [('dav','C', 25), ('jae', 'A', 12), ('john', 'B', 11)]]
print(sorted(student_tuples1, key = lambda student: student[1][1])) # ('jane', 'B', 11)의 두번째 B를 기준으로 정렬

# sorted : 딕셔너리 value 정렬(lambda 이용)
d = {'blockdmask': 400, 'equal': 300, 'apple': 200, 'dish': 100, 'cook': 500}
print('1. 원본 딕셔너리')
print(d.items())

print('\n2. 딕셔너리 정렬 : sorted(d.items())')
f = sorted(d.items())
print(f)

print('\n3. 딕셔너리 정렬 : sorted(d.items(), key=lambda x: x[1])')
g = sorted(d.items(), key=lambda x: x[1])
print(g)

print('\n4. 딕셔너리 정렬 : sorted(d.items(), key=lambda x: x[1], reverse=True)')
h = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(h)

# bisect 사용
from bisect import bisect_left, bisect_right

a = [10,11,12,13,14]

def index(a, x): # 인덱스
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x): # x값보다 전에 있는 값중에 가장 오른쪽에 있는 값 찾기
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x): # x값보다 전에 있는 값중에 가장 오른쪽에 있는 값 또는 같은 값 찾기
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

print(find_lt(a,18))