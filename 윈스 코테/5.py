def solution(grids):
    result = []
    for grid in grids:
        black_boxes = []  # 검은색 상자들의 좌표
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'X':
                    black_boxes.append((i, j))

        if len(black_boxes) == 4:  # 검은색 상자가 4개면 ㅁ 모양 가능성이 있음
            # 4개의 상자가 직사각형 모양을 이루는지 확인
            xs = sorted([box[0] for box in black_boxes])
            ys = sorted([box[1] for box in black_boxes])
            if xs[0] == xs[1] and xs[2] == xs[3] and ys[0] == ys[1] and ys[2] == ys[3]:
                # 상자 사이에 흰색 상자가 있는지 확인
                white_boxes = [(i, j) for i in range(xs[0]+1, xs[2]) for j in range(ys[0]+1, ys[2])]
                if all([grid[i][j] == '.' for i, j in white_boxes]):
                    result.append(True)
                    continue
                
        result.append(False)
    return result

grids = [[".....", ".XXX.", ".X.X.", ".XXX.", "....."],
         ["XXXXX", "XXXXX", "XXX.X", "XXX.X", "XXXXX"],
         ["XXXXX", "X...X", "X.X.X", "X...X", "XXXXX"],
         ["....X", ".....", "XXX..", "X.X..", "XXX.."],
         [".......", "XXX.XXX", "X.X.X.X", "XXX.XXX", "......."],
         ["XXXXX", "XX.XX", "X...X", "XX.XX", "XXXXX"]]
print(solution(grids))