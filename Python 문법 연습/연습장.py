
# 원소가 하나 있을 때 -1인 경우 첫 번째 원소를 출력
c = [1]
print(c[-1]) # 1

# 리스트 + 리스트는 리스트 안에 해당 원소들이 전부 들어간다.
a = [[2],[3]]
result = []
for C in a:
    result.append([1]+C)
print(result) # [[1, 2], [1, 3]]

# if 문으로 비교하는 경우 key값을 비교한다. -> True
memo = {1:20, 2:30, 3:40}
if 3 in memo: # 
    print(True)
else:
    print(False)

# [0,1,2,3]
print(list(range(4)))

# 튜플을 str으로 씌우는 경우 그냥 자체가 전부 str으로 바뀐다.
key = str((1,2))
print(type(key))
print(key[0]) # (
print(key[1]) # 1

# 리스트 안의 값을 스왑
a = [1,2,3,4,5]
a[0], a[1] = a[1], a[0]
print("a는 :", a) # [2,1,3,4,5]

# range에 다한 이해
print(list(range(2,0,-1))) # [2,1]
for i in range(2,0,-1):
    print("메롱", end = " ")
    print(i)
    print()
# 메롱 2, 메롱 1

# 나머지
print(8//2) # 4
print(3//2) # 1

# 다중 연속 할당 시 마지막 값이 입력됨
a = [1,2,3,4,5,6]
a[0] = a[3] = a[5]
print(a) # [6,2,3,6,5,6]

# Slice 1
g = [[' ' for _ in range(3)] for _ in range(3)]
print(g) # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print(g[0][:5]) # [' ', ' ', ' '] -> slice인 경우 끝 인덱스가 전체 인덱스를 넘어가도 오류가 나지 않음
print(g[0]) # [' ', ' ', ' ']
g[1] = ['*', ' ', '*']
g[0] = g[2] = ['*']*3 
for i in range(3):
    print(g[i][:3])
# ['*', '*', '*']
# ['*', ' ', '*']
# ['*', '*', '*']

# 슬라이스에 요소 할당하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a','b','c']
print(a) # [0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90] -> 리스트가 변경 되며 한 개씩 들어감
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a']    # 인덱스 2부터 4까지에 값 1개를 할당하여 요소의 개수가 줄어듦
print(a) # [0, 10, 'a', 50, 60, 70, 80, 90]
print(len(a)) # 8
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e'] # 인덱스 2부터 4까지 값 5개를 할당하여 요소의 개수가 늘어남
print(a) # [0, 10, 'a', 'b', 'c', 'd', 'e', 50, 60, 70, 80, 90]
print(len(a)) # 12
# 인덱스 증가폭을 설정하는 경우
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b', 'c']    # 인덱스 2부터 2씩 증가시키면서 인덱스 7까지 값 할당
print(a) # [0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
# 그 밖의 range, 튜플, 문자열은 슬라이싱으로 할당을 할 수가 없다.
abc = [['1','2','3'],['4','5','6'],['7','8','9']]
# 인덱스로 삭제
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:8:2]    # 인덱스 2부터 2씩 증가시키면서 인덱스 6까지 삭제
print(a) # [0, 10, 30, 50, 70, 80, 90]
# 슬라이싱으로 삭제하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:30:2] # 끝 인덱스가 역시 총 인덱스를 넘어도 오류가 나지 않는다.
print(a) # [0, 10, 30, 50, 70, 90]
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[2:40:3]) # [20,50,80]
# 음수 슬라이싱
a = [1,2,3,4,5,6,7]
print(a[-10:]) # [1,2,3,4,5,6,7]
# 음수 시작인 경우 해당하는 숫자 인덱스부터 시작해서 end 사이를 출력
a = [1,2,3,4,5]
print(a[-4:3]) # -4,-3,-2,-1 이런식의 인덱스가 뽑히는 게아닌 인덱스 -4에 해당하는 값부터 3에 해당하는 인덱스가 출력됨
#[2,3]

# join으로 문자열 만들기
abc = [['1','2','3'],['4','5','6']]
print(abc[1]) # ['4', '5', '6']
print(abc[1][2] ) # 6
print(''.join(abc[1])) # 456

# 나눗셈
N = 17
a = 3
N /= a
print(N) # 5.666666666666667 -> 7이 나오는 이유 부동 소수점 이슈
print(a) # 3
# 반올림 round -> Round half to even 방식 주의(1.5 2.5 등 중간값인 경우 짝수인 정수로 반올림된다)
print(round(1.5)) # 2
print(round(2.5)) # 2
# 올림 math 함수의 ceil
import math
print(math.ceil(1.5))
print(math.ceil(-1.5))
# 내림 math 함수의 floor
print(math.floor(1.5))
print(math.floor(-1.5))
# 버림 math 함수의 trunc
print(math.trunc(1.5))
print(math.trunc(-1.5))

# 부동 소수점 이슈
print(0.1 + 0.2) # 0.30000000000000004
# 우리가 보통 계산 할때 사용하는 10진법과 달리 컴퓨터는 2진법으로 동작하는데,
# 몇몇 소수는 10진법에서 2진법으로 변환하는 과정에서 무한 소수가 되어버린다.
# 저장공간에 한계가 있는 컴퓨터는 무한 소수를 유한 소수로 바꾸게 되는데,
# 이 과정에서 미세한 오차가 발생해서 오류가 발생한 것이다. (정밀도 문제)
# 그러하기에 소수점 더하기의 경우 주의를 해야 한다.
# 해결방법 1 소수점 만큼 10을 곱해서 계산 후 마지막에 나눠준다. -> 추천
# 해결방법 2 소수점 계산한 값을 원하는 자리에서 반올림 해준다.
print(type(3/100)) # float

# 문자열 포멧팅 -> 3.6부터 f포메팅 추천
name = "june"
result = f"your name is {name}"
print(result) # your name is june

# 이중 리스트 삽입
li = [[0]*3 for _ in range(5)]
print(li) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  

# 58까지 3의 개수 구하기
cnt_second = 0
for i in range(59):
	for j in str(i):
		if j == '3':
			cnt_second += 1
			break
print(cnt_second)


for i in range(10,20):
    for j in range(20,25):
        print(str(i)+str(j), end = ' ')
    print()

# 문자열 아스키 코드 값의 비교
t = 'b'
if t>'a':
    print(t)

# 문자 -> 아스키 코드(int) : ord, 아스키 코드(int) -> 문자(str) : chr
data = 'bd'
print(type(ord(data[0]))) # int
col = int(ord(data[0])) - int(ord('a')) # 1
print(chr(ord('a') + col)) # 'b'
print(type(chr(ord('a') + col))) # str

# 문자열의 정렬 -> 아스키 코드 순으로 여러개가 합쳐진 문자인 경우 제일 앞의 문자 아스키 코드에 따라 정렬 순서 결정
data = ['B','G','A','E','C','()A', ')G']
print(ord('(')) # 40
print(ord(')')) # 41
data.sort()
print(data) # ['()A', ')G', 'A', 'B', 'C', 'E', 'G']

# 같은 인덱스끼리 더하여 list로 반환하기
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = [9,9,9,9,9]
num = 1
result = map(lambda a, b, c: a+b+c, list1, list2, list3)
result2 = zip(list1, list2, list3)
print(list(result)) # [16, 18, 20, 22, 24] 각 원소를 더함
print(list(result2)) # [(1, 6, 9), (2, 7, 9), (3, 8, 9), (4, 9, 9), (5, 10, 9)] 

# deque
from collections import deque
start = 1
queue = deque([(1,2)])
queue.append(1)
print(queue)
print(queue.popleft())
queue.append(2)
print(queue)
print(queue)
print(queue.popleft())
print()

# if 문의 순서, try except 문
# try:
#     a =[1,2,3,4,5]
#     for i in range(len(a)):
#         if  a[i] == 1 or a[i] == 2 or a[i] == 3 or a[i+6]==1: # if문의 왼쪽부터 차근 차근 검사함 -> 1통과 2통과 후 다른 숫자를 검색할때 오류가 발생
#             print(a[i])
#         else:
#             print("not",a[i])
# except:
#     print('out of index')

# 한 줄 문법
a = [1,2,3,4,5,6,7]
t = [x for x in a if x >=3]
print(t)


# 문자열 여러줄 입력받기 
# n = 5
# s_list = [input() for _ in range(n)] #예시로 n에 3넣어 3줄 입력받기(엔터로 구분)
# for i in range(n):
# 	array = [list(map(int, input().split()))]
# print(array)

# 이차원 리스트의 생성
# 곱하기의 경우 얕은 복사
board = [[0] * 4] * 4
for i in range(4):
  print(board[i])
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
board[0][0] = 1 # board[0] ~ board[3] 까지 모두 같은 배열을 가르킴
for i in range(4):
  print(board[i])
# [1, 0, 0, 0]
# [1, 0, 0, 0]
# [1, 0, 0, 0]
# [1, 0, 0, 0]
a = [2] * 4
a[0] = 1
print(a)
# 2차원 리스트 생성시 밑 방법을 사용하던가 아니면 모두 for문으로 만들 것을 추천
board = [[0] * 4 for _ in range(4)]
board[1][2] = 1
for i in range(4):
  print(board[i])

# 전역 변수
a = 3
b = 1
def practice(n):
    global w # w는 전역변수로 함수 실행이 끝나도 없어지지 않는다.
    w = 1
    result = a + b + n
    print(result)
practice(5) # 9
print(w)

# 다중 할당
a = [1,2,3]
c,d,e = a
print(c,d,e)  # 1 2 3

# 인덱스 뽑아내기
persons = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
for i in persons:
    print(persons.index(i))

# enumerate
wordList = enumerate(["zero","one","two","three","four","five","six","seven","eight","nine"]) 
print(list(wordList))
for i in wordList:
    print(i)
print(list(wordList)) # []
# 빈 리스트가 뽑히는 이유 :
# enumerate() 함수는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게
# 해주는 iterator 객체이다. 모든 값을 순회하면서 소진 했기에 빈 리스트가 반환 된다.

# set 연산자 활용
a = [1,2,3,4,5,5]
b = [3,4,5,5,6,7,8]
print(set(a)) # {1, 2, 3, 4, 5}
print(set(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set(a)&set(b)) # {3, 4, 5}
print(set(a)|set(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set(a)-set(b)) # {1, 2}
print(set(a)^set(b)) # {1, 2, 6, 7, 8} 대칭 차집합합

# 문자열 find
a = 'anfei2gn3a'
print(a.find('feig')) # 해당 문자열이 없어서 -1 반환
print(a.find('a')) # 0 해당 문자열이 찾아지는 가장 첫번째 인덱스 반환

# 문자열 strip
text = "dog.jpeg"
print(text.strip("abcd.e")) # 양쪽 끝에 해당 하는 문자열이 있는 지 체크 후 하나씩 지워 나간다.
# og.jpeg
 
# 문자열을 바로 list로 받는 경우 \n 조심
# import sys
# input = sys.stdin.readline
# a = list(input()) # abcde
# print(a) # ['a', 'b', 'c', 'd', 'e', '\n']

# 큰 따옴표 출력 백슬슬랫 사용
token = '{"[]}'
print(token)
token = "{\"[]}"
print(token)
token = "{'""'}"
print(token)
for removeChar in token:
    print(removeChar)

# 부등호 한번에 표현하기
a= 3
if 2<= a <= 5:
    print("메")

# 소문자로 바꾸기
new_id = 'ABCDEF'
for id in new_id:
    if 'A'<= id <= 'Z':
        id1 = chr(ord(id) - (ord('A') - ord('a')))
        new_id = new_id.replace(id, id1) # 문자열 치환
print(new_id)
new_id = 'ABCDEF'
new_id = new_id.lower()
print(new_id)

# Split
temp = 'hello, What are doing'
print(temp.split()) # ['hello,', 'What', 'are', 'doing']

# Strip
temp = '..fjeijfiege.1.'
temp = temp.strip('.1')
print(temp[-1])
print(temp + 'a')

# -1 인덱스
answer = '.'
print(answer[-1]) # .
print(answer[0]) # .

# stack
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
print(len(board))
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop(-1)
stack.append(1)
stack.append(4)
stack.pop()
print(stack)

# 빈 객체 sum
i = []
print(sum(i)) # 0

# zip과 enumerate의 혼합
begin = 'abcd'
target = 'aghd'
for idx, (b,t) in enumerate(zip(begin, target)):
    print(b,t)

# 반환 값이 없으면 None
def abc():
    return None # None을 안써도 가능
g = abc()
if g == None:
    print("none")
print(g) # None

if not g:
    print("빔")
else:
    print("안빔")

# 딕셔너리의 활용
routes = dict()
routes['1'] = 5
print(routes) # {'1': 5}
print(routes.get('1')) # 5
print(routes['1']) # 5
print(routes)

# list의 insert, append
a = [1,2,3,4,5]
a.insert(0,6) # 인덱스 위치에 6을 집어넣음
print(a) # [6,1,2,3,4,5]

# 파이썬의 정렬 알고리즘은 timsort = insert sort + merge sort

# deque 첫 삽입시 [] 중요
start = 1
from collections import deque
q = deque([start])
print(q)
q.append(2)
print(q)

# heapq -> 파이썬의 힙은 최소 힙
import heapq
a = [1,2,3,4,6,8,9]
heapq.heapify(a) # list를 heap 구조로 만들기
print(heapq.nlargest(1,a)) # 가장 큰 숫자 뽑아내기 [9]
print(a) # [1, 2, 3, 4, 6, 8, 9]

h = [[2,6],[3,5],[4,8],[1,7]]
heapq.heapify(h)
heapq.heappop(h)
print(h)

# 최대 힙 만들기
heap_items = [1,3,5,7,9]
max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))
print(max_heap)

# permutations
from itertools import permutations
numbers = [6,10,2]
temp = []
# for i in numbers:
#     temp.append(str(i))
numbers = list(map(str, numbers)) # string화
print(list(permutations(numbers,len(numbers))))
a = permutations(numbers,len(numbers))
b = list(permutations(numbers,len(numbers)))
result = list(map(''.join,a))
result2 = list(map(''.join,b))
print(max(result))
print(result)

# 문자열의 비교
a = '303030'
b = '333'
if a > b :
    print("303030이더큼")
else:
    print("333이 더큼")

print((int(a) > int(b)) - (int(a) < int(b)))
print(a+b)

# Counter
from collections import Counter
num = "12324"
a = Counter(num)
print(a) # Counter({'2': 2, '1': 1, '3': 1, '4': 1})
b = dict(sorted(a.items()))
print(b)

# hash
hash("leo")
print(type(hash("leo")))

# 문자열 정렬
phoneBook = ["119", "97674223", "1195524421"]
phoneBook = sorted(phoneBook)
print(phoneBook)


#  [ SET x 8 ] 초기화
s = [ set() for x in range(8) ] 

N= 5
# 각 set마다 기본 수 "N" * i 수 초기화
for i,x in enumerate(s, start=1):
    x.add( int( str(N) * i ) )
print(s)

# 거꾸로 출력
a = [1,2,3]
for i in range(len(a)-1,-1,-1):
    print(a[i])

# map의 정렬
a, b = map(sorted, [[4,2],[3,1]])
print(a,b) # [2, 4] [1, 3]
a = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
routes = list(map(sorted,a))
print('routes:',routes) # routes: [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

# if문 false 조건
a = 0
if not a:
    print('1')
if not []:
    print('1')
if not {}:
    print('1')
if not deque():
    print('1')
if not set():
    print('1')
# 문자 '0'인 경우 True
if not '0':
    print('1')


# 문자열 속 있는지 체크
a = '11192324'
b =  '923'
if b in a:
    print("존재")

# 전역변수
a = 3
def g():
    global a
    a += 1
g()
print(a)

a = set([1,3,45,2])
print(a)
print(type(sorted(a))) # list
print(type(a)) # set

# set add
# a = [set() for _ in range(3)]
# a[0].add(2)
# a[0].add(2)
# a[0].add(5)
# a[0].add((1,2))
# a[0].add([2,3]) # 들어갈수 없음
# a[0].add({1:2}) # 들어갈수 없음
# print(a)

# 딕셔너리의 덧셈 불가
a = {1:2}
b = {2:4}
# c = a + b
# print(c)
a.update(b)
print(a) # {1: 2, 2: 4}

# map의 문자열
n_str = list(map(int, '12345'))
print(n_str) # [1,2,3,4,5]


size = 5
while size:
    size -= 1
    print(size)

# 리스트 같은 경우 전역변수로 설정한 경우 global 처리 안해도 안의 값을 바꾸면 바뀐다.
visited = [0] * 4
def change_element():
    visited[0] = 1
change_element()
print(visited) # [1,0,0,0]

# 하지만 리스트 자체를 바꾸는 경우 global 처리를 안하는 경우 함수 내부 변수로 인식
visited = [0] * 4
def change_list():
    visited = [1,2,3,4,5]
change_list()
print(visited) # [0,0,0,0]

# 딕셔너리
from collections import defaultdict
from copy import deepcopy
from re import A

# 딕셔너리의 없는 키 조회
a = defaultdict(list)
print(a['feji'])
print(a)

# 딕셔너리의 정렬
all_info = {
    'f':[6,3,9,3],
    "fe":[22,30,4,5]
}
print(all_info.items()) # dict_items([('f', [6, 3, 9, 3]), ('fe', [22, 30, 4, 5])])
print(sorted(all_info)) # ['f', 'fe']
print(sorted(all_info.items())) # [('f', [6, 3, 9, 3]), ('fe', [22, 30, 4, 5])]
for i in all_info.values():
    i.sort()

print(all_info)

#  bisect 이진 탐색
from bisect import bisect_right
from bisect import bisect_left
a = [[2019,4,6],[2018,5,7],[2018,4,2],[2017,6,8],[2018,1,1]]
a = [5,6,8,9]
print(a)
print(bisect_right(a,9))
print(bisect_left(a,9))

# 깊은 복사
t = [10,11]
a = [1,2]
t = a
a = [3,4]
print(t)
print(a)

# 얕은 복사
t = [10,11]
a = [1,2]
t = a
a[1] = 5
print(a) # [1, 5]
print(t) # [1, 5]

# 함수안의 함수로 글로벌 리스트 갱신하기
def a():
    global t
    t = []
    b()
    print(t)

def b():
    global t
    t.append(2)
a()

# 매개 변수를 통한 값 바꾸기
def b():
    l = [4,5,6,7]
    a(l)
    print(l)
    
def a(l):
    l[2] = 5
b()

# 얕은 복사 2
a = [1,2,3,4]
b = []
b.append(a)
a[1] = 10
a[2] = 5
print(b)

# 리스트 뒤집기
a = [[2,3,1,0,0,0,0,1,3,0,0],[2,1,0,2,0,0,0,2,3,0,0],[1,2,3]]
print(a[::-1])

# 얕은 복사 3
def a(x,y,z):
    t = [x,y,z]
    x = 1
    a = 2
    u = [2,1]
    m = 6
    t.append(m)
    t.append(u)
    u[0] = 90
    m = 100
    print(x)
    print(u)
    print(m)
    print(t)

a(10,20,30)

# 깊은 복사
a = [1,2,3,4,5]
b = deepcopy(a)
c = a[:]
d = a
print(b)
c[3] = 20
print(c)
print(a)
print(d)

# 얕은 복사 4
a = [[1,2],[2,3],[3,4]]
temp = a[:]
temp[1][1] = 10
print(a)
print(temp)

# 단일 값 복사는 깊은복사
a = [1,2,3,4]
b = a[2]
a[2] = 5
print(b)

# sort 조건 걸기
a = [[1,9],[1,2],[3,4],[5,6]]
a.sort(key = lambda x : [x[0], x[1]])
print(a) # [[1, 2], [1, 9], [3, 4], [5, 6]]

a = [[3,1],[4,1],[5,0]]
a.sort(key = lambda x : x[1])
print(a) # [[5, 0], [3, 1], [4, 1]]

    
# 다른 크기의 리스트 비교
a = [10,20]
b = [1,20,90]
if a > b:
    print(1)
else:
    print(10)

# 리스트의 곱
a = [1,2,3,4]
a = 2* a
print(a)

# 문자열의 슬라이싱
a = 'abcd'
print(a[-2:])
a = 'deg'
print(a[-10:])

# for문 안의 i값의 변경하는 경우 -> 영향 받지않음
n = [1,2,3,4,5]
for i in range(len(n)):
    print(n[i], end = '') # 12345
    i += 2
print()
i = 0
while i < len(n):
    print(n[i], end = '')
    i += 2
print()

# elif 문 안에 기준 if문과 구문이 겹치면 어떻게 될까? -> 첫 if문만 돌아감
a = 5
if a > 1:
    print(2)
elif a > 1:
    print(1)
    
# enumerate를 사용하는 경우 한번 순회 후 해당 값에는 아무것도 들어 있지 않다.
for i, a in enumerate([9,8,7,6]):
    print(i)

# 딕셔너리의 정렬 -> 리스트로 바꾼 후 가능
a = {'abc': [5,2]}
a = sorted(a.items(), key = lambda x:[x[1][0], -x[1][1]])
print(a[:6])

# 이차원 리스트 마지막 값 뽑아내기
a = [[1,2],[2,3]]
print(a[-1][-1])

# String 정렬
a = ["11:20","11:19","23:12","01:52"]
a.sort()
print(a)

# list 값바꾸기
a = [['a',2,3], ['b',6,3]]

a = "a b c d"
print(a.split())