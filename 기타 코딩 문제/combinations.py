from itertools import combinations as comb

nums = list(map(int, input("입력해주세요 : ").split()))
r = int(input("조합할 갯수를 정해주세요 : "))
print(nums)
print(r)

def combinations1(nums):
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                temp = (nums[i],nums[j],nums[k])
                result.append(temp)
    return result

# print(combinations1(nums))

def combination2(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        print("여기입니다:",chosen)
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        print(f"start는 {start}")
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

# print(combination2(nums,3))

def combinations3(arr, r):
    result = []
    if r == 0:
        return [[]]
    
    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        print(f"rest_arr : {rest_arr}")
        for C in combinations3(rest_arr,r-1):
            result.append([elem]+C)
            print(f"result : {result}")
    print(f"result_2 : {result}")        
    print("\n")
    return result

print(combinations3(nums,r))