class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        

    def get(self, index: int) -> int:
        if self.size <= index or index <0:
            return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head
        to_add = ListNode(val)
        cur.next, to_add.next =to_add,  cur.next
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        to_add = ListNode(val)
        cur.next = to_add
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        to_add = ListNode(val)
        to_add.next, cur.next = cur.next, to_add
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)