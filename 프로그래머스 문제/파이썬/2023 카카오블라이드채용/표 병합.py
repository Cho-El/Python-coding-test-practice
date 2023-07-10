def solution(commands):
    index = [[(i, j) for j in range(51)] for i in range(51)]
    content = [["EMPTY" for _ in range(51)] for _ in range(51)]
    answer = []
    for command in commands:
        splitCommand = list(command.split(" "))
        # UPDATE 기능
        if splitCommand[0] == "UPDATE":
            # UPDATE r c value
            if len(splitCommand) == 4:
                com,r,c,value = splitCommand
                r, c = int(r), int(c)
                x, y = index[r][c]
                content[x][y] = value
            # UPDATE value1 value2
            else:
                com, v1, v2 = splitCommand
                for i in range(1,len(content)):
                    for j in range(1,len(content[0])):
                        if content[i][j] == v1:
                            content[i][j] = v2
        # MERGE r1 c1 r2 c2
        elif splitCommand[0] == "MERGE":
            com, r1, c1, r2, c2 = splitCommand
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            x1, y1 = index[r1][c1]
            x2, y2 = index[r2][c2]
            # (r2, c2)의 인덱스를 (r1, c1)으로 연결
            for i in range(1, len(content)):
                for j in range(1, len(content[0])):
                    if index[i][j] == (x2, y2):
                        index[i][j] = (x1, y1)
                        
            # (r1, c1)의 값으로 연결 EMPTY인 경우 r2, c2의 값을 가진다.
            
            if content[x1][y1] == "EMPTY":
                content[x1][y1] = content[x2][y2]
                
        # UNMERGE r c
        elif splitCommand[0] == "UNMERGE":
            # (r, c)셀 인덱스를 초기화
            com, r, c = splitCommand
            r,c = int(r), int(c)
            x, y = index[r][c]
            targetValue = content[x][y]
            for i in range(1, len(content)):
                for j in range(1, len(content[0])):
                    if index[i][j] == (x, y):
                        content[i][j] = "EMPTY"
                        index[i][j] = (i, j)
            content[r][c] = targetValue
            
        # PRINT r c
        else:
            com, r, c = splitCommand
            r,c = int(r), int(c)
            x, y = index[r][c]
            answer.append(content[x][y])
    
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))