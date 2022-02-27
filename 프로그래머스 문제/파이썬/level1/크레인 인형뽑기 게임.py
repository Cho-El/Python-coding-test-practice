board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
def solution(board, moves):
    result = 0
    pocket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                pocket.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(pocket) > 1:
            if pocket[-1] == pocket[-2]:
                pocket.pop()
                pocket.pop()
                result += 2
            
    return result

print(solution(board, moves))
            