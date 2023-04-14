def changeToBinaryNum(number):
    temp = []
    while number > 0:
        temp.append(str(number % 2))
        number //= 2
    
    temp.reverse()
    binaryNum = ''.join(temp)
    i = 1
    while len(binaryNum) > 2 ** i - 1:
        i += 1
    
    binaryNum = '0' * (2 ** i - 1 - len(binaryNum)) + binaryNum    
    return binaryNum
        
def checkBinaryTree(target, startIdx, endIdx, isNode):
    if startIdx > endIdx:
        return True
    mid = (startIdx + endIdx) // 2
    
    # 이진트리가 될 수 없는 경우
    if not int(isNode) and target[mid] == '1':
        return False
    
    leftTree = checkBinaryTree(target, startIdx, mid - 1, target[mid])
    if leftTree:
        rightTree = checkBinaryTree(target, mid + 1, endIdx, target[mid])
        if rightTree:
            return True
        else:
            return False
    else:
        return False
    
    
def solution(numbers):
    answer = []
    for number in numbers:
        targetNum = changeToBinaryNum(number)
        if targetNum[(len(targetNum) - 1) // 2] == '0':
            answer.append(0)
        elif checkBinaryTree(targetNum,0,len(targetNum) - 1, '1'):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

print(solution([7,42,5,58]))
print(solution([63,111,95]))