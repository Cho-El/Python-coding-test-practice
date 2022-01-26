# nums = list(map(int,input("정렬할 숫자들을 입력해주세요 : ").split(' ')))
nums = [1,10,5,8,7,6,4,3,2,9]
def quick_sort(nums, start, end): # start와 end는 인덱스 값
    if start >= end: # 원소가 1개인 경우
        return
    pivot = start
    left = start + 1
    right = end
    while(left < right): # 엇갈릴 때 까지 반복
        while(nums[left]<= nums[pivot] and left < end):
            left += 1
        while(nums[right]>=nums[pivot] and right > pivot):
            right -= 1 
        if left >= right :
            nums[right], nums[pivot] = nums[pivot], nums[right]
        else :
            nums[left], nums[right] = nums[right], nums[left]
    quick_sort(nums, start, right-1)
    quick_sort(nums, right+1, end)

quick_sort(nums,0,len(nums)-1)
print(nums)