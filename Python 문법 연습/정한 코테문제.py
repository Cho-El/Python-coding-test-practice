import time
def nCr(n, r):
    a = 1
    b = 1
    for i in range(r):
        a *= n - i
        b *= r - i
    return int(a/b)

def solution(n):
    bin_n = bin(n)
    cnt_one = 0
    result = 0

    for i in range(len(bin_n)-1,1,-1):
        if bin_n[i] == '1':
            cnt_one += 1 # 지금까지 찾은 1의 갯수
            result += nCr(len(bin_n)-i-1, cnt_one)

    return result

start = time.time()
print(solution(10))
end = time.time()
print(end - start)

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 5)


def solution(n):
    # 효율성 통과 못함
    # 제출한 답
    # temp = bin(n).count("1")
    # cnt = 0
    # for i in range(1, n):
    #     if temp == bin(i).count("1"):
    #         cnt += 1
    # return cnt

    # 새로 푼 답
    global cnt, one_cnt, temp, dic
    dic = defaultdict(int)
    cnt = 0
    temp = format(n, "b")
    one_cnt = temp.count("1")
    dfs("", 0)
    return cnt


def dfs(str, n):
    global cnt, one_cnt, temp, dic
    if len(str) > len(temp) or n > one_cnt:
        return
    if n == one_cnt and int(str) < int(temp) and dic[int(str)] == 0:
        dic[int(str)] = 1
        cnt += 1
        return
    dfs(str + "0", n)
    dfs(str + "1", n + 1)