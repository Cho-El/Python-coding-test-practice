'''
1. itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공합니다.
	- 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용됩니다.
2. heapq : 힙 자료구조를 제공합니다.
	- 일반적으로 우선순위 큐 기능을 구현하기 위해 사용됩니다.
3. collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함합니다.
4. math : 필수적인 수학적 기능을 제공합니다.
	- 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수를 포함
백슬래쉬로 코드 여러 줄로 나눌 수 있음
컨 k f로 자동정렬 가능
컨 shift L로 같은 변수명 여러 개를 동시에 변경이 가능
알트 쉬프트 드래그로 그 줄 한번에 변경 가능
'''
# 0. 내장함수 -------------------------------------------------
# sum()
# min(), max()
# eval()
result = eval("(3+5)*7")
#sorted

# 1. itertools 라이브러리-----------------------------------
'''
순열 : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
조합 : 'AB', 'AC', 'BC'
'''
# 순열
from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data,3))
print(result)

# 조합
from itertools import combinations

result = list(combinations(data, 2))
print(result)

# 중복 순열
from itertools import product

result = list(product(data, repeat = 2))
print(result)

# 중복 조합
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
print(result)

# 2. collections 라이브러리
# ----------------------------------------------------------------------
# Counter -> iterable 객체 내부 원소가 몇 번씩 등장했는지를 알려준다.
from collections import Counter
counter = Counter(['red','red','red','blue','blue','blue','blue','green'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))
print(counter)
print(list(counter)) # 횟수가 안뜬다 counter를 쓸 경우 dict을 사용하자.

# 3. math 라이브러리
# 최대공약수와 최소공배수
import math

def lcm(a, b):# 최소 공배수
	return a*b//math.gcd(a,b)
print(math.gcd(21,14))
print(lcm(21,14))