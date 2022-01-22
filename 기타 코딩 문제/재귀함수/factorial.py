# 재귀함수와 메모화
def factorial_1(n): # 팩토리얼
    if n == 0:
        return 1
    return n*factorial_1(n-1)
print(factorial_1(4))

# 피보나치1 재귀 -> 숫자가 커질수록 계산량이 많아짐
def fibo1(n): 
    if n == 1 or n == 2:
        return 1

    return fibo1(n-1) + fibo1(n-2)

print(fibo1(5))

# 피보나치2 메모화를 통한 재귀 -> 숫자가 커질수록 계산량이 많아짐
memo = {1:1, 2:1}
def fibo2(n):
    if n in memo:
        return memo[n]
    else:
        output = fibo2(n-1) + fibo2(n-2)
        memo[n] = output
        return output

print(fibo2(10))

# fibo2 코드와 같지만 else를 없애고 조기리턴한 코드이다 요즘 추세
def fibo3(n): 
    if n in memo:
        return memo[n]
    output = fibo3(n-1) + fibo3(n-2)
    memo[n] = output
    return output