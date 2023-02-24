import sys

n, b = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

# 행렬 곱하기(A*A) 알고리즘
def mul(n,a,b):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

# 1629 곱셈 문제와 같은 형식
def cal(n,b,A):
    if b == 1:
        return A
    # 단순 2제곱일 경우
    elif b == 2:
        return mul(n,A,A)
    else:
        temp = cal(n, b // 2, A)
        # b가 짝수일 경우 제곱수를 계속 곱하면 된다.
        # AAAA = ((A^2)^2)
        if b % 2 == 0:
            return mul(n,temp,temp)
        # b가 홀수일 경우 마지막에 A를 곱해줘야한다.
        # AAAAA = ((A^2)^2)*A
        else:
            return mul(n,mul(n,temp,temp),A)

result = cal(n,b,A)

for row in result:
    for num in row:
        print(num % 1000,end= ' ')
    print()
