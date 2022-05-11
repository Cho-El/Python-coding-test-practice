def rotate(rc):
    column = len(rc) # 행
    row = len(rc[0]) # 열
    column_dir = 1
    row_dir = 1
    x = 0
    y = 0
    store = rc[x][y]
    for i in range(2):
        # 열로 이동
        for j in range(row - 1):
            store, rc[x][y + row_dir] = rc[x][y + row_dir], store
            y += row_dir
        row_dir *= -1
        # 행으로 이동
        for j in range(column - 1):
            store, rc[x + column_dir][y] = rc[x + column_dir][y], store
            x += column_dir
        column_dir *= -1
    return

def shiftrow(rc):
    column_size = len(rc)
    for i in range(column_size - 1, 0, -1):
        rc[i], rc[i-1] = rc[i-1], rc[i]
    return
def solution(rc, operations):

    for op in operations:
        if op == 'Rotate':
            rotate(rc)
        else:
            shiftrow(rc)
    
    return rc

if __name__ == '__main__':
    rc = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[8, 6, 3], [3, 3, 7], [8, 4, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    
    operations = [["Rotate", "ShiftRow"],
    ["Rotate", "ShiftRow", "ShiftRow"],
    ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]]

    for rc, operations in zip(rc, operations):
        print(solution(rc,operations))