import math
def solution(arrayA,arrayB):
    answer = 0
    gc,lc= 0,0
    se = []

    for i in range(len(arrayA)):
        gc = math.gcd(gc,arrayA[i])

    for i in range(len(arrayB)):
        lc = math.gcd(lc,arrayB[i])

    for j in range(len(arrayA)):
        if arrayA[j] % lc == 0:
            lc = 1
        if arrayB[j] % gc == 0:
            gc = 1

    if gc == 1 and lc ==1:
        return 0
    else:
        return max(gc,lc)

print(solution([10,17],[5,20]))
print(solution([10,20],[5,17]))
