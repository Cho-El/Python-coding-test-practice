import sys
# 이분 탐색, 매개 변수 탐색
# 1번 풀이--------------------------------
k,n = map(int,input().split())
num = []
for i in range(k):
	num.append(int(input()))

max_n = max(num)
start = 1
end = max_n
while True:
    if start > end:
        answer = end
        break
    cnt = 0
    mid = (start + end)//2
    for n1 in num:
        cnt += n1//mid
    
    if cnt < n:
        end = mid-1
    
    if cnt >= n:
        start = mid + 1

print(answer)

# 2번 풀이--------------------------------

k,n = map(int,input().split())
num = []
for i in range(k):
	num.append(int(input()))

max_n = max(num)
start = 1
end = max_n
answer = 0
while start <= end:
    cnt = 0
    mid = (start + end)//2
    for n1 in num:
        cnt += n1//mid
    
    if cnt < n:
        end = mid-1
    
    if cnt >= n:
        start = mid + 1
        if answer < mid: # mid값이 필요한 전선의 최대 길이일 경우 answer에 저장한다.
            answer = mid

print(answer)