class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


class Solution:
    def reverseListIter(self, head: ListNode) -> ListNode:
        prev = None
        curr = head 

        while curr != None:
            nextTemp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nextTemp

        return prev 

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head 

        p = self.reverseListRecursive(head.next)
        head.next.next = head 
        head.next = None 
        return p


l1 = ListNode(val=1)
l2 = ListNode(val=2)
l3 = ListNode(val=3)
l4 = ListNode(val=4)
l5 = ListNode(val=5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
s.reverseListRecursive(l1)
print(s)
