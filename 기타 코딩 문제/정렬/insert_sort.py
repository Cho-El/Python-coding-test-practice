nums = list(map(int,input("정렬할 숫자들을 입력해주세요 : ").split(' ')))

def insert_sort(nums):
	for i in range(1,len(nums)):
		for k in range(i, 0, -1):
			if nums[k-1] > nums[k]:
				nums[k-1], nums[k] = nums[k], nums[k-1]
	return nums
	
print(insert_sort(nums))