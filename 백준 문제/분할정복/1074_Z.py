# 분할 정복, 재귀
import sys
sys.setrecursionlimit(10 ** 6)

def div_con(start_r, start_c, size):
    global cnt
    if size == 2:
        if start_r == r and start_c == c:
            print(cnt)
            return
        cnt += 1
        if start_r == r and start_c + 1 == c:
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c == c:
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c + 1 == c:
            print(cnt)
        cnt += 1
    else:
        size //= 2
        div_con(start_r, start_c, size)
        div_con(start_r, start_c + size, size)
        div_con(start_r + size, start_c, size)
        div_con(start_r + size, start_c + size, size)

def div_con2(r, c, size):
    global answer
    size //= 2
    if r == 0 and c == 0:
        return 0
    if r == 0 and c == 1:
        return 1
    if r == 1 and c == 0:
        return 2
    if r == 1 and c == 1:
        return 3
    
    if r < size and c < size: # 2사분면
        return div_con2(r, c,size)
    elif r < size and c >= size: # 1사분면
        return size ** 2 + div_con2(r, c - size,size)
    elif r >= size and c < size: # 3사분면
        return size **2 * 2 + div_con2(r - size, c,size)
    elif r >= size and c >= size: # 4사분면
        return size ** 2 * 3 + div_con2(r - size, c - size, size)
    



N, r, c = map(int, input().split())
cnt = 0

# div_con(0, 0, 2 ** N)
print(div_con2(r, c, 2 ** N))
