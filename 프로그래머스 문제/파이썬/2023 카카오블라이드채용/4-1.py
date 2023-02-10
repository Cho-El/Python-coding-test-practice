#
import sys
class Tree:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right
        
def makeTree(num, startIdx, endIdx):
    if startIdx > endIdx :
        return None
    
    rootIdx = (startIdx + endIdx) // 2
    root = num[rootIdx]
    leftTree = makeTree(num,startIdx, rootIdx - 1)
    rightTree = makeTree(num, rootIdx + 1, endIdx)
    
    return Tree(root, leftTree, rightTree)

def checkTree(tree):
    global check
    # leaf 노드인지 체크
    if tree.left == None or tree.right ==None:
        return
    
    # 아니라면 root가 0인지 체크
    if tree.value == '0':
        check = False
        return
    
    checkTree(tree.left)
    checkTree(tree.right)
    
def solution(numbers):
    global check
    result = []
    for n in numbers:
        targetNum = bin(n)[2:]
        i = 0
        while 2 ** i < len(targetNum):
            i += 1
        targetNum = '0' * (2 ** i - 1 - len(targetNum)) + targetNum
        tree = makeTree(targetNum,0,len(targetNum) - 1)
        check = True
        checkTree(tree)
        if check:
            result.append(1)
        else:
            result.append(0)
    
    return result
        
    
if __name__ == "__main__":
    numbers = [[7,42,5],[63,111,95]]
    for n in numbers:
        print(solution(n))