from copy import deepcopy

def solution(arr,k,t):
	global result
	result = []
	for i in range(k, len(arr) + 1):
		dfs(arr, i, t, 0, [])
	return len(result)

def dfs(arr, depth, t, startIdx, store):
	global result
	# 종료조건 depth가 0일때
	if depth == 0:
		if sum(store) <= t:
			temp = deepcopy(store)
			result.append(temp)
		return
	
	for i in range(startIdx, len(arr)): 
		store.append(arr[i])
		a = dfs(arr, depth - 1, t, i + 1, store)
		store.pop()

print(solution([2,5,3,8,1],3,11))
print(solution([1,1,2,2],2,3))
print(solution([1,2,3,2],2,2))
