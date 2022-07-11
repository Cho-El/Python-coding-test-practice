# dp 문제 같으면 다 써서 규칙을 찾아보자
import sys
input = sys.stdin.readline
n = int(input())
tree = [[]]
for _ in range(n):
	tree.append([i for i in map(int, input().rstrip().split())])

for i in range(1, n):
	tree[i + 1][0] = tree[i][0] + tree[i + 1][0]
	tree[i + 1][i] = tree[i][i-1] + tree[i + 1][i]
	for j in range(1,i):
		tree[i + 1][j] = tree[i + 1][j] + max(tree[i][j], tree[i][j - 1])

print(max(tree[n]))