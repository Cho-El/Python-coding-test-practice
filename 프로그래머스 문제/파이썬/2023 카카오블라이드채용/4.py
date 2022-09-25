import sys
sys.setrecursionlimit(10**6)

def solution(numbers):
    global answer
    answer = []
    for n in numbers:
        str = bin(n)[2:]
        lenMax = 1
        while lenMax < len(str):
            lenMax *= 2
        str = '0' * ((lenMax-1) - len(str)) + str
        if treePossible(str):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

def treePossible(num):
    center = len(num)//2
    
    if len(num) == 1:
        return True
    
    if num[center] == '0':
        return False
    else:
        left_num = num[:center]
        right_num = num[center + 1:]
        
        if (not treePossible(right_num) or not treePossible(left_num)):
            return False
    
    return True
if __name__ == "__main__":
    print(solution([58]))