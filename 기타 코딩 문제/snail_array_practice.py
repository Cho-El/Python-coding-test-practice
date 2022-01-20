# #달팽이 문제
# num = int(input("숫자를 입력해 : "))
# num2 = int(input("숫자를 입력해 : "))

# n, m = map(int, input().split())

# class Giraffes :
#     def __init__(self, spots):
#         self.giraffe_spots = spots
#         self.l2 = 3
#     def spp(self, spot):
#         self.giraffe_spots = spot
#         self.l1 = spot
#         self.l3 = "메롱"
#         # self.l2 = self.l1*2
        

# a = Giraffes(100)
# b = Giraffes(150)
# c = Giraffes(180)
# d = Giraffes(190)

# c.spp(20)
# print(c.l3)
# print(a.giraffe_spots)
# print(b.giraffe_spots)
# print(c.giraffe_spots)
# print(d.giraffe_spots)

# n = 0    # 숫자 1, 2, 3, ...
# step = 1 # 증가/감소 크기: 1, -1
# y = 0    # 줄 위치
# x = -1   # 칸 위치 (배열 선두보다 한칸 앞)
# size = 5 # 배열 크기 (5*5 배열)
# arr = [[0]*size for i in range(size)]   # 2차원 배열 구조
 
# while True:
#     for _ in range(size):  # 몇 칸 진행할까 인덱스가 필요없는 for문에 _가 쓰임
#         n += 1
#         x += step
#         arr[y][x] = n
#     size -= 1
#     if size < 1:  # 출력할 게 없으면 종료
#         break
#     for _ in range(size):  # 몇 줄 진행할까
#         n += 1
#         y += step
#         arr[y][x] = n       
#     step = -step  # 증감 방향을 반대로      
   
# # 2차원 리스트 출력하기
# for line in arr:
#     for n in line:
#         print('%3d'%n, end = '')
#     print()

# n = int(input("N의 값을 입력해주세요 : "))
# arr = [[0]*n for _ in range(n)]
# row_size = n
# column_size = n

# 1번 방법
n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
row, column, cnt = 0, -1, 0
row_size, column_size = n, m
step = 1
 
while row_size and column_size:
    for _ in range(column_size):    # fill column_index
        cnt += 1
        column += step
        arr[row][column] = cnt
 
    row_size -= 1
 
    for _ in range(row_size):    # fill row_index
        cnt += 1
        row += step
        arr[row][column] = cnt
 
    column_size -= 1
    step = -step    # switch direction
 
for i in arr:
    print(*i, ' ')