#
'''
연산자의 종류가 최대 3개이므로 연산자 우선순위는 최대 6개까지 나올 수 있습니다. (3! = 6) 연산자 우선순위가 정해지면,
문자열의 앞에서부터 차례대로 우선순위가 빠른 연산자부터 찾아서 그 연산자와 양 옆의 숫자(피연산자) 2개를 제거하고 
계산된 결괏값을 대입하는 과정을 반복하면 됩니다.
이때 미리 입력으로 주어진 문자열에서 숫자와 연산자를 분리하여 각각의 배열에 보관해 놓으면 보다 
편하게 문제를 해결할 수 있습니다.
숫자에 대한 배열을 준비하고, 연산자에 대한 배열을 준비한 다음, 우선순위에 맞는 연산자의 인덱스를 연산자 배열에서 찾은 후 기억 합니다.
 그 후 숫자 배열에서 해당 인덱스와 다음 인덱스를 계산하는 방식을 이용하면 됩니다.
 eval() 함수 -> string 수식계산을 가능하게함
 isdigit() -> str값이 숫자인지 파악
deque()는 deepcopy가 되지 않는다.
'''
# 1번 풀이 완전탐색
import sys, re
from itertools import permutations as pe
import copy
from collections import deque
def solution1(expression):
    array = ['*','+','-']
    result = 0
    ops = list(pe(array,3))
    # ex = re.split('[-|+|*]',expression)
    # expression을 숫자 수식으로 나누기
    temp = ''
    start = []
    for i in expression:
        if i.isdigit() == True:
            temp += i
        else:
            start.append(temp)
            start.append(i)
            temp = ''
    start.append(temp)
    
    answer = 0
    for op in ops:
        ex = deque(start)
        for i in op:
            q = deque()
            while ex:
                now = ex.popleft()
                if now == i:
                    num1 = q.pop()
                    num2 = ex.popleft()
                    q.append(str(eval(num1 + now + num2)))
                else:
                    q.append(now)
            ex = q
        answer = max(answer, abs(int(ex.pop())))

    
    return answer
            
print(solution1("100-200*300-500+20"))



# 2번 풀이 분할 정복
import re
from itertools import permutations as pe

def cal(ex,n,op):
    if n == 2:
        return str(eval(ex))
    else:
        if op[n] == '+':
            temp = []
            for e in ex.split('+'):
                temp.append(cal(e,n+1,op))
            result = str(eval('+'.join(temp)))
        if op[n] == '-':
            temp = []
            for e in ex.split('-'):
                temp.append(cal(e,n+1,op))
            result = str(eval('-'.join(temp)))
        if op[n] == '*':
            temp = []
            for e in ex.split('*'):
                temp.append(cal(e,n+1,op))
            result = str(eval('*'.join(temp)))
        
    return result

def solution2(expression):
    op = ['-','*','+']
    ops = pe(op,3)
    answer = 0
    for i in ops:
        answer = max(answer, abs(int(cal(expression,0,i))))
    return answer
print(solution2("100-200*300-500+20"))
