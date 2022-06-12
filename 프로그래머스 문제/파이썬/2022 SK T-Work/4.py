import sys
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(,k):
    q = deque()
    while q:   
        return

def solution(grid, k):
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = -1
    return answer

if __name__ == '__main__':
    grid = [['..FF','###F','###.'],
    ['..FF','###F','###.'],
    ['.F.FFFFF.F','.########.','.########F','...######F','##.######F','...######F','.########F','.########.','.#...####F','...#......']]
    k = [4,5,6]

    for grid, k in zip(grid, k):
        print(solution(grid, k))