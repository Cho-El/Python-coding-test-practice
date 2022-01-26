nums = list(map(int,input("정렬할 숫자들을 입력해주세요 : ").split(' ')))

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if nums[j] > nums[j+1] :
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

print(bubble_sort(nums))