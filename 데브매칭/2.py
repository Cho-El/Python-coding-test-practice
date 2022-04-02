from itertools import permutations
from collections import defaultdict


def solution(grid):
    width = len(grid[0])
    height = len(grid)

    gp = [list(i) for i in grid]
    cnt = 0
    for y in range(height):
        for x in range(width):
            if gp[y][x] == "?":
                gp[y][x] = cnt
                cnt += 1

    def change(li):
        temp = [[0] * width for _ in range(height)]
        cnt = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "?":
                    temp[y][x] = li[cnt]
                    cnt += 1
                else:
                    temp[y][x] = grid[cnt]
        return temp

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    def check(map):
        def bfs(y, x):
            stack = [(y, x)]
            visited[y][x] = 1

            while stack:
                y, x = stack.pop()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if (
                        0 <= ny < height
                        and 0 <= nx < width
                        and visited[ny][nx] == 0
                        and map[ny][nx] == temp
                    ):
                        visited[ny][nx] = 1
                        stack.append((ny, nx))

        dic = defaultdict(int)
        visited = [[0] * width for _ in range(height)]
        temp = ""
        for y in range(height):
            for x in range(width):
                if visited[y][x] == 0 and dic[map[y][x]] == 0:
                    temp = map[y][x]
                    dic[temp] = 1
                    bfs(y, x)
                elif visited[y][x] == 0 and dic[map[y][x]] == 1:
                    return False
        return True

    answer = 0
    for li in list(permutations(["a", "b", "c"], cnt)):
        temp = change(li)
        if check(temp):
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(["??b", "abc", "cc?"]))