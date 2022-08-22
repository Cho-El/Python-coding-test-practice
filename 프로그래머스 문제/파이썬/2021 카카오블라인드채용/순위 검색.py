from collections import defaultdict
import bisect

def solution(info, query):
    
    language = ['cpp','java','python','-']
    job = ['backend', 'frontend','-']
    career = ['junior','senior','-']
    food = ['chicken','pizza','-']
    result = []
    all_info = defaultdict(list)
    
    for l in language:
        for j in job:
            for c in career:
                for f in food:
                    temp = ''
                    temp += l + j + c + f
                    all_info[temp]
     
    for i in info:
        l_tmp, j_tmp, c_tmp, f_tmp, score = i.split()
        for lt in ['-',l_tmp]:
            for jt in ['-',j_tmp]:
                for ct in ['-',c_tmp]:
                    for ft in ['-',f_tmp]:
                        temp = ''
                        temp += lt + jt + ct + ft
                        all_info[temp].append(int(score))
    
    for i in all_info.values():
        i.sort()
    
    for q in query:
        temp = q.split()
        target_score = int(temp[-1])
        
        while 'and' in temp:
            temp.remove('and')
        
        querystring = ''.join(temp[:-1])
        target_value_list = all_info[querystring]
        [50,100,100,100,100,200,300]
        
        if target_value_list:
            result.append(len(target_value_list) - bisect.bisect_left(target_value_list, target_score))
        else:
            result.append(0)
            
    return result
        
if __name__ == "__main__":
    info = [[],[],[],[]]
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))