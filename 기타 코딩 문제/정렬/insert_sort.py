nums = list(map(int,input("정렬할 숫자들을 입력해주세요 : ").split(' ')))

def insert_sort(nums):
	for i in range(1,len(nums)):
		for k in range(i, 0, -1):
			if nums[k-1] > nums[k]:
				nums[k-1], nums[k] = nums[k], nums[k-1]
	return nums
	
print(insert_sort(nums))

# 재귀함수
def insertionSortRecursive(arr,n):

    if n<=1:
        return
      
    insertionSortRecursive(arr,n-1)
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
  
    arr[j+1]=last
      
def printArray(arr,n):
    for i in range(n):
        print(arr[i])
  
arr = [12,11,13,5,6]
n = len(arr)
insertionSortRecursive(arr, n)
printArray(arr, n)