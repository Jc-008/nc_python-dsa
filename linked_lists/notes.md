Problem: 
#  Remove Linked List Elements

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

 
## **Example 1:**
![](example1.jpg "example 1")
```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

## **Example 2:**
```
Input: head = [], val = 1
Output: []
```

## **Example 3:**
```
Input: head = [7,7,7,7], val = 7
Output: []
```



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