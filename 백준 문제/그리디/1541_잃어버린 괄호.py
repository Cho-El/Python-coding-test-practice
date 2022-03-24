import sys
# strings = sys.stdin.readline().rstrip()
# num = []
# result = 0

# start = 0
# for i in range(len(strings)):
#     if strings[i] == '-':
#         end = i
#         num.append(strings[start:end])
#         start = end + 1

# num.append(strings[start:])

# for i in range(len(num)):
#     start = 0
#     sum_n = 0
#     for j in range(len(num[i])):
#         if num[i][j] == '+': 
#             end = j
#             sum_n += int(num[i][start:end])
#             start = end + 1
#     sum_n += int(num[i][start:])
#     num[i] = sum_n

# for ix, v in enumerate(num):
#     if ix == 0:
#         result += v
#     else:
#         result -= v

# print(result)

## 2번째 풀이
strings = sys.stdin.readline().rstrip().split('-')
num = []

for string in strings:
    cnt = 0
    temp = string.split('+')
    for j in temp:
        cnt += int(j)
    num.append(cnt)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)