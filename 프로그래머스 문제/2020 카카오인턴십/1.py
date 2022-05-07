from collections import defaultdict

def solution(survey, choices):
    score_list = [3,2,1,0,1,2,3]
    answer = ''
    total_score = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    pair = [['R','T'], ['C','F'],['J','M'],['A','N']]
    for sur,cho in zip(survey,choices):
        if cho <= 3:
            total_score[sur[0]] += score_list[cho-1]
        else:
            total_score[sur[1]] += score_list[cho-1]
    
    # 종합
    for p in pair:
        x, y = p
        if total_score[x] > total_score[y]:
            answer += x
        elif total_score[x] < total_score[y]:
            answer += y
        else:
            temp = sorted(p)
            answer += temp[0]

    return answer

if __name__ == '__main__':
    a = [(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]),(["TR", "RT", "TR"],	[7, 1, 3])]
    for i in a:
        survey, choices = i
        print(solution(survey, choices))