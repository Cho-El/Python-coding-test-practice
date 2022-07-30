# 이진 검색 트리

import sys
sys.setrecursionlimit(10 ** 6)

preorder = []
def postorder(start, end):
    
    # 시작이 end를 넘으면
    if start >= end:
        return
    root = preorder[start]

    # root보다 큰게 없는 경우 -> 오른쪽 노드에 값이 없다.
    if root >= preorder[end - 1]:
        postorder(start + 1, end)
        print(root)
        return
    
    idx = 0
    # 오른쪽 노드를 찾기
    for i in range(start + 1, end):
        if preorder[i] > root:
            idx = i
            break
    
    postorder(start + 1, idx)
    postorder(idx, end)
    print(root)
    
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
    
postorder(0, len(preorder))