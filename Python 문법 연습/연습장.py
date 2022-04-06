
a=[1,2,3]
start = 1 if a else 0
print(start)
b = []
print(a[-1])
c = [1]
print(c[-1])

a = [[2],[3]]
result = []
for C in a:
    result.append([1]+C)

print(result) 

memo = {1:20, 2:30, 3:40}

if 3 in memo: # 
    print(True)
else:
    print(False)

print(list(range(4)))

key = str((1,2))
print(key)

a = [1,2,3,4,5]
a[0], a[1] = a[1], a[0]
print("a는 :", a)

for i in range(1,0,-1):
    print("메롱")

for i in range(0,2):
    print(i)

print(8//2)
nums = [1,2,3,4,5]
for i in range(len(nums)-1):
    print("는",i)

print(3//2)

a = [1,2,3,4,5,6]

a[0] = a[3] = a[5] = 12
print(a)

g = [[' ' for _ in range(3)] for _ in range(3)]
print(g)
print(g[0][:3])
print(g[0])
g[1] = ['*', ' ', '*']
g[0] = g[2] = ['*']*3
for i in range(3):
    print(g[i][:3])

print(g)

abc = [['1','2','3'],['4','5','6'],['7','8','9']]
print(abc[1])
print(abc[1][2] )
print(''.join(abc[1]))

a = [1,2,3,4,5,6]
for i in a:
    if i == 1 or i == 2 or i == 3:
        print(i)

a = []
a.append('L')
a.append('R')
print(a)

N = 17
a = 5

N /= a

print(N)

print(a)
print()
for i in range(0,2):
    print(i)

# plan = list(map(str, input("계획서를 입력해주세요").split()))
# print(plan)

li = [[0]*3 for _ in range(5)]
print(li)

for i in li:
    for j in i:
        print()

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

t = 'b'

if t>'a' or t<'z':
    print(t)

data = 'bd'
col = int(ord(data[0])) - int(ord('a')) + 1 # 아스키코드
print(col)

data = ['B','G','A','E','C']
data.sort()
print(data)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
num = 1
# 같은 인덱스끼리 더하여 list로 반환하기
result = map(lambda a, b: a+b, list1, list2)
print(list1 + list2)
print(list(result))
t = 'ab'+'c'
print(t)

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

'''
a =[1,2,3,4,5]
for i in range(len(a)):
    if a[i+6]==1 or a[i] == 1 or a[i] == 2 or a[i] == 3: # if문의 왼쪽부터 차근 차근 검사함
        print(a[i])
    else:
        print("not",a[i])
'''
'''
n,m = input().split()
print(n,m)
n,m = int(input().split())
print(n,m)
'''

a = [1,2,3,4,5,6,7]

t = [x for x in a if x >=3]
print(t)

# a,target = list(map(int, input().split()))

# print(target)


for i in range(4,-1,-1):
    print(i)

n = 5
#3. 문자열 여러줄 입력받기 
# s_list = [input() for _ in range(n)] #예시로 n에 3넣어 3줄 입력받기(엔터로 구분)

# for i in range(n):
# 	array = [list(map(int, input().split()))]

# print(array)
m=4

dp = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(dp)
result = max([dp[i][2] for i in range(4)])

print(result)

board = [[0] * 4] * 4
for i in range(4):
  print(board[i])

board[0][0] = 1
for i in range(4):
  print(board[i])

board = [[0] * 4 for _ in range(4)]
board[1][2] = 1
for i in range(4):
  print(board[i])

nums = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


abc = False

if not abc:
    print("ㅇㅇ")

a = 3
b = 1

def practice(n):
    global w # w는 전역변수로 함수 실행이 끝나도 없어지지 않는다.
    result = a + b + n
    print(result)

practice(5)

graph=[1]
for i in graph:
    print("1")
        
a = [1,2,3]
c,d,e = a
print(c,d,e)

persons = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
for i in persons:
    print(persons.index(i))

wordList = enumerate(["zero","one","two","three","four","five","six","seven","eight","nine"]) 
print(wordList)

# set 연산자 활용
a = [1,2,3,4,5,5]
b = [3,4,5,5,6,7,8]
print(set(a))
print(set(b))
print(set(a)&set(b))
print(set(a)|set(b))
print(set(a)-set(b))
print(set(a)^set(b))

a = 'anfei2gn3'
print(a.find('feig'))

text = "dog.jpeg"
print(text.strip("j.peg"))

token = "{\"[]}"
for removeChar in token:
    print(removeChar)

a= 3
if 2<= a <= 5:
    print("메")

new_id = 'ABCDEF'
for id in new_id:
    if 'A'<= id <= 'Z':
        id1 = chr(ord(id) - (ord('A') - ord('a')))
        new_id = new_id.replace(id, id1)
print(new_id)

new_id = 'ABCDEF'
new_id = new_id.lower()
print(new_id)

temp = 'hello, What are doing'
print(temp.split())

temp = '..fjeijfiege.1.'
temp = temp.strip('.')
print(temp[-1])
print(temp + 'a')

answer = '.'
if answer[0] == '.':
    answer = answer[1:] if len(answer) > 1 else '.'
if answer[-1] == '.':
    answer = answer[:-1]

print(answer)

a, b = set([1,2,3]), set([4,5,6])
print(a,b)

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

name = 'abekfei'
default = 'A' * len(name)
print(default)

i = []
print(sum(i))

from collections import deque
begin = 'abcd'
target = 'aghd'
q = deque()
    # begin과 타겟값의 다른 부분의 index 저장
for idx, (b,t) in enumerate(zip(begin, target)):
    if b != t:
        q.append(idx)

print(q)

a= [1,2]
c,d = a
print(c,d)

from collections import defaultdict
graph = defaultdict(list)
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["JFK","ABC"]]

for a,b in tickets:
    graph[a].append(b)
    graph[b]

print(graph)
print(graph['JFK'])
print(graph["IAD"])
print(graph)
graph['ICN'].append(False)
print(graph)
print(graph['ICN'][-1])

graph = defaultdict(list)
for a,b in tickets:
    graph[a].append(b)
    graph[b] # key가 목적지인 값 생성
for key in graph: # 방문 표시
    graph[key].append(False)

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["JFK","ABC"]]
for i,(s,e) in enumerate(tickets):
    print(i,s,e)

tickets = [["ABC","AAG"], ["ABC","ADG"]]
print(tickets)

if tickets[0] > tickets[1]:
    print("왼쪽이 더크다.")
else:
    print("왼쪽이 더작다")

def abc():
    return

g = abc()
print(g)

if not g:
    print("안빔")
else:
    print("빔")

print()
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["JFK","ABC"]]
routes = dict()

for (start, end) in tickets:
    print(routes.get(start))
    routes[start] = routes.get(start, []) + [end]  

print(routes)
routes['ICN'].insert(1,'DEF')
print(routes)

start = 1
from collections import deque
q = deque([start])
print(q)


for st_ in [{}, "number"]:
    try:
        int(st_)
    except ValueError as m:
        print(m)
    except TypeError as m:
        print(m)
    print("\n")

operations = ["I 16", "D 1"]
for i in operations:
    letter, num = i.split(' ')
    print(num)

if num == 1:
    print("맞아")

import heapq
a = [1,2,3,4,6,8,9]
heapq.heapify(a)
print(heapq.nlargest(1,a))
print(a)

h = [[1,7],[2,6],[3,5],[4,8]]
heapq.heapify(h)
heapq.heappop(h)
print(h)

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

a = '303030'
b = '333'
if a > b :
    print("303030이더큼")
else:
    print("333이 더큼")

print((int(a) > int(b)) - (int(a) < int(b)))
print(a+b)

from collections import Counter
num = "12324"
a = Counter(num)
b = dict(sorted(a.items()))
print(b)

hash("leo")
print(type(hash("leo")))

phoneBook = ["119", "97674223", "1195524421"]
phoneBook = sorted(phoneBook)
print(phoneBook)

# 문자열 비교 시 
a = '1234'
b = '32jrijgs'
if a == b[:len(a)]:
    print(1)
else:
    print(2)

 # 1. [ SET x 8 ] 초기화
    s = [ set() for x in range(8) ] 

N= 5
# 2. 각 set마다 기본 수 "N" * i 수 초기화
for i,x in enumerate(s, start=1):
    x.add( int( str(N) * i ) )

print(s)

a = [1,2,3]
for i in range(len(a)-1,-1,-1):
    print(a[i])

from itertools import permutations
# data = ['1', '2', '3']
data = '17' # 문자열은 리스트로 사용 가능

result = list(permutations(data,2))
print(result)
for resul in result:
    a = ''.join(resul) # join 함수는 str만 가능
    print(a, end = ' ')
print()
print(int('011'))

a = []
a.append(1)
a.append(2)
print(a)

a= set()

a = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

for index, (start, end) in enumerate(a):
    print(index, start, end)
a = 1
b = 2


print(min(a,b))

a, b = map(sorted, [[4,2],[3,1]])
print(a,b)

a = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
routes = list(map(sorted,a))
print('routes:',routes)

a = [-20,-46]
b = sorted(a)
print(b)

for i in range(1,0):
    print("sjofsjo")

a = 0

if not a:
    print('1')

a = [1,2,3,4,5]

if 3 in a:
    print("123242")

print(-1)
print(max(a))

a = '11192324'
b =  '119'
if a in b:
    print(252)

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
for ix, (g, p) in enumerate(zip(genres, plays)):
    print(ix, g, p)

c = [(1,5),(2,6),(3,8)]

n = 1141414
print(len(str(n)))
a = '136654'
print(a)
print(a.index(max(a[:6])))


a = 3
def g():
    global a
    a += 1

def f():
    global a
    a += 1
g()
print(a)

a = 1
while(a < 5):
    a += 1

print()
print()
print()
print()
print()
print()

a = 1
result = 0

def sum1(a,b):
    global result
    result += (a+b)

a = '1'
b = '2'
print(a>b)

a = set([1,2,3,45])
print(max(a))

a = [set() for _ in range(3)]
a[0].add(2)
a[0].add(2)
a[0].add(5)
print(a)

crit = 12345
n_str = list(map(int, str(crit)))
print(n_str)


for i in range(0):
    print(-1)

a = set()
a.add((123,1))
a.add((123, 1))
a.add((123,4))
print(a)

a = set()
if not a:
    print(-1)

def a():
    return -1
b = a()
print(b)

# size = 5
# while size:
#     size -= 1
#     print("메롱")
# import sys
# a = sys.stdin.readline().rstrip()
# print(list(a))



visited = [0] * 4
def d():
    visited[0] = 1
    
d()
print(visited)

import sys
from itertools import combinations as com

dice_idx = [0,1,2,3,4,5]

n1 = list(com(dice_idx,1))
n2 = list(com(dice_idx,2))
n3 = list(com(dice_idx,3))
size = [[] for _ in range(4)]

for i in range(1,4):
    size[i] += list(com(dice_idx,i))

a = [(1,2),(3,4),(4,5)]

if (1,2) in a:
    a.remove((1,2))

print(a)

a = '00009'
print(int(a))

a = (0,1)
b = (0,2)
c = (1,2)
d = (0,4)
e = (1,4)
if a < b:
    print(b)
if b < c:
    print(c)
if d < c:
    print(c)
else:
    print(d)

if c < e:
    print(e)


a = 'i s'
if ' ' in a:
    print(-1)

if 126:
    print(1)

log = 'abcdef : fefe'
f = 'abcdef : '

print(log.find(f))

if log.find(f) != -1:
    start = log.find(f) + len(f)
    print(log[start : ])

a= set()
a.add('a')
a.add('b')
a.add('a')
print(a)

a = ['g','b','a']
a.sort()
print(a)

a = 'B'
if a.isupper():
    print(a.lower())

print(a)

temp = [a.lower(),'a','@','e','c']
temp.sort()
print(temp)
a = ['!','a','b','c','d']
b = ['a','b']

print(b < a)

a = [['!', 'a', 'b', 'c', 'd'], ['b', 'c', 'd'], ['a'], ['!', 'e', 'i', 'l', 'n', 's', 'w']]
a.sort(key = len)
print(a)

a = ['bc','ba','a']
a.sort()
print(a)
a = '11'
b = '22'
print(a+b)
from collections import deque
q = deque()
if not q:
    print(-1)

# a = sys.stdin.readline().rstrip()
# b = list(a)
# b.sort()
# c = set(b)
# d = set(a)
# print(str(a))
# print(b)
# print(c)
# print(d)

a = '1'
a += 'bcd' * 0
print(a)
a = '12345'
b = a[::-1]
print(b)
print(len(a))
a = '89'
b = a[len(a)-1:-1:-1]
print(''.join(list(reversed(a))[1:]))

visited = [1,2,3,4,5]
def a():
    visited[1] = 200

a()
print(visited)
print(sorted((2,1)))
a = set() # 리스트가 들어갈수없다.
b = [[1,2],[2,3],[3,4]]
c = [(1,2),(2,3)]
a = (1,2)
print(a)
x,y = sorted((2,1))
print(x,y)

a= [[1,2],[2,3],[3,4]]
print(a[:])

a = 123
print(len(str(a)))

for x in range(4):
  if x == 2:
    print ('loop out')
    break
else:
  print ('loop end')

a = deque([3])
print(a)

a = [1,2]
def b():
    a[0] = 100
def c():
    global a
    a = [4,5,6]
b()
print(a)
c()
print(a)
a = ['abc']
if 'ab' in a:
    print(1)

a = {'a':1, 'b': 2}

if 'b' in a:
    print(1)

size = 9
size //= 3
print(size)
print()
for i in range(x,size*3,size):
    for j in range(y,size*3,size):
        print(size)

print()
# a = sys.stdin.readline().rstrip().strip('[]')
a = '[1,2,3,4]'
a = a.strip('[]')
print(a)
b = list(a.split(','))
b = a.split(',') # 위에 것과 같다.
print(b)
print(type(b))

a = [1,2,3,4]
print(a[::-1])
print(a[::1])

a = '[]'
a = a.strip('[]')
print(a)
a = a.split(',')

for i in a:
    print(i)
    print(type(i))

a = sys.stdin.readline().rstrip().split(',')
print(a)
print(list(a))