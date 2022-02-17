'''
- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
ex) 선택 정렬
- 이진 탐색 : 정렬되어 있는 리스테에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
- 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
'''

target = int(input('숫자를 입력해주세요 : '))
array = [0,2,4,6,8,9,10,12,14,16,18]
def binary_search(array, target, start, end):
	if start > end : 
		return None
	mid = (start + end)//2
	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binary_search(array,target,start,mid-1)
	else:
		return binary_search(array,target,mid+1,end)


if binary_search(array, target, 0, len(array)) != None:
	print(f"{array[binary_search(array, target, 0, len(array))]}가 있습니다.")

else:
	print("없음")


'''
파이썬 이진 탐색 라이브러리
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
사용법
from bisect import bisect_left, bisect_right
'''

'''
값이 특정 범위에 속하는 데이터 개수 구하기
'''

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
	right_index = bisect_right(a, right_value)
	left_index = bisect_left(a, left_value)

	return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

'''
파라메트릭 서치
-> 이진탐색을 이용한 문제에서 보통 사용함
- 파라메트릭 서치란 최적화 문제를 결정 문제('예' or '아니오')로 바꾸어 해결하는 기법입니다.
ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있습니다.
'''

''