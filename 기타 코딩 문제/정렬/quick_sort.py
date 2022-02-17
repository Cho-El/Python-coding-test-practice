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
        if left >= right : # 엇갈리면 피벗의 값과 교체
            nums[right], nums[pivot] = nums[pivot], nums[right]
        else : # 엇갈리지 않고, left와 right이 정해지면 두 값을 교체
            nums[left], nums[right] = nums[right], nums[left]
    quick_sort(nums, start, right-1)
    quick_sort(nums, right+1, end)
    return nums

quick_sort(nums,0,len(nums)-1)
print(nums)

nums = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort2(nums):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(nums) <= 1:
        return nums

    pivot = nums[0] # 피벗은 첫 번째 원소
    tail = nums[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(nums))

nums = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort3(nums,start,end):
    if len(nums) <= 1:
        return
    pivot = nums[0]
    while start >= end:
        for i in range(start, len(nums)):
            if pivot <= nums[i]: # 왼쪽에서 오른쪽으로는 큰값
                left_index = i
                break
        for i in range(end, 1, -1): # 오른쪽에서 왼쪽으로는 작은 값
            if pivot >= nums[i]:
                right_index = i
                break
        if right_index < left_index:
            nums[right_index], nums[0] = nums[0], nums[right_index]
            quick_sort3(nums,0,right_index)
            quick_sort3(nums,right_index+1,right_index)

        else:
            nums[right_index],nums[left_index] = nums[left_index], nums[right_index]
            start += 1
            end -= 1
        
        
    