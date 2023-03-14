import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]
result = [0 for _ in range(N)]

# increse
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and increase[i] < increase[j] + 1:
            increase[i] = increase[j] + 1

# decrease
for i in range(N-1, -1, -1):
    for j in range(i + 1, N):
        if A[i] > A[j] and decrease[i] < decrease[j] + 1:
            decrease[i] = decrease[j] + 1
    result[i] = decrease[i] + increase[i] - 1

print(max(result))