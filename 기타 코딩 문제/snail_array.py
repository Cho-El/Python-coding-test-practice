num = int(input("배열의 크기를 설정해주세요 : "))
snail = [[0]*num for _ in range(num)]
print(snail)
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

arr = [1,2,3,4,5,6,7,8]
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr) # 초기화
    print(c)
    c = [0 for _ in range(len(arr))]
    print(c)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
permute(arr)
print(list(range(4)))