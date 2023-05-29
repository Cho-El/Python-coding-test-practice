# 연결리스트
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# tail이 존재하는 SLinkedList
class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def addLast(self, value) -> None:
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode
    def addFirst(self, value) -> None:
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head = newNode
    def findNode(self, value) -> None:
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            node = node.next

class Node2:
    def __init__(self,value) -> None:
        self.value = value
        self.prev = None
        self.next = None
        
class DLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def addLast(self, value) -> None:
        newNode = Node2(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def addFirst(self, value) -> None:
        newNode = Node2(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            
    def findNode(self, value) -> Node2:
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            node = node.next
        raise RuntimeError("Node not found")
    
    def findNodeAndMovingHead(self, value) -> None:
        node = self.findNode(value)
        # 해당 노드가 첫 노드일 때 -> 변화 필요 없음
        if node == self.head:
            return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev = node
        self.head = node
    
    def findNodeAndMovingTail(self, value) -> None:
        node = self.findNode(value)
        # 해당 노드가 끝 노드 일 때 -> 변화 필요 없음
        if node == self.tail:
            return
        # 해당 노드가 head일 때
        elif node == self.head:
            self.head = node.next
            self.head.prev = node.prev
        # 해당 노드가 중간 노드일 때
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = self.tail
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node
    
    def returnAllNode(self) -> list:
        result = []
        node = self.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result
    
import sys
input = sys.stdin.readline
n = int(input())
# array = [2,4,1,-2,3,5,-1]
array = [2,1,3,-2,-2,-3,-3,1,4]
dList = DLinkedList()

for i in range(1, n + 1):
    dList.addLast(i)

for a in array:
    if a > 0 :
        dList.findNodeAndMovingHead(a)
    else:
        dList.findNodeAndMovingTail(abs(a))

print(dList.returnAllNode())