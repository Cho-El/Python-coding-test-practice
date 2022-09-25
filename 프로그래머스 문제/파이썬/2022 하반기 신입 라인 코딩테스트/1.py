from typing import List

def solution(queries: List[List[int]]) -> int:
    answer = 0
    array_dic = {}
    for q in queries:
        arr_num,add_cnt = q
        if arr_num in array_dic:
            Element, max_array = array_dic[arr_num]
            if Element + add_cnt > max_array:
                answer += Element
                new_arr_size = 1
                while Element + add_cnt > new_arr_size :
                    new_arr_size *= 2
                array_dic[arr_num][1] = new_arr_size
                array_dic[arr_num][0] += add_cnt
            else:
                array_dic[arr_num][0] += add_cnt
        else:
            new_arr_size = 1
            while add_cnt > new_arr_size:
                new_arr_size *= 2
            array_dic[arr_num] = [add_cnt, new_arr_size]
        
    return answer

if __name__ == "__main__":
    queries = [[[1,1],[1,2],[1,4],[1,8]],[[2,10],[7,1],[2,5],[2,9],[7,32]]]
    for q in queries:
        print(solution(q))
    