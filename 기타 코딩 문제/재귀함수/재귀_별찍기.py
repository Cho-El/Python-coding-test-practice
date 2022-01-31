import sys
sys.setrecursionlimit(10**6)

# N = int(input())

# stars = [['' for _ in range(N)] for _ in range(N)]
# def fill_star(n, x, y):
#     if n == 1 and x != -1: # 사이즈의 크기가 1이면 *을 삽입
#         stars[y][x] = '*'
#     next = n//3
#     for dy in range(3):
#         for dx in range(3):
#             if dx != 1 or dy != 1: # 중간 위치가 아니면 별을 삽입하는 함수 출력
#                 fill_star(next, x + dx * next, y + dy * next)
#             else:
#                 fill_star(next, -1, -1)

# fill_star(N,0,0)
# for i in stars:
#     print(''.join(i))

N = int(sys.stdin.readline().strip())
g = [['' for _ in range(N)] for _ in range(N)]

# def starprint(n):
#     div3 = n//3
#     if n == 3:
#         g[1] = ['*', ' ', '*']
#         g[0][:3] = g[2][:3] = ['*']*3
#         # g[0] = g[2] = ['*']*3
#         return
#     starprint(div3)

#     for i in range(0, n, div3):
#         for j in range(0, n, div3):
#             if i != div3 or j != div3:
#                 for k in range(div3):
#                     g[i+k][j:j+div3] = g[k][:div3]



# starprint(N)

# for i in range(N):
#     for j in range(N):
#         print(g[i][j], end = '')
#     print()

def append_star(n):
    if n == 1:
        return ['*']
    stars = append_star(n//3)
    L = []

    for S in stars:
        L.append(S*3)
    for S in stars:
        L.append(S + ' '*(n//3) + S)
    for S in stars:
        L.append(S*3)
    return L
a = append_star(N)
print(a)
for i in range(N):
    for j in range(N):
        print(a[i][j], end = '')
    print()

print('\n'.join(append_star(N)))