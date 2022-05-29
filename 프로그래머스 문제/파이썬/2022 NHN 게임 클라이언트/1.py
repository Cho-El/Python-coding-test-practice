import sys
from collections import defaultdict
from collections import deque
def overlap_check(arr):
    arr.sort()
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: # 중복이 있는 경우
                return True
    
    return False
def solution(cards1, cards2):

    answer = 0
    # 라운드별 
    for round in range(len(cards1)):
        sum_list = cards1[round] + cards2[round]

        # 10장 중에서 중복되는 번호 체크
        if overlap_check(sum_list):
            answer += 1
        else: # 10장 중 중복이 없는 경우 한 플레이어가 직전 라운드에서 받은 카드와 비교
            if round != 0:
                prev_dict1 = defaultdict(int)
                prev_dict2 = defaultdict(int)
                for c1, c2 in zip(cards1[round-1], cards2[round-1]):      
                    prev_dict1[c1] += 1
                    prev_dict2[c2] += 1

                cnt = 0
                for c1 in cards1[round]:
                    if c1 in prev_dict1:
                        cnt += 1
                    if cnt == 2:
                        answer += 1
                        break

                if cnt != 2:
                    cnt = 0
                    for c2 in cards2[round]:
                        if c2 in prev_dict2:
                            cnt += 1
                        if cnt == 2:
                            answer += 1
                            break

    return answer

if __name__ == '__main__':
    cards1 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],[[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]]
    cards2 = [[[5, 7, 9, 11, 13], [11, 13, 15, 17, 19]],[[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]]
    for cards1, cards2 in zip(cards1, cards2):
        print(solution(cards1, cards2))
