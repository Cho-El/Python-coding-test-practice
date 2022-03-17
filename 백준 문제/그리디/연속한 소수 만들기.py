import math
T = int(input())
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
    max_num = 100000
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    answer = 0
    prime_num_list = []

    if a[0] != 1:
        for i in range(a[0], 1, -1):
            if is_prime_num(i):
                start = i
                break
    else:
        start = 2
    
    if a[-1] != 1:
        for i in range(a[-1], 100001):
            if is_prime_num(i):
                end = i
                break
    
    # start와 end 사이의 소수들 list에 삽입
    for i in range(start, end + 1):
        if is_prime_num(i):
            prime_num_list.append(i)
    
    if len(prime_num_list) < n: # 소수 리스트의 갯수가 n보다 적은 경우
        while(len(prime_num_list) != n):
            for i in range(prime_num_list[-1]+1, 100001):
                if is_prime_num(i):
                    prime_num_list.append(i)
                    if len(prime_num_list) == n:
                        break
        answer = penalty(prime_num_list, a)
    
    else:
        temp = prime_num_list[:n]
        answer = penalty(temp, a)
        for i in range(1, len(prime_num_list) - n + 1):
            temp = prime_num_list[i:i+n]
            answer = min(answer, penalty(temp, a))
    
    print(prime_num_list)
    print(answer)
            