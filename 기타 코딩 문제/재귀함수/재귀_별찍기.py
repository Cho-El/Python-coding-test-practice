N = int(input())

stars = [['' for _ in range(N)] for _ in range(N)]
def fill_star(n, x, y):
    if n == 1 and x != -1: # 사이즈의 크기가 1이면 *을 삽입
        stars[y][x] = '*'
    else:
        stars
    next = n//3
    for dy in range(3):
        for dx in range(3):
            if dx != 1 or dy != 1: # 중간 위치가 아니면 별을 삽입하는 함수 출력
                fill_star(next, x + dx * next, y + dy * next)
            else:
                fill_star(next, -1, -1)

fill_star(N,0,0)
for i in stars:
    print(''.join(i))

def starprint(n):
    if n == 3:
        return [['*','*','*'],['*',' ','*'],['*','*','*']]