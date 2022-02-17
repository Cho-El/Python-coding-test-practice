nums = list(map(int,input("정렬할 숫자들을 입력해주세요 : ").split(' ')))

def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[i] < nums[j-1] :
                nums[i], nums[j-1] = nums[j-1], nums[i]
    return nums
	
# print(insert_sort(nums))

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

# 삽입 정렬2
def insert_Sort2(nums):
    for i in range(1,len(nums)):
        for j in range(i, 0, -1):
            if nums[j] > nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break

# 삽입 정렬 재귀 고민해보기
def recursion_insertion_sort(nums,n):
    # 종료조건
    if n == len(nums):
        return nums
    for i in range(n,0,-1):
        if nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        else:
            break
    return recursion_insertion_sort(nums,n+1)

# print(recursion_insertion_sort(nums,1))