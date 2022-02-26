array = [1,5,2,6,3,7,4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def solution():
    result = []
    for start, end, k in commands:
        # start, end, k = command
        # temp = array[start-1:end]
        # temp.sort()
        # result.append(temp[k-1])
        result.append(list(sorted(array[start-1:end]))[k-1])
    print(result)

solution()



def solution2():
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))