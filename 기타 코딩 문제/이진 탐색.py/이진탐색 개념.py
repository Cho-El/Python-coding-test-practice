'''
- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
ex) 선택 정렬
- 이진 탐색 : 정렬되어 있는 리스테에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
- 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
'''

target = 
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

