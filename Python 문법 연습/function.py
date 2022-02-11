import math
# enumerate -> 순서와 리스트의 값을 전달하는 기능 _> 튜플형태로 만들어줌
names = ['철수', '영희', '영수']
for i, name in enumerate(names):
  print('{}번: {}'.format(i + 1, name))
#   print(f'{i+1}번 : {name}')

# map
# math.pow(제곱), math.

# round 반올림 함수
# a = [] 리스트, append
# b = {} 딕셔너리, 
# max 최댓값
# min 최솟값
# sorted 원본 리스트에 영향을 주지 않고, 정렬된 새로운 리스트 반환
# list 함수
# sort 원본 리스트에 영향을 주고, 해당 리스트 순서를 정렬해 줌, 값 반환은 하지않음
# (기본 default는 오름차순, reverse=True 옵션을 통해 내림 차순 가능)
# reverse(list) -> list를 뒤집어준다. ex) list = [a,b,c] -> list = [c,b,a]
# reversed() -> reversed 객체를 반환하며, 시퀀셜하지 않은 딕셔너리를 제외한 타입을 지원한다. 
# pop() 마지막 자료를 찾아서 삭제
# extend() 추가적인 내용을 연장, append는 그대로넣지만(리스트 채로), extend의 경우 속성 분해 후 연결
# insert(x,y) : x번 인덱스에 y를 삽입
# copy.copy의 경우 얕은 복사로 메모리 주소만을 할당(단 string의 경우 값을 바꾸면 메모리 재할당이 일어난다. - immutable 객체)
# copy.deepcopy b = copy.deepcopy(a) 내부의 모든 객체들을 새롭게 copy해주며, a와 b 두개는 서로 영향을 받지않는다.
# list(combination(nums,3)) -> 조합 list로 뽑기

# index 함수 -> 리스트 중에서 특정한 원소가 몇 번째 처음으로 등장했는지를 알려준다.
a = [1,2,3,4,5,6,7,8,9,10]
print(a.index(5))

#join()
l = ['a', 'b', 'c']
''.join(reversed(l))  # 'cba'

#초기화 방법

#수행 시간 측정 코드
import time
start = time.time()
end = time.time()
print("time : ", end - start)

# abs 함수 -절대값 함수
a = abs(-22)

# map 함수
'''
함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형을 첫 번째 인자로 들어온
함수에 하나씩 집어넣어서 함수를 수행하는 함수이다.

ex)
map(적용시킬 함수, 적용할 값들)

'''

# filter 함수
'''
filter(함수, 리스트)형태 -> list안에 인자들을 함수를 통해 걸러줌
'''
list(filter(lambda x: x < 5, range(10)))