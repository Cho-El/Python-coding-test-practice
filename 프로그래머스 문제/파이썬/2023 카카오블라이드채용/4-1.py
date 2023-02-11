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
    root = int(num[rootIdx])
    leftTree = makeTree(num,startIdx, rootIdx - 1)
    rightTree = makeTree(num, rootIdx + 1, endIdx)
    
    return Tree(root, leftTree, rightTree)

def checkTree(tree, parent):
    global check
    
    # leaf 노드인지 체크
    if tree == None:
        return
    
    # 부모 노드가 0인데 자식의 값은 1인 경우
    if parent == 0:
        if tree.value == 1:
            check = False
            return
    
    checkTree(tree.left, tree.value)
    checkTree(tree.right, tree.value)
    
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
        tree = makeTree('1100000',0,6)
        
        if tree.value == 0: # 루트 노드가 0인경우
            result.append(0)
        else: # 아닌 경우 
            check = True
            checkTree(tree, 1)
            if check:
                result.append(1)
            else:
                result.append(0)
    
    return result

    
if __name__ == "__main__":
    numbers = [[7,42,5],[63,111,95]]
    for n in numbers:
        print(solution(n))