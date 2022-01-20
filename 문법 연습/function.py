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
# reverse(H), H를 찾아서 삭제
# pop() 마지막 자료를 찾아서 삭제
# extend() 추가적인 내용을 연장, append는 그대로넣지만(리스트 채로), extend의 경우 속성 분해 후 연결
# insert(x,y) : x번 인덱스에 y를 삽입
# copy.copy의 경우 얕은 복사로 메모리 주소만을 할당(단 string의 경우 값을 바꾸면 메모리 재할당이 일어난다. - immutable 객체)
# copy.deepcopy b = copy.deepcopy(a) 내부의 모든 객체들을 새롭게 copy해주며, a와 b 두개는 서로 영향을 받지않는다.
# list(combination(nums,3)) -> 조합 list로 뽑기

#초기화 방법