# dp
import sys

# input = sys.stdin.readline
# t = int(input())
# n = int(input())
# sticker = []
# for i in range(2):
#     sticker.append(list(map(int, input().rstrip().split())))
    
t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))
