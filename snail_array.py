num = int(input("배열의 크기를 설정해주세요 : "))
snail = [[0]*num for _ in range(num)]
cnt = num * num
i = 0
row, column = 0, -1
direction = 1
row_size, column_size = num, num


while i < cnt :
    for _ in range(column_size):
        column += direction
        i += 1
        snail[row][column] = i
    row_size -= 1
    
    for _ in range(row_size):
        row += direction
        i += 1
        snail[row][column] = i
    column_size -= 1
    direction *= -1

# list = []   
# for i in snail:
#     print(*i, sep = '   ')
#     print(i)
#     list.append(i)

for i in snail:
    for j in i:
        print(j, end = ' ')
    print()
    