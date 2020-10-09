class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        # if linked list does not exist
        if not self.head:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.size == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        # self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return -1
        new_node = Node(val)
        cur = self.head
        if index != 0:
            for i in range(index - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
            # print('...')
            # print(cur.next.val)
            # print('...')
            if index == self.size:
                self.tail = new_node
            self.size += 1
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size:
            return -1
        cur = self.head
        if index != 0:
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        elif index == 0 :
            self.head = cur.next
            if self.size == 1:
                self.head = None
                self.tail = None
        self.size -= 1

    def pr(self):
        cur = self.head
        print(self.size)
        print('---')
        print(cur.val)
        for i in range(self.size-1):
            cur = cur.next
            print(cur.val)
        print('...head...')
        print(self.head)
        print('...head...')
        print('...tail...')
        print(self.tail)
        print('...tail...')

list = MyLinkedList()
list.addAtHead(1)

list.addAtTail(3)

list.addAtIndex(1,2)
print(list.get(1))
list.deleteAtIndex(0)
print(list.get(0))
list.pr()

# 问题
# 边际条件-当index==self.size
# 改function addAtIndex()
