# 트리
import sys
n = int(input())
tree = {}
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
# 전위 순회
def preorder(node):
    print(node.data, end = '')
    if node.left != None:
        preorder(tree[node.left])
    if node.right != None:
        preorder(tree[node.right])
        
# 중위 순회 -> 노드를 중간에 확인
def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end = '')
    if node.right != None:
        in_order(tree[node.right])

# 후위 순회 -> 노드를 제일 마지막에 확인
def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end = '')


for _ in range(n):
    a,b,c = input().rstrip().split()
    if b == '.':
        b = None
    if c == '.':
        c = None
    tree[a] = Node(a, b, c)

preorder(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
