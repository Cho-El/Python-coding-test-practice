from collections import deque
import sys

def solution(queue1, queue2):
    # 투포인터
    target_num = (sum(queue1) + sum(queue2)) // 2
    total_q = queue1 + queue2

    now_sum = 0
    end = 0
    result_array = []
    answer = sys.maxsize

    for start in range(len(total_q)):
        while now_sum <  target_num and end < len(total_q):
            now_sum += total_q[end]
            end += 1
        if now_sum == target_num:
            result_array.append((start, end))
        now_sum -= total_q[start]
    
    if result_array:
        for start, end in result_array:
            if start < len(total_q) // 2:
                if end >= len(total_q) // 2:
                    moving = start + end - len(total_q) // 2
                    answer = min(moving, answer)
                else:
                    moving = start
                    answer = min(moving, answer)

            else:
                moving = end - start + len(total_q) // 2 + 2 * (start - len(total_q) // 2)
                answer = min(moving, answer)
    else:
        return -1
    
    return answer
    
if __name__ == '__main__':
    a = [([3, 2, 7, 2],[4, 6, 5, 1]	),([1, 2, 1, 2],[1, 10, 1, 2]), ([1, 1], [1, 5])]
    for i in a:
        q1, q2 = i
        print(solution(q1, q2))