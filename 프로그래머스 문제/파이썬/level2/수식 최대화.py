#
'''
연산자의 종류가 최대 3개이므로 연산자 우선순위는 최대 6개까지 나올 수 있습니다. (3! = 6) 연산자 우선순위가 정해지면,
문자열의 앞에서부터 차례대로 우선순위가 빠른 연산자부터 찾아서 그 연산자와 양 옆의 숫자(피연산자) 2개를 제거하고 
계산된 결괏값을 대입하는 과정을 반복하면 됩니다.
이때 미리 입력으로 주어진 문자열에서 숫자와 연산자를 분리하여 각각의 배열에 보관해 놓으면 보다 
편하게 문제를 해결할 수 있습니다.
숫자에 대한 배열을 준비하고, 연산자에 대한 배열을 준비한 다음, 우선순위에 맞는 연산자의 인덱스를 연산자 배열에서 찾은 후 기억 합니다.
 그 후 숫자 배열에서 해당 인덱스와 다음 인덱스를 계산하는 방식을 이용하면 됩니다.
'''
# 분할정복 and 완전탐색
import sys, re
from itertools import permutations as pe
def solution(expression):
    sign = ['*','+','-']
    result = 0
    pe_signs = list(pe(sign,3))
    ex = re.split('[-|+|*]',expression)

    for pe_sign in pe_signs:
        for x in pe_sign:
            
        result = max(result, )
            
        

print(solution("100-200*300-500+20"))