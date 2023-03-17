#
import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

end = 0
result = 0
sumArr = 0
for start in range(n):
    while end < n:
        if sumArr < m:
            sumArr += arr[end]
            end += 1
        else:
            break
    
    if sumArr == m:
        result += 1
        
    sumArr -= arr[start]
    
print(result)