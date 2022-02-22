
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
