'''
행복 왕국의 왕실 정원은 체스판과 같은 8X8 좌표 평면입니다.
왕실 정원의 특정한 한 칸에 나이트가 서 있습니다.
나이트는 매우 충성스러운 신호로서 매일 무술을 연마합니다.

나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는
나갈 수 없습니다.

나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
1. 수평으로 두칸 이동한 뒤 수직으로 한 칸 이동
2. 수직으로 두칸 이동한 뒤 수평으로 한 칸 이동

좌표 평면상에 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을
작성하세요. 왕실의 정원에서 행 위치를 표현할 때는 1~8로 표현하며, 열 위치의 경우 a~h로 표현합니다.

ex)
a1
출력 2
c2
출력 6
'''
start = input("위치를 입력해주세요 : ")
def knight(start):
    x = [1,2,3,4,5,6,7,8]
    y = ['a','b','c','d','e','f','g','h']
    
    # 8가지로 움직일 수 있다. LLU, LLD, RRU, RRD, UUL, UUR, DDL, DDR
    dx = [-1,1,-1,1,-2,-2,2,2]
    dy = [-2,-2,2,2,-1,1,-1,1]
    cnt = 0

    ix = x.index(int(start[1])) # start의 x인덱스
    iy = y.index(start[0]) # start의 y인덱스

    for i in range(8):
        nx = ix + dx[i]
        ny = iy + dy[i]
        if nx >= 0 and ny >= 0 and nx <= 7 and ny <= 7 :
            cnt += 1
    return cnt

print(knight(start))

def knight2(start):
    row = int(start[1]) # 행 1,2,3,4,5,6 ... 으로 표현
    col = int(ord(start[0])) - int(ord('a')) + 1 # 영어 a,b,c,d를 1,2,3,4로 표현
    result = 0 # 경우의 수

    steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)] # 8가지 방향에 대한 경우의 수

    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]
        if next_row >=1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            result += 1
    
    return result

print(knight2(start))