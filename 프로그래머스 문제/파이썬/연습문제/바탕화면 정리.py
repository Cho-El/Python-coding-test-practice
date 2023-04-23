#
import sys
def solution(wallpaper):
    answer = [50,50,0,0]
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                answer[0] = min(answer[0], x)
                answer[1] = min(answer[1], y)
                answer[2] = max(answer[2], x + 1)
                answer[3] = max(answer[3], y + 1)
    return answer

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))
