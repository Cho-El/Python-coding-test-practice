def solution(arr,brr):
	cnt = 0
	for i in range(len(arr)-1):
		if arr[i] != brr[i]:
			dif = brr[i] - arr[i]
			arr[i] += dif
			arr[i+1] -= dif
			cnt += 1
	return cnt
arr = [3,7,2,4]
brr = [4,5,5,2]
arr1 = [6,2,2,6]
brr1 = [4,4,4,4]

print(solution(arr1,brr1))
