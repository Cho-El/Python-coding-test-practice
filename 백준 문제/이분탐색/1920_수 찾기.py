import sys
# 이진 탐색, 자료형
# 1번 풀이------------------------------------------- 
n = int(input())
listn = list(map(int,sys.stdin.readline().split()))
listn.sort()

m = int(input())
listm = list(map(int,sys.stdin.readline().split()))

def binary_search(listn, v):
    start = 0
    end = len(listn)-1
    check = 0
    
    while start <= end: # start와 end가 같을 때도 검사를 해봐야됨 -> start와 end mid 세 값이 모두 같은데 이 값을 확인안하고 넘어가면 안되므로
        mid = (start + end) // 2
        if listn[mid] == v:
            check = 1
            break

        elif listn[mid] < v:
            start = mid + 1

        else:
            end = mid - 1
    
    print(check)

for i in listm:
    binary_search(listn, i)        