#
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = {}
for _ in range(n):
    address, num = input().rstrip().split()
    graph[address] = num

for _ in range(m):
    temp = input().rstrip()
    print(graph[temp])