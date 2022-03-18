import math
import time
import random
from bisect import bisect_left, bisect_right

T = int(input())

def eratoss(n):
    array = [True for i in range(n + 1)]
    result = []
    for i in range(2, int(math.sqrt(n)) + 1) :
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    for i in range(2, 100001):
        if array[i]:
            result.append(i)
    return result

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def penalty(X,Y):
    result = 0
    for x, y in zip(X,Y):
        result += abs(x - y)
    return result

for _ in range(T):
    n = int(input())
    # a = []
    # for i in range(n):
    #     t = random.randrange(1, 100000)
    #     a.append(t)

    a = list(map(int, input().split()))
    a.sort()
    answer = 0
    ts = time.time()
    # 4번 풀이
    prime_num_list = eratoss(100001) # True, False 담아져 있다.
    p_real = []

    # start
    if a[0] != 1:
        start = bisect_right(prime_num_list, a[0]) - 1
    else:
        start = 0
    
    
    # end
    end = bisect_left(prime_num_list, a[-1])

    if end - start + 1 < n: # 두 개 인덱스의 차가 n보다 작을 때
        end += n - end + start -1
        p_real = prime_num_list[start : end + 1]
        answer = penalty(p_real, a)

    else:
        p_real = prime_num_list[start : end + 1]
        temp = p_real[:n]
        answer = penalty(temp, a)
        for i in range(1, len(p_real) - n + 1):
            temp = p_real[i: i+n]
            answer = min(answer, penalty(temp, a))

    print(answer)
    # ------------------------------
    # te = time.time()
    # print('time:', te - ts)



    # 1번 풀이
    # if a[0] != 1:
    #     for i in range(a[0], 1, -1):
    #         if is_prime_num(i):
    #             start = i
    #             break
    # else:
    #     start = 2
    
    # if a[-1] != 1:
    #     for i in range(a[-1], 100001):
    #         if is_prime_num(i):
    #             end = i
    #             break
    
    # # start와 end 사이의 소수들 list에 삽입
    # for i in range(start, end + 1):
    #     if is_prime_num(i):
    #         prime_num_list.append(i)
    
    # if len(prime_num_list) < n: # 소수 리스트의 갯수가 n보다 적은 경우
    #     while(len(prime_num_list) != n):
    #         for i in range(prime_num_list[-1]+1, 100001):
    #             if is_prime_num(i):
    #                 prime_num_list.append(i)
    #                 if len(prime_num_list) == n:
    #                     break
    #     answer = penalty(prime_num_list, a)
    
    # else:
    #     temp = prime_num_list[:n]
    #     answer = penalty(temp, a)
    #     for i in range(1, len(prime_num_list) - n + 1):
    #         temp = prime_num_list[i:i+n]
    #         answer = min(answer, penalty(temp, a))

    # # 2번 풀이
    # if a[0] != 1:
    #     for i in range(a[0], 1, -1):
    #         if is_prime_num(i):
    #             start = i
    #             break
    # else:
    #     start = 2

    # if a[-1] != 1:
    #     for i in range(a[-1], 100001):
    #         if is_prime_num(i):
    #             end = i
    #             break

    # temp = eratoss(end)

    # for i in range(start, end + 1): # start와 end 사이의 모든 소수 담기
    #     if temp[i]:
    #         prime_num_list.append(i)
    
    # if len(prime_num_list) < n:
    #     for i in range(prime_num_list[-1]+1, 100001):
    #         if is_prime_num(i):
    #             prime_num_list.append(i)
    #             if len(prime_num_list) == n:
    #                 break
    #     answer = penalty(prime_num_list, a)
        
    # else:
    #     temp = prime_num_list[:n]
    #     answer = penalty(temp, a)
    #     for i in range(1, len(prime_num_list) - n + 1):
    #         temp = prime_num_list[i:i+n]
    #         answer = min(answer, penalty(temp, a))
 # 3번 풀이
   
    # -----------------------
    # prime_num_list = eratoss(100001) # True, False 담아져 있다.
    # p_real = []

    # # start
    # if a[0] != 1:
    #     for ix, p in enumerate(prime_num_list):
    #         if p <= a[0]:
    #             start = ix
    #         else:
    #             break
    # else:
    #     start = 0

    # # end
    # if a[-1] != 1:
    #     for ix, p in enumerate(prime_num_list):
    #         if p <= a[-1]:
    #             end = ix
    #         else:
    #             end = ix
    #             break

    # if end - start + 1 < n:
    #     end += n - end + start -1
    #     p_real = prime_num_list[start : end + 1]
    #     answer = penalty(p_real, a)

    # else:
    #     p_real = prime_num_list[start : end + 1]
    #     temp = p_real[:n]
    #     answer = penalty(temp, a)
    #     for i in range(1, len(p_real) - n + 1):
    #         temp = p_real[i: i+n]
    #         answer = min(answer, penalty(temp, a))