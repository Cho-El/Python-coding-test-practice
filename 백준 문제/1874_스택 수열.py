import sys
# 스택 자료구조
# 1번 풀이----------------------------------------

n = int(input())
stack = []
target = []
result = []
check = True
for i in range(n):
    target.append(int(input()))

now_num = 1
for i in range(0,len(target)):
    t = target[i]
    if stack and stack[-1] == t:
        stack.pop()
        result.append('-')
        continue
    
    if stack and stack[-1] > t:
        check = False
        break

    while now_num <= t:
        stack.append(now_num)
        result.append('+')
        now_num += 1

    stack.pop()
    result.append('-')

if check:
    for i in result:
        print(i)
else:
    print('NO')

"""
n까지 스택에 넣어주고
스택의 Top이 내가 찾는 값과 다르다면 바로 종료
"""
# 2번 풀이----------------------------------------
n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break               

if flag == 0:
    for i in answer:
        print(i)