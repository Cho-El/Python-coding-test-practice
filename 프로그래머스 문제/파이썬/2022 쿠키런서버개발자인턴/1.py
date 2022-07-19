def solution(openA, closeB):
    answer = 0
    close_start_time = 0
    while closeB:
        if openA:
            if close_start_time == 0:
                start = openA.pop(0)
            else:
                start = openA.pop(0)
                while close_start_time > start and openA:
                    start = openA.pop(0)
                
                if close_start_time > start:
                    break
        
        else:
            break
        close = closeB.pop(0)
        while start > close:
            close = closeB.pop(0)

        close_start_time = close
        answer += close - start

    return answer

if __name__ == '__main__':
    openA = [[3,5,7], [4,7,9,16],[10,11],[10]]
    closeB = [[4,10,12],[2,5,12,14,20],[1,2,3,4,16],[11,500]]
    for o,c in zip(openA, closeB):
        print(solution(o, c))