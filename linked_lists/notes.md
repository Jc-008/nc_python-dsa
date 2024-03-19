Problem is : 



## Used in the python terminal to explain about the dummy node, prev, current and also removing nodes for problem (Remove Linked List Elements) 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)

head
<__main__.ListNode object at 0x7fd30d8772e0>

head.val
1
head.next
dummy = ListNode(0)
dummy.next = head
node = ListNode(2)
head.next = node
prev = dummy
current = head

prev
<__main__.ListNode object at 0x7fd30d8c1d30>

current
<__main__.ListNode object at 0x7fd30d8772e0>

current.next
<__main__.ListNode object at 0x7fd30d8a9a90>

node
<__main__.ListNode object at 0x7fd30d8a9a90>

prev.next
<__main__.ListNode object at 0x7fd30d8772e0>

prev.next = current.next
prev.next
<__main__.ListNode object at 0x7fd30d8a9a90>

dummy
<__main__.ListNode object at 0x7fd30d8c1d30>