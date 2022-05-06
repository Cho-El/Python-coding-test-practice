# 문자열
import sys
# 1번 풀이 50점
# n = int(input())
# m = int(input())
# s = sys.stdin.readline().rstrip()
# target = 'I' + 'OI' * n
# cnt = 0
# for i in range(len(s) - len(target) + 1):
#     if s[i] == 'I':
#         if s[i:i + len(target)] == target:
#             cnt += 1

# print(cnt)

# 2번 풀이
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    print(i, S[i:])
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)