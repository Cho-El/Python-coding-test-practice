from itertools import permutations
import heapq
def solution2(numbers):
    numbers = list(map(str, numbers)) # string화
    result = list(map(''.join,permutations(numbers,len(numbers))))
    heapq.heapify(result)
    result = heapq.nlargest(1,result)[0]
    return result


def solution(numbers):
    h = []
    result = ''
    numbers = list(map(str, numbers)) # string화
    for number in numbers:
        heapq.heappush(h, (-int(number[0]),number))
    while h:
        result += heapq.heappop(h)[1]

    return result

'''
lambda x : x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다. 
x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
이 문제의 핵심이라고 할 수 있다. 
문자열 비교는 ASCII 값으로 치환되어 정렬된다. 따라서 666, 101010, 222의 첫번째 인덱스 값으로 비교한다. 
6 = 86, 1 = 81, 2 = 82 이므로 6 > 2 > 1순으로 크다. 
'''
def solution3(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution4(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    print(n)
    answer = str(int(''.join(n)))
    return answer

print(solution4([6, 10, 2]))
