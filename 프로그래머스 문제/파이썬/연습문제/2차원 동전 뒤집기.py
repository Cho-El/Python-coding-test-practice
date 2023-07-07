def make_list(lst, row, col) :
    result = list()
    for i in range(row) :
        result.append(sum([(1 << j) * lst[i][j] for j in range(col)]))
    return result

def flip(lst, flip_chk, row, col) :
    result = list()

    for i in range(row) :
        if flip_chk & (1 << i) :
            result.append((1 << col) - lst[i] - 1)
        else :
            result.append(lst[i])
    for i in range(col) :
        if flip_chk & (1 << (row + i)) :
            for j in range(row) :
                result[j] ^= (1 << i)
    return result

def solution(beginning, target):
    row, col = len(beginning), len(beginning[0])
    
    beginning_list = make_list(beginning, row, col)
    target_list = make_list(target, row, col)
        
    test_case = list(range(1 << (row + col)))
    test_case.sort(key = lambda x : bin(x).count('1'))
    for i in test_case:
        print(bin(i))
    for i in test_case :
        fliped_list = flip(beginning_list, i, row, col)
        cnt = bin(i).count('1')
        if fliped_list == target_list :
            return cnt
    
    return -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],
         [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))