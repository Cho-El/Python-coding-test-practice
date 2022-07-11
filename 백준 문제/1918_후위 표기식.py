# 스택
import sys
input = sys.stdin.readline
exps = input().rstrip()
result = ''
prior = {'*':2, '/':2, '+':1, '-':1, '(':0, ')':0}
stack = []

for exp in exps:
    if exp.isalpha():
        result += exp
    else:
        # ( 이 올때
        if exp == '(':
            stack.append(exp)
        # ) 이 올때
        elif exp == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        # 다른 기호가 올때
        else:
            while stack and prior[stack[-1]] >= prior[exp]:
                result += stack.pop()
            stack.append(exp)

while stack:
    result += stack.pop()

print(result)