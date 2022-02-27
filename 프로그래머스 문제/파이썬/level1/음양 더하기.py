absolutes = [4,7,12]
signs = [True,False,True]
def solution(absolutes, signs):
    result = 0
    for pair in zip(absolutes, signs):
        if pair[1]:
            result += pair[0]
        else:
            result-= pair[0]
    
    return result

print(solution(absolutes, signs))