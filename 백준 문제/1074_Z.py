# 분할 정복, 재귀
n,r,c = map(int, input().split)
dx = [0,1,0]
dy = [1,-1,1]
graph = [[0] * 2**n] * 2 **n
cnt = 0
def make_z(start):
    sx, sy = start
    graph[sx][sy] = cnt
    cnt += 1
    for i in range(3):
        nx = sx + dx[i]
        ny = sy + dy[i]
        graph[sx][sy] = cnt
        cnt += 1
    
    make_z()

def div_con(start_r, start_c, size):
    global cnt
    if size == 2:
        if start_r == r and start_c == c: # 2사분면
            print(cnt)
            return
        cnt += 1
        if start_r == r and start_c + 1 == c: # 1사분면
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c == c: # 3사분면
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c + 1 == c: # 4사분면
            print(cnt)
            return
        cnt += 1
    else:
        size //= 2
        div_con(start_r, start_c, size) # 2사분면
        div_con(start_r, start_c + size, size) # 1사분면
        div_con(start_r + size, start_c, size) # 3사분면
        div_con(start_r + size, start_c + size, size) # 4사분면

N, r, c = map(int, input().split())
cnt = 0

div_con(0, 0, 2 ** N)
