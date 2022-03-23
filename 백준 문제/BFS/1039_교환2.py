import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
q = deque([n])

# 두번째 풀이, bfs함수르 k번 만큼

def bfs():
	visited = set()
	size = len(q)
	while size:
		size -= 1
		num = q.popleft()
		n_str = list(str(num))
		for i in range(len(n_str) - 1):
			for j in range(i+1, len(n_str)):
				if i == 0 and n_str[j] == '0': continue

				n_str[i], n_str[j] = n_str[j], n_str[i]
				real_n = int(''.join(n_str))
				if real_n not in visited:
					visited.add(real_n)
					q.append(real_n)
				n_str[i], n_str[j] = n_str[j], n_str[i]
				
	if not visited:
		return -1
	answer = max(visited)
	return answer


while k:
	k-= 1
	answer = bfs()

print(answer)

# from collections import deque

# n,k = input().strip().split()
# size = len(n)
# n,k = map(int, [n,k])

# def solv():
#     answer = 0
#     visited = set()

#     q = deque([(n,0)])
#     while q:
#         now,cnt = q.pop()
#         if cnt == k:
#             answer = max(answer, now)
#             continue

#         arr = list(map(int, str(now)))
#         for i in range(size-1):
#             for j in range(i+1,size):
#                 if i == 0 and arr[j] == 0: continue 
#                 arr[i],arr[j] = arr[j],arr[i]
#                 num = list_to_int(arr)
#                 if num+cnt+1 not in visited:
#                     q.appendleft((num,cnt+1))
#                     visited.add(num+cnt+1)
#                 arr[i],arr[j] = arr[j],arr[i]
#     print(answer if answer > 0 else -1)
    
# def list_to_int(arr):
#     result = 0
#     for num in arr:
#         result = result*10+num
#     return result
# solv()