nums = list(map(int, input("입력해주세요 : ").split()))
print(nums)

def combinations(nums):
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                temp = (nums[i],nums[j],nums[k])
                result.append(temp)
    return result

print(combinations(nums))